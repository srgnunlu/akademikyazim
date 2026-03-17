"""Agent implementations."""

from agents.core.source_hunter import SourceHunterAgent
from agents.core.methodology_checker import MethodologyCheckerAgent
from agents.core.citation_verifier import CitationVerifierAgent
from agents.core.rq_refiner import RQRefinerAgent
from agents.core.literature_analyst import LiteratureAnalystAgent
from agents.core.argument_builder import ArgumentBuilderAgent
from agents.core.draft_writer import DraftWriterAgent
from agents.core.self_critic import SelfCriticAgent
from agents.core.orchestrator import OrchestratorAgent

__all__ = [
    "SourceHunterAgent",
    "MethodologyCheckerAgent",
    "CitationVerifierAgent",
    "RQRefinerAgent",
    "LiteratureAnalystAgent",
    "ArgumentBuilderAgent",
    "DraftWriterAgent",
    "SelfCriticAgent",
    "OrchestratorAgent",
]
