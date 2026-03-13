"""Anthropic-specific LLM provider.

Uses the Anthropic SDK (different message format from OpenAI).
Only needed when users want to call Claude API directly outside Claude Code.
"""

from anthropic import AsyncAnthropic

from agents.providers.base import LLMProvider


class AnthropicProvider(LLMProvider):
    """Provider for Anthropic's Claude models."""

    def __init__(self, name: str, api_key: str, default_model: str):
        super().__init__(name=name, default_model=default_model)
        self.client = AsyncAnthropic(api_key=api_key)

    async def chat(
        self,
        messages: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> str:
        resolved = self.resolve_model(model)

        # Separate system message from conversation messages.
        system_text = None
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_text = msg["content"]
            else:
                chat_messages.append(msg)

        kwargs: dict = {
            "model": resolved,
            "max_tokens": 4096,
            "messages": chat_messages,
            "temperature": temperature,
        }
        if system_text:
            kwargs["system"] = system_text

        response = await self.client.messages.create(**kwargs)
        return response.content[0].text

    async def health_check(self) -> dict:
        model = self.default_model
        try:
            result = await self.chat(
                messages=[{"role": "user", "content": "Reply with OK"}],
                model=model,
                temperature=0,
            )
            return {
                "status": "ok",
                "provider": self.name,
                "model": model,
                "detail": result[:100],
            }
        except Exception as exc:
            return {
                "status": "error",
                "provider": self.name,
                "model": model,
                "detail": str(exc)[:200],
            }
