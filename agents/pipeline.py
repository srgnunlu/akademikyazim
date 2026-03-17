"""Pipeline — defines and executes the Idea → Article pipeline.

Orchestrates the sequence of agent tasks from initial idea to final output,
with configurable checkpoints for human review.

Usage:
    from agents.pipeline import Pipeline, PipelineConfig
    config = PipelineConfig(autonomy="balanced", language="tr")
    pipeline = Pipeline(config, agent_config, project_dir)
    result = await pipeline.execute(idea="...")
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Awaitable

logger = logging.getLogger(__name__)


class TaskType(str, Enum):
    RESEARCH_QUESTION = "research_question"
    LITERATURE_SEARCH = "literature_search"
    LITERATURE_ANALYSIS = "literature_analysis"
    ARGUMENT_BUILDING = "argument_building"
    DRAFTING = "drafting"
    SELF_REVIEW = "self_review"
    FULL_REVIEW = "full_review"
    OUTPUT = "output"


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    CHECKPOINT = "checkpoint"  # Waiting for human review
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class Task:
    """A single pipeline task."""

    id: str
    type: TaskType
    title: str
    agent: str
    input_data: dict = field(default_factory=dict)
    dependencies: list[str] = field(default_factory=list)
    human_checkpoint: bool = False
    status: TaskStatus = TaskStatus.PENDING
    result: dict = field(default_factory=dict)
    error: str = ""
    started_at: float = 0
    completed_at: float = 0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type.value,
            "title": self.title,
            "agent": self.agent,
            "status": self.status.value,
            "human_checkpoint": self.human_checkpoint,
            "error": self.error,
            "duration": self.completed_at - self.started_at if self.completed_at else 0,
        }


@dataclass
class PipelineConfig:
    """Pipeline configuration."""

    autonomy: str = "balanced"  # "maximal", "balanced", "conservative"
    language: str = "tr"
    field: str = ""
    document_type: str = "article"
    max_draft_iterations: int = 3
    provider: str = "anthropic"


@dataclass
class PipelineResult:
    """Result of a complete pipeline execution."""

    success: bool
    tasks: list[Task]
    outputs: dict = field(default_factory=dict)
    total_time: float = 0
    checkpoints_passed: int = 0

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "total_time": round(self.total_time, 1),
            "checkpoints_passed": self.checkpoints_passed,
            "tasks": [t.to_dict() for t in self.tasks],
            "output_files": list(self.outputs.keys()),
        }


class Pipeline:
    """Idea → Article pipeline executor."""

    def __init__(
        self,
        config: PipelineConfig,
        project_dir: Path,
    ):
        self.config = config
        self.project_dir = project_dir
        self.tasks: list[Task] = []
        self._checkpoint_callback: Callable[..., Awaitable[bool]] | None = None

    def set_checkpoint_callback(
        self, callback: Callable[..., Awaitable[bool]]
    ) -> None:
        """Set a callback for human checkpoints.

        The callback receives (task, result) and should return True to proceed
        or False to halt the pipeline.
        """
        self._checkpoint_callback = callback

    def build_pipeline(self, idea: str) -> list[Task]:
        """Build the task list for idea → article pipeline.

        Checkpoint placement depends on autonomy level:
        - balanced: 3 checkpoints (RQ, arguments, drafts)
        - maximal: 2 checkpoints (RQ, final)
        - conservative: checkpoint at every stage
        """
        cfg = self.config
        is_balanced = cfg.autonomy == "balanced"
        is_conservative = cfg.autonomy == "conservative"

        self.tasks = [
            # Stage 1: Research Question Refinement
            Task(
                id="rq_refine",
                type=TaskType.RESEARCH_QUESTION,
                title="Araştırma Sorusu Rafine / Research Question Refinement",
                agent="rq_refiner",
                input_data={"idea": idea, "field": cfg.field, "document_type": cfg.document_type},
                human_checkpoint=True,  # Always checkpoint for RQ
            ),
            # Stage 2: Literature Search
            Task(
                id="lit_search",
                type=TaskType.LITERATURE_SEARCH,
                title="Kaynak Arama / Literature Search",
                agent="source_hunter",
                dependencies=["rq_refine"],
                human_checkpoint=is_conservative,
            ),
            # Stage 3: Literature Analysis
            Task(
                id="lit_analysis",
                type=TaskType.LITERATURE_ANALYSIS,
                title="Kaynak Analizi / Literature Analysis",
                agent="literature_analyst",
                dependencies=["lit_search"],
                human_checkpoint=is_conservative,
            ),
            # Stage 4: Argument Building
            Task(
                id="arg_build",
                type=TaskType.ARGUMENT_BUILDING,
                title="Argüman Yapısı / Argument Structure",
                agent="argument_builder",
                dependencies=["lit_analysis"],
                human_checkpoint=is_balanced or is_conservative,
            ),
            # Stage 5: Draft Writing (with self-review loop)
            Task(
                id="drafting",
                type=TaskType.DRAFTING,
                title="Taslak Yazımı / Draft Writing",
                agent="draft_writer",
                dependencies=["arg_build"],
                human_checkpoint=is_balanced or is_conservative,
            ),
            # Stage 6: Full Document Review
            Task(
                id="full_review",
                type=TaskType.FULL_REVIEW,
                title="Bütünsel İnceleme / Full Document Review",
                agent="self_critic",
                dependencies=["drafting"],
                human_checkpoint=is_conservative,
            ),
            # Stage 7: Output Generation
            Task(
                id="output",
                type=TaskType.OUTPUT,
                title="Çıktı Üretimi / Output Generation",
                agent="output",
                dependencies=["full_review"],
                human_checkpoint=False,
            ),
        ]

        return self.tasks

    def get_status(self) -> dict:
        """Get current pipeline status."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.status == TaskStatus.COMPLETED)
        current = next(
            (t for t in self.tasks if t.status in (TaskStatus.RUNNING, TaskStatus.CHECKPOINT)),
            None,
        )
        return {
            "total_tasks": total,
            "completed": completed,
            "progress": completed / max(total, 1),
            "current_task": current.to_dict() if current else None,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    def get_next_task(self) -> Task | None:
        """Get the next runnable task (all dependencies completed)."""
        for task in self.tasks:
            if task.status != TaskStatus.PENDING:
                continue
            deps_met = all(
                any(t.id == dep and t.status == TaskStatus.COMPLETED for t in self.tasks)
                for dep in task.dependencies
            )
            if deps_met:
                return task
        return None

    def save_state(self) -> None:
        """Save pipeline state to .tezatlas/pipeline_state.json."""
        state_path = self.project_dir / ".tezatlas" / "pipeline_state.json"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state = {
            "config": {
                "autonomy": self.config.autonomy,
                "language": self.config.language,
                "field": self.config.field,
                "document_type": self.config.document_type,
            },
            "tasks": [t.to_dict() for t in self.tasks],
            "saved_at": time.time(),
        }
        state_path.write_text(
            json.dumps(state, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def load_state(self) -> bool:
        """Load pipeline state from file. Returns True if loaded successfully."""
        state_path = self.project_dir / ".tezatlas" / "pipeline_state.json"
        if not state_path.exists():
            return False
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            for task_data in state.get("tasks", []):
                for task in self.tasks:
                    if task.id == task_data["id"]:
                        task.status = TaskStatus(task_data["status"])
                        break
            return True
        except (json.JSONDecodeError, KeyError):
            return False
