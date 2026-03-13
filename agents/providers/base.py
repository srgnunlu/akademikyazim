"""Abstract base class for LLM providers."""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Base class for all LLM provider implementations."""

    def __init__(self, name: str, default_model: str):
        self.name = name
        self.default_model = default_model

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
