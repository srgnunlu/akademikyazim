"""Anthropic-specific LLM provider.

Uses the Anthropic SDK (different message format from OpenAI).
Only needed when users want to call Claude API directly outside Claude Code.
"""

import logging

from anthropic import AsyncAnthropic

from agents.providers.base import ChatResponse, LLMProvider, ToolCall

logger = logging.getLogger(__name__)


class AnthropicProvider(LLMProvider):
    """Provider for Anthropic's Claude models."""

    def __init__(self, name: str, api_key: str, default_model: str):
        super().__init__(name=name, default_model=default_model)
        self.validate_api_key(api_key, name, allow_empty=False)
        self.client = AsyncAnthropic(api_key=api_key, timeout=120.0)

    def _split_system(self, messages: list[dict]) -> tuple[str | None, list[dict]]:
        """Separate system message from conversation messages."""
        system_text = None
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_text = msg["content"]
            else:
                chat_messages.append(msg)
        return system_text, chat_messages

    async def chat(
        self,
        messages: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> str:
        resolved = self.resolve_model(model)
        system_text, chat_messages = self._split_system(messages)

        kwargs: dict = {
            "model": resolved,
            "max_tokens": 8192,
            "messages": chat_messages,
            "temperature": temperature,
        }
        if system_text:
            kwargs["system"] = system_text

        try:
            response = await self.client.messages.create(**kwargs)
        except Exception as exc:
            logger.error(
                "API call failed for provider '%s' model '%s': %s",
                self.name, resolved, exc,
            )
            raise
        return response.content[0].text

    async def chat_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
        model: str | None = None,
        temperature: float = 0.3,
    ) -> ChatResponse:
        """Send messages with tool definitions (Anthropic tool_use format)."""
        resolved = self.resolve_model(model)
        system_text, chat_messages = self._split_system(messages)

        # Convert OpenAI tool format to Anthropic format if needed
        anthropic_tools = []
        for tool in tools:
            if "function" in tool:
                # OpenAI format → Anthropic format
                func = tool["function"]
                anthropic_tools.append({
                    "name": func["name"],
                    "description": func.get("description", ""),
                    "input_schema": func.get("parameters", {"type": "object", "properties": {}}),
                })
            else:
                # Already Anthropic format
                anthropic_tools.append(tool)

        kwargs: dict = {
            "model": resolved,
            "max_tokens": 8192,
            "messages": chat_messages,
            "tools": anthropic_tools,
            "temperature": temperature,
        }
        if system_text:
            kwargs["system"] = system_text

        try:
            response = await self.client.messages.create(**kwargs)
        except Exception as exc:
            logger.error(
                "Tool-calling failed for provider '%s' model '%s': %s",
                self.name, resolved, exc,
            )
            raise

        # Parse response blocks
        text_parts = []
        tool_calls = []
        for block in response.content:
            if block.type == "text":
                text_parts.append(block.text)
            elif block.type == "tool_use":
                tool_calls.append(ToolCall(
                    id=block.id,
                    name=block.name,
                    arguments=block.input if isinstance(block.input, dict) else {},
                ))

        return ChatResponse(
            text="\n".join(text_parts),
            tool_calls=tool_calls,
            finish_reason=response.stop_reason or "end_turn",
            raw=response,
        )

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
