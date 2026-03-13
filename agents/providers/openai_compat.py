"""Generic OpenAI-compatible LLM provider.

Covers: OpenAI, Gemini, DeepSeek, Grok, Groq, Together, MiniMax, Ollama,
and any other provider exposing an OpenAI-compatible chat completions endpoint.
"""

from openai import AsyncOpenAI

from agents.providers.base import LLMProvider


class OpenAICompatProvider(LLMProvider):
    """Provider that works with any OpenAI-compatible API."""

    def __init__(
        self,
        name: str,
        base_url: str,
        api_key: str,
        default_model: str,
    ):
        super().__init__(name=name, default_model=default_model)
        self.base_url = base_url
        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=api_key or "not-needed",
        )

    async def chat(
        self,
        messages: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> str:
        resolved = self.resolve_model(model)
        response = await self.client.chat.completions.create(
            model=resolved,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content

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
