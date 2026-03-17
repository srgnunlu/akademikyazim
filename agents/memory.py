"""Shared agent memory system — file-backed persistent store.

Agents share state through this memory system. Each entry is tagged with
the producing agent, a key, and optional metadata. Memory persists across
sessions via JSON files in .tezatlas/memory/.

Usage:
    memory = AgentMemory(project_dir)
    memory.store("research_question", {"rq": "..."}, agent="rq_refiner")
    entry = memory.retrieve("research_question")
    results = memory.search("monetary policy", top_k=5)
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class MemoryEntry:
    """A single memory entry produced by an agent."""

    key: str
    value: Any
    agent: str
    timestamp: float = field(default_factory=time.time)
    metadata: dict = field(default_factory=dict)
    session_id: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> MemoryEntry:
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class AgentMemory:
    """File-backed shared memory for multi-agent coordination.

    Storage layout:
        .tezatlas/memory/
        ├── session_memory.json   — current session entries
        ├── long_term.json        — cross-session persistent entries
        └── agent_outputs/        — per-agent output archive
            ├── rq_refiner/
            ├── literature_analyst/
            └── ...
    """

    def __init__(self, project_dir: Path, session_id: str = ""):
        self.project_dir = project_dir
        self.session_id = session_id or str(int(time.time()))
        self._base = project_dir / ".tezatlas" / "memory"
        self._session_path = self._base / "session_memory.json"
        self._longterm_path = self._base / "long_term.json"
        self._outputs_dir = self._base / "agent_outputs"
        self._ensure_dirs()
        self._session: dict[str, MemoryEntry] = {}
        self._longterm: dict[str, MemoryEntry] = {}
        self._load()

    def _ensure_dirs(self) -> None:
        self._base.mkdir(parents=True, exist_ok=True)
        self._outputs_dir.mkdir(parents=True, exist_ok=True)

    # ── Core operations ──────────────────────────────────────────────

    def store(
        self,
        key: str,
        value: Any,
        agent: str,
        metadata: dict | None = None,
        persist: bool = False,
    ) -> MemoryEntry:
        """Store a value. If persist=True, also write to long-term memory."""
        entry = MemoryEntry(
            key=key,
            value=value,
            agent=agent,
            timestamp=time.time(),
            metadata=metadata or {},
            session_id=self.session_id,
        )
        self._session[key] = entry
        if persist:
            self._longterm[key] = entry
        self._save()

        # Archive to agent outputs
        agent_dir = self._outputs_dir / agent
        agent_dir.mkdir(exist_ok=True)
        out_path = agent_dir / f"{key}.json"
        out_path.write_text(
            json.dumps(entry.to_dict(), ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )
        return entry

    def retrieve(self, key: str) -> MemoryEntry | None:
        """Retrieve by key. Session memory takes precedence over long-term."""
        return self._session.get(key) or self._longterm.get(key)

    def retrieve_value(self, key: str, default: Any = None) -> Any:
        """Shortcut to get just the value."""
        entry = self.retrieve(key)
        return entry.value if entry else default

    def search(self, query: str, top_k: int = 5) -> list[MemoryEntry]:
        """Simple keyword search across all memory entries."""
        query_lower = query.lower()
        scored: list[tuple[int, MemoryEntry]] = []

        all_entries = {**self._longterm, **self._session}
        for entry in all_entries.values():
            score = 0
            value_str = json.dumps(entry.value, ensure_ascii=False, default=str).lower()
            for word in query_lower.split():
                if word in entry.key.lower():
                    score += 3
                if word in value_str:
                    score += 1
                if word in entry.agent.lower():
                    score += 1
            if score > 0:
                scored.append((score, entry))

        scored.sort(key=lambda x: -x[0])
        return [entry for _, entry in scored[:top_k]]

    def get_context_for(self, agent_name: str) -> list[MemoryEntry]:
        """Get all memory entries relevant to a specific agent's needs."""
        # Return all entries from session + long-term, sorted by recency
        all_entries = {**self._longterm, **self._session}
        entries = list(all_entries.values())
        entries.sort(key=lambda e: -e.timestamp)
        return entries

    def get_agent_outputs(self, agent_name: str) -> list[MemoryEntry]:
        """Get all outputs produced by a specific agent."""
        all_entries = {**self._longterm, **self._session}
        return [e for e in all_entries.values() if e.agent == agent_name]

    def get_pipeline_state(self) -> dict[str, Any]:
        """Get the current pipeline state summary."""
        return {
            "session_id": self.session_id,
            "session_entries": len(self._session),
            "longterm_entries": len(self._longterm),
            "agents_active": list({e.agent for e in self._session.values()}),
            "keys": list(self._session.keys()),
        }

    def clear_session(self) -> None:
        """Clear session memory (long-term persists)."""
        self._session.clear()
        self._save()

    # ── Serialization ────────────────────────────────────────────────

    def _load(self) -> None:
        if self._session_path.exists():
            try:
                raw = json.loads(self._session_path.read_text(encoding="utf-8"))
                self._session = {
                    k: MemoryEntry.from_dict(v) for k, v in raw.items()
                }
            except (json.JSONDecodeError, TypeError):
                logger.warning("Corrupt session memory, starting fresh")
                self._session = {}

        if self._longterm_path.exists():
            try:
                raw = json.loads(self._longterm_path.read_text(encoding="utf-8"))
                self._longterm = {
                    k: MemoryEntry.from_dict(v) for k, v in raw.items()
                }
            except (json.JSONDecodeError, TypeError):
                logger.warning("Corrupt long-term memory, starting fresh")
                self._longterm = {}

    def _save(self) -> None:
        self._session_path.write_text(
            json.dumps(
                {k: v.to_dict() for k, v in self._session.items()},
                ensure_ascii=False, indent=2, default=str,
            ),
            encoding="utf-8",
        )
        if self._longterm:
            self._longterm_path.write_text(
                json.dumps(
                    {k: v.to_dict() for k, v in self._longterm.items()},
                    ensure_ascii=False, indent=2, default=str,
                ),
                encoding="utf-8",
            )
