"""Tests for agents/pipeline.py — pipeline definition and execution."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from agents.pipeline import Pipeline, PipelineConfig, Task, TaskStatus, TaskType


@pytest.fixture
def temp_project(tmp_path):
    return tmp_path


class TestPipelineConfig:
    def test_defaults(self):
        config = PipelineConfig()
        assert config.autonomy == "balanced"
        assert config.language == "tr"
        assert config.document_type == "article"
        assert config.max_draft_iterations == 3

    def test_custom_config(self):
        config = PipelineConfig(
            autonomy="maximal",
            language="en",
            field="economics",
        )
        assert config.autonomy == "maximal"
        assert config.field == "economics"


class TestPipeline:
    def test_build_pipeline_balanced(self, temp_project):
        config = PipelineConfig(autonomy="balanced")
        pipeline = Pipeline(config, temp_project)
        tasks = pipeline.build_pipeline("Test idea")

        assert len(tasks) == 7

        # Check checkpoint placement for balanced mode
        checkpoints = {t.id: t.human_checkpoint for t in tasks}
        assert checkpoints["rq_refine"] is True       # Always
        assert checkpoints["lit_search"] is False      # Auto in balanced
        assert checkpoints["lit_analysis"] is False    # Auto in balanced
        assert checkpoints["arg_build"] is True        # Checkpoint #2
        assert checkpoints["drafting"] is True         # Checkpoint #3
        assert checkpoints["full_review"] is False     # Auto in balanced
        assert checkpoints["output"] is False          # Never

    def test_build_pipeline_conservative(self, temp_project):
        config = PipelineConfig(autonomy="conservative")
        pipeline = Pipeline(config, temp_project)
        tasks = pipeline.build_pipeline("Test idea")

        # Conservative = checkpoint at every stage (except output)
        checkpoint_count = sum(1 for t in tasks if t.human_checkpoint)
        assert checkpoint_count >= 5

    def test_build_pipeline_maximal(self, temp_project):
        config = PipelineConfig(autonomy="maximal")
        pipeline = Pipeline(config, temp_project)
        tasks = pipeline.build_pipeline("Test idea")

        # Maximal = only RQ checkpoint
        checkpoint_count = sum(1 for t in tasks if t.human_checkpoint)
        assert checkpoint_count == 1

    def test_get_next_task(self, temp_project):
        config = PipelineConfig()
        pipeline = Pipeline(config, temp_project)
        pipeline.build_pipeline("Test idea")

        # First task should be rq_refine (no dependencies)
        next_task = pipeline.get_next_task()
        assert next_task is not None
        assert next_task.id == "rq_refine"

    def test_dependency_resolution(self, temp_project):
        config = PipelineConfig()
        pipeline = Pipeline(config, temp_project)
        pipeline.build_pipeline("Test idea")

        # lit_search depends on rq_refine
        # Should not be next until rq_refine is completed
        rq_task = pipeline.tasks[0]
        rq_task.status = TaskStatus.RUNNING  # Not completed yet

        next_task = pipeline.get_next_task()
        assert next_task is None  # No task has all deps met

        rq_task.status = TaskStatus.COMPLETED
        next_task = pipeline.get_next_task()
        assert next_task is not None
        assert next_task.id == "lit_search"

    def test_get_status(self, temp_project):
        config = PipelineConfig()
        pipeline = Pipeline(config, temp_project)
        pipeline.build_pipeline("Test idea")

        status = pipeline.get_status()
        assert status["total_tasks"] == 7
        assert status["completed"] == 0
        assert status["progress"] == 0.0

        # Complete first task
        pipeline.tasks[0].status = TaskStatus.COMPLETED
        status = pipeline.get_status()
        assert status["completed"] == 1
        assert status["progress"] > 0

    def test_save_and_load_state(self, temp_project):
        config = PipelineConfig()
        pipeline = Pipeline(config, temp_project)
        pipeline.build_pipeline("Test idea")

        # Complete first task
        pipeline.tasks[0].status = TaskStatus.COMPLETED
        pipeline.save_state()

        # Verify state file exists
        state_path = temp_project / ".tezatlas" / "pipeline_state.json"
        assert state_path.exists()

        # Load state in new pipeline
        pipeline2 = Pipeline(config, temp_project)
        pipeline2.build_pipeline("Test idea")
        loaded = pipeline2.load_state()
        assert loaded is True
        assert pipeline2.tasks[0].status == TaskStatus.COMPLETED


class TestTask:
    def test_to_dict(self):
        task = Task(
            id="test",
            type=TaskType.RESEARCH_QUESTION,
            title="Test Task",
            agent="rq_refiner",
            human_checkpoint=True,
        )
        d = task.to_dict()
        assert d["id"] == "test"
        assert d["type"] == "research_question"
        assert d["agent"] == "rq_refiner"
        assert d["human_checkpoint"] is True
        assert d["status"] == "pending"
