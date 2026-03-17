"""Generic OpenAI-compatible LLM provider.

Covers: OpenAI, Gemini, DeepSeek, Grok, Groq, Together, MiniMax, Ollama,
and any other provider exposing an OpenAI-compatible chat completions endpoint.
"""

import logging

from openai import AsyncOpenAI

from agents.providers.base import LLMProvider

logger = logging.getLogger(__name__)

_LOCAL_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "host.docker.internal")


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

        # Local providers (e.g. Ollama) don't need an API key
        is_local = any(host in (base_url or "") for host in _LOCAL_HOSTS)
        validated_key = self.validate_api_key(
            api_key, name, allow_empty=is_local
        )

        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=validated_key or "not-needed",
            timeout=30.0,
        )

    async def chat(
        self,
        messages: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> str:
        resolved = self.resolve_model(model)
        try:
            response = await self.client.chat.completions.create(
                model=resolved,
                messages=messages,
                temperature=temperature,
            )
        except Exception as exc:
            logger.error(
                "API call failed for provider '%s' model '%s': %s",
                self.name, resolved, exc,
            )
            raise
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
