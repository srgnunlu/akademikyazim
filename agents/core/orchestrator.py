"""Orchestrator Agent — master coordinator for the multi-agent pipeline.

Drives the Idea → Article pipeline by:
1. Decomposing the task into pipeline stages
2. Selecting and invoking the right agent for each stage
3. Managing shared memory between agents
4. Handling checkpoints for human review
5. Coordinating the draft → review → revise loop
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Awaitable

from agents.config import AgentConfig
from agents.core.argument_builder import ArgumentBuilderAgent
from agents.core.draft_writer import DraftWriterAgent
from agents.core.literature_analyst import LiteratureAnalystAgent
from agents.core.rq_refiner import RQRefinerAgent
from agents.core.self_critic import SelfCriticAgent
from agents.core.source_hunter import SourceHunterAgent
from agents.memory import AgentMemory
from agents.pipeline import Pipeline, PipelineConfig, PipelineResult, Task, TaskStatus, TaskType
from agents.tools import ToolRegistry

logger = logging.getLogger(__name__)

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "orchestrator.md"


class OrchestratorAgent:
    """Master agent that coordinates the multi-agent pipeline."""

    def __init__(
        self,
        agent_config: AgentConfig,
        project_dir: Path,
        pipeline_config: PipelineConfig | None = None,
    ):
        self.agent_config = agent_config
        self.project_dir = project_dir
        self.config = pipeline_config or PipelineConfig()
        self.memory = AgentMemory(project_dir)
        self.tool_registry = ToolRegistry(project_dir)
        self.pipeline = Pipeline(self.config, project_dir)
        self._checkpoint_callback: Callable[..., Awaitable[dict]] | None = None
        self._progress_callback: Callable[[str, dict], None] | None = None

        # Load orchestrator prompt (used for complex decisions)
        if _PROMPT_PATH.exists():
            self._system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")
        else:
            self._system_prompt = ""

    def set_checkpoint_callback(
        self, callback: Callable[..., Awaitable[dict]]
    ) -> None:
        """Set callback for human checkpoints.

        Callback receives (task_id, task_title, result) and should return:
        {"approved": bool, "feedback": str, "selected": Any}
        """
        self._checkpoint_callback = callback

    def set_progress_callback(
        self, callback: Callable[[str, dict], None]
    ) -> None:
        """Set callback for progress updates."""
        self._progress_callback = callback

    def _report_progress(self, message: str, data: dict | None = None) -> None:
        if self._progress_callback:
            self._progress_callback(message, data or {})

    async def run(self, idea: str) -> PipelineResult:
        """Execute the full pipeline from idea to article.

        Args:
            idea: The raw research idea from the user.

        Returns:
            PipelineResult with all outputs and status.
        """
        start_time = time.time()
        checkpoints_passed = 0

        # Build pipeline
        self.pipeline.build_pipeline(idea)
        self._report_progress("Pipeline oluşturuldu", self.pipeline.get_status())

        # Store initial idea in memory
        self.memory.store("idea", idea, agent="orchestrator", persist=True)

        # Execute tasks sequentially
        while True:
            task = self.pipeline.get_next_task()
            if task is None:
                break

            task.status = TaskStatus.RUNNING
            task.started_at = time.time()
            self._report_progress(f"Çalışıyor: {task.title}", task.to_dict())

            try:
                result = await self._execute_task(task)
                task.result = result

                # Handle checkpoint
                if task.human_checkpoint:
                    task.status = TaskStatus.CHECKPOINT
                    self._report_progress(f"Onay bekleniyor: {task.title}", task.to_dict())

                    if self._checkpoint_callback:
                        response = await self._checkpoint_callback(
                            task.id, task.title, result
                        )
                        if not response.get("approved", True):
                            task.status = TaskStatus.FAILED
                            task.error = response.get("feedback", "Kullanıcı tarafından reddedildi")
                            break
                        # Store user selection in memory
                        if response.get("selected"):
                            self.memory.store(
                                f"{task.id}_selection",
                                response["selected"],
                                agent="user",
                                persist=True,
                            )
                        if response.get("feedback"):
                            self.memory.store(
                                f"{task.id}_feedback",
                                response["feedback"],
                                agent="user",
                            )
                    checkpoints_passed += 1

                task.status = TaskStatus.COMPLETED
                task.completed_at = time.time()
                self.pipeline.save_state()

            except Exception as exc:
                task.status = TaskStatus.FAILED
                task.error = str(exc)
                task.completed_at = time.time()
                logger.error("Task %s failed: %s", task.id, exc)
                self._report_progress(f"Hata: {task.title}", {"error": str(exc)})
                break

        # Build final result
        all_completed = all(
            t.status == TaskStatus.COMPLETED for t in self.pipeline.tasks
        )
        total_time = time.time() - start_time

        return PipelineResult(
            success=all_completed,
            tasks=self.pipeline.tasks,
            outputs=self._collect_outputs(),
            total_time=total_time,
            checkpoints_passed=checkpoints_passed,
        )

    async def _execute_task(self, task: Task) -> dict:
        """Execute a single pipeline task by dispatching to the right agent."""
        handlers = {
            TaskType.RESEARCH_QUESTION: self._run_rq_refiner,
            TaskType.LITERATURE_SEARCH: self._run_source_hunter,
            TaskType.LITERATURE_ANALYSIS: self._run_literature_analyst,
            TaskType.ARGUMENT_BUILDING: self._run_argument_builder,
            TaskType.DRAFTING: self._run_drafting_loop,
            TaskType.FULL_REVIEW: self._run_full_review,
            TaskType.OUTPUT: self._run_output,
        }

        handler = handlers.get(task.type)
        if not handler:
            return {"error": f"Unknown task type: {task.type}"}

        return await handler(task)

    async def _get_agent(self, agent_name: str) -> tuple:
        """Get provider and model for an agent."""
        return self.agent_config.get_agent_provider(agent_name)

    # ── Task Handlers ────────────────────────────────────────────────

    async def _run_rq_refiner(self, task: Task) -> dict:
        provider, model = await self._get_agent("rq_refiner")
        agent = RQRefinerAgent(provider, model)
        return await agent.run(
            idea=task.input_data.get("idea", ""),
            field=self.config.field,
            document_type=self.config.document_type,
            language=self.config.language,
            memory=self.memory,
        )

    async def _run_source_hunter(self, task: Task) -> dict:
        provider, model = await self._get_agent("source_hunter")
        agent = SourceHunterAgent(provider, model)

        # Get the selected RQ from memory
        rq_data = self.memory.retrieve_value("research_questions", {})
        selection = self.memory.retrieve_value("rq_refine_selection")
        rq = ""
        if selection:
            rq = selection if isinstance(selection, str) else str(selection)
        elif rq_data:
            rqs = rq_data.get("research_questions", [])
            if rqs:
                rq = rqs[0].get("question", "")

        # Get existing sources
        sources_dir = self.project_dir / "sources"
        existing = []
        if sources_dir.is_dir():
            existing = [f.stem for f in sources_dir.glob("*.pdf")]

        result = await agent.run(
            research_question=rq,
            field=self.config.field,
            existing_sources=existing,
            language_preference=self.config.language,
        )

        self.memory.store("source_search", result, agent="source_hunter", persist=True)
        return result

    async def _run_literature_analyst(self, task: Task) -> dict:
        provider, model = await self._get_agent("literature_analyst")
        agent = LiteratureAnalystAgent(provider, model, self.tool_registry)

        rq = self._get_rq_from_memory()

        # Load source notes from notes/ directory
        notes = self._load_source_notes()

        return await agent.run(
            research_question=rq,
            field=self.config.field,
            source_notes=notes,
            memory=self.memory,
        )

    async def _run_argument_builder(self, task: Task) -> dict:
        provider, model = await self._get_agent("argument_builder")
        agent = ArgumentBuilderAgent(provider, model)

        rq = self._get_rq_from_memory()
        lit_analysis = self.memory.retrieve_value("literature_analysis", {})
        notes = self._load_source_notes()

        return await agent.run(
            research_question=rq,
            literature_analysis=lit_analysis,
            source_notes=notes,
            field=self.config.field,
            document_type=self.config.document_type,
            language=self.config.language,
            memory=self.memory,
        )

    async def _run_drafting_loop(self, task: Task) -> dict:
        """Run draft → self-review → revise loop for each section."""
        provider_dw, model_dw = await self._get_agent("draft_writer")
        provider_sc, model_sc = await self._get_agent("self_critic")
        writer = DraftWriterAgent(provider_dw, model_dw)
        critic = SelfCriticAgent(provider_sc, model_sc, self.tool_registry)

        rq = self._get_rq_from_memory()
        arg_data = self.memory.retrieve_value("argument_structure", {})
        arguments = arg_data.get("arguments", []) if arg_data else []
        outline = arg_data.get("outline", {}) if arg_data else {}
        notes = self._load_source_notes()

        sections = outline.get("sections", [])
        if not sections:
            # Default sections for an article
            sections = [
                {"title": "Giriş / Introduction", "type": "intro"},
                {"title": "Literatür Taraması / Literature Review", "type": "literature"},
                {"title": "Yöntem / Methodology", "type": "method"},
                {"title": "Bulgular / Results", "type": "results"},
                {"title": "Tartışma / Discussion", "type": "discussion"},
                {"title": "Sonuç / Conclusion", "type": "conclusion"},
            ]

        all_drafts = {}
        for section in sections:
            title = section.get("title", "")
            section_type = section.get("type", "")
            section_args = [
                a for a in arguments
                if a.get("id") in section.get("argument_ids", [])
            ] or arguments

            self._report_progress(f"Yazılıyor: {title}", {"section": title})

            # Write initial draft
            draft_result = await writer.run(
                section_title=title,
                section_type=section_type,
                outline=section,
                arguments=section_args,
                source_notes=notes,
                research_question=rq,
                field=self.config.field,
                language=self.config.language,
                memory=self.memory,
            )

            # Self-review loop (max iterations)
            best_draft = draft_result
            for iteration in range(self.config.max_draft_iterations):
                draft_text = ""
                drafts = draft_result.get("drafts", [])
                if drafts:
                    draft_text = drafts[0].get("content", "")

                if not draft_text:
                    break

                review = await critic.run(
                    draft_text=draft_text,
                    section_type=section_type,
                    research_question=rq,
                    arguments=section_args,
                    source_notes=notes,
                    memory=self.memory,
                )

                # If review passes, we're done
                if review.get("pass", False) or review.get("overall_score", 0) >= 7:
                    best_draft = draft_result
                    best_draft["review"] = review
                    break

                # Otherwise revise
                self._report_progress(
                    f"Revizyon {iteration + 1}: {title}",
                    {"score": review.get("overall_score", 0)},
                )
                feedback = review.get("revision_instructions", "")
                draft_result = await writer.run(
                    section_title=title,
                    section_type=section_type,
                    outline=section,
                    arguments=section_args,
                    source_notes=notes,
                    research_question=rq,
                    field=self.config.field,
                    language=self.config.language,
                    revision_feedback=feedback,
                    memory=self.memory,
                )
                best_draft = draft_result
                best_draft["review"] = review

            all_drafts[section_type or title] = best_draft

        self.memory.store("all_drafts", all_drafts, agent="draft_writer", persist=True)
        return all_drafts

    async def _run_full_review(self, task: Task) -> dict:
        provider, model = await self._get_agent("self_critic")
        critic = SelfCriticAgent(provider, model, self.tool_registry)

        all_drafts = self.memory.retrieve_value("all_drafts", {})
        rq = self._get_rq_from_memory()

        sections = []
        for key, draft_data in all_drafts.items():
            drafts = draft_data.get("drafts", [])
            content = drafts[0].get("content", "") if drafts else ""
            sections.append({
                "title": key,
                "type": key,
                "content": content,
            })

        return await critic.review_full_document(
            sections=sections,
            research_question=rq,
            memory=self.memory,
        )

    async def _run_output(self, task: Task) -> dict:
        """Generate final output files."""
        all_drafts = self.memory.retrieve_value("all_drafts", {})
        outputs = {}

        # Combine all drafts into a single document
        combined = []
        for key, draft_data in all_drafts.items():
            drafts = draft_data.get("drafts", [])
            if drafts:
                content = drafts[0].get("content", "")
                combined.append(f"## {key}\n\n{content}")

        full_text = "\n\n".join(combined)

        # Write output markdown
        output_path = self.project_dir / "drafts" / "full_draft.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(full_text, encoding="utf-8")
        outputs["full_draft.md"] = str(output_path)

        return {"files": outputs, "word_count": len(full_text.split())}

    # ── Helpers ──────────────────────────────────────────────────────

    def _get_rq_from_memory(self) -> str:
        """Get the active research question from memory."""
        selection = self.memory.retrieve_value("rq_refine_selection")
        if selection:
            return selection if isinstance(selection, str) else str(selection)
        rq_data = self.memory.retrieve_value("research_questions", {})
        if rq_data:
            rqs = rq_data.get("research_questions", [])
            if rqs:
                return rqs[0].get("question", "")
        return self.memory.retrieve_value("idea", "")

    def _load_source_notes(self) -> list[dict]:
        """Load source notes from the notes/ directory."""
        from core.literature_intel import NoteIndex
        notes_dir = self.project_dir / "notes"
        if not notes_dir.is_dir():
            return []
        index = NoteIndex(notes_dir)
        return index.notes

    def _collect_outputs(self) -> dict:
        """Collect all generated output files."""
        outputs = {}
        drafts_dir = self.project_dir / "drafts"
        if drafts_dir.is_dir():
            for f in drafts_dir.glob("*.md"):
                outputs[f.name] = str(f)
        return outputs
