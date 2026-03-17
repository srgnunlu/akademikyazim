"""Abstract base class for LLM providers."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class ToolCall:
    """Represents a tool call requested by the LLM."""

    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class ChatResponse:
    """Structured response from chat_with_tools."""

    text: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)
    finish_reason: str = "stop"
    raw: Any = None

    @property
    def has_tool_calls(self) -> bool:
        return len(self.tool_calls) > 0


class LLMProvider(ABC):
    """Base class for all LLM provider implementations."""

    def __init__(self, name: str, default_model: str):
        self.name = name
        self.default_model = default_model

    @staticmethod
    def validate_api_key(
        api_key: str, provider_name: str, *, allow_empty: bool = False
    ) -> str:
        """Validate and return API key. Raises ValueError if empty and not allowed."""
        if not api_key and not allow_empty:
            raise ValueError(
                f"API key required for provider '{provider_name}'. "
                f"Set the appropriate environment variable in .env"
            )
        if not api_key:
            logger.warning("No API key for provider '%s' — requests may fail", provider_name)
        return api_key

    @abstractmethod
    async def chat(
        self,
        messages: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> str:
        """Send messages and return response text.

        Args:
            messages: List of {"role": ..., "content": ...} dicts.
            model: Model override. Uses default_model if None.
            temperature: Sampling temperature.

        Returns:
            The assistant's response text.
        """

    async def chat_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> ChatResponse:
        """Send messages with tool definitions and return structured response.

        Args:
            messages: List of {"role": ..., "content": ...} dicts.
            tools: Tool definitions (OpenAI function-calling format).
            model: Model override.
            temperature: Sampling temperature.

        Returns:
            ChatResponse with text and/or tool_calls.
        """
        # Default implementation: fall back to plain chat (no tool support)
        text = await self.chat(messages, model, temperature)
        return ChatResponse(text=text)

    @abstractmethod
    async def health_check(self) -> dict:
        """Send a minimal prompt to verify connectivity.

        Returns:
            {"status": "ok"|"error", "provider": name, "model": ..., "detail": ...}
        """

    def resolve_model(self, model: str | None) -> str:
        return model or self.default_model
