"""Abstract base class for LLM providers."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


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

    @abstractmethod
    async def health_check(self) -> dict:
        """Send a minimal prompt to verify connectivity.

        Returns:
            {"status": "ok"|"error", "provider": name, "model": ..., "detail": ...}
        """

    def resolve_model(self, model: str | None) -> str:
        return model or self.default_model
