"""Tests for agents/memory.py — shared agent memory system."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from agents.memory import AgentMemory, MemoryEntry


@pytest.fixture
def temp_project(tmp_path):
    """Create a temporary project directory."""
    return tmp_path


class TestMemoryEntry:
    def test_to_dict_roundtrip(self):
        entry = MemoryEntry(
            key="test_key",
            value={"data": "hello"},
            agent="test_agent",
            timestamp=1234567890.0,
            metadata={"version": 1},
            session_id="sess_1",
        )
        d = entry.to_dict()
        restored = MemoryEntry.from_dict(d)
        assert restored.key == "test_key"
        assert restored.value == {"data": "hello"}
        assert restored.agent == "test_agent"
        assert restored.session_id == "sess_1"

    def test_from_dict_ignores_extra_fields(self):
        d = {
            "key": "k",
            "value": "v",
            "agent": "a",
            "extra_field": "ignored",
        }
        entry = MemoryEntry.from_dict(d)
        assert entry.key == "k"
        assert entry.value == "v"


class TestAgentMemory:
    def test_store_and_retrieve(self, temp_project):
        memory = AgentMemory(temp_project)
        memory.store("rq", {"question": "What is X?"}, agent="rq_refiner")

        entry = memory.retrieve("rq")
        assert entry is not None
        assert entry.value["question"] == "What is X?"
        assert entry.agent == "rq_refiner"

    def test_retrieve_nonexistent(self, temp_project):
        memory = AgentMemory(temp_project)
        assert memory.retrieve("nonexistent") is None

    def test_retrieve_value_with_default(self, temp_project):
        memory = AgentMemory(temp_project)
        assert memory.retrieve_value("missing", "default") == "default"

    def test_search(self, temp_project):
        memory = AgentMemory(temp_project)
        memory.store("topic_a", {"content": "monetary policy analysis"}, agent="agent_a")
        memory.store("topic_b", {"content": "climate change impact"}, agent="agent_b")
        memory.store("topic_c", {"content": "monetary base expansion"}, agent="agent_c")

        results = memory.search("monetary", top_k=5)
        assert len(results) >= 2
        # Both "monetary" entries should rank higher
        keys = [r.key for r in results]
        assert "topic_a" in keys
        assert "topic_c" in keys

    def test_persistence(self, temp_project):
        # Store in first instance
        mem1 = AgentMemory(temp_project, session_id="s1")
        mem1.store("key1", "value1", agent="a1")

        # Load in second instance
        mem2 = AgentMemory(temp_project, session_id="s1")
        entry = mem2.retrieve("key1")
        assert entry is not None
        assert entry.value == "value1"

    def test_long_term_persistence(self, temp_project):
        mem1 = AgentMemory(temp_project, session_id="s1")
        mem1.store("persistent", "data", agent="a", persist=True)
        mem1.clear_session()

        mem2 = AgentMemory(temp_project, session_id="s2")
        entry = mem2.retrieve("persistent")
        assert entry is not None
        assert entry.value == "data"

    def test_get_agent_outputs(self, temp_project):
        memory = AgentMemory(temp_project)
        memory.store("k1", "v1", agent="agent_a")
        memory.store("k2", "v2", agent="agent_b")
        memory.store("k3", "v3", agent="agent_a")

        outputs = memory.get_agent_outputs("agent_a")
        assert len(outputs) == 2

    def test_get_pipeline_state(self, temp_project):
        memory = AgentMemory(temp_project)
        memory.store("k1", "v1", agent="a1")
        memory.store("k2", "v2", agent="a2")

        state = memory.get_pipeline_state()
        assert state["session_entries"] == 2
        assert set(state["agents_active"]) == {"a1", "a2"}

    def test_agent_output_files(self, temp_project):
        memory = AgentMemory(temp_project)
        memory.store("test_output", {"result": 42}, agent="test_agent")

        # Check that output file was created
        output_file = temp_project / ".tezatlas" / "memory" / "agent_outputs" / "test_agent" / "test_output.json"
        assert output_file.exists()
        data = json.loads(output_file.read_text())
        assert data["value"]["result"] == 42

    def test_corrupt_memory_recovery(self, temp_project):
        # Write corrupt JSON
        mem_dir = temp_project / ".tezatlas" / "memory"
        mem_dir.mkdir(parents=True, exist_ok=True)
        (mem_dir / "session_memory.json").write_text("NOT JSON")

        # Should not crash, just start fresh
        memory = AgentMemory(temp_project)
        assert memory.retrieve("anything") is None
        # Should be able to store
        memory.store("new", "value", agent="test")
        assert memory.retrieve("new").value == "value"
