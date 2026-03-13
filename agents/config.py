"""Configuration loader and provider factory.

Reads agents.yaml + .env, instantiates the correct LLMProvider per agent.
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

from agents.providers.base import LLMProvider
from agents.providers.openai_compat import OpenAICompatProvider
from agents.providers.anthropic import AnthropicProvider

# Resolve paths relative to the project root (parent of agents/)
_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_CONFIG = _ROOT / "agents.yaml"
_DEFAULT_ENV = _ROOT / ".env"


def _load_env(env_path: Path = _DEFAULT_ENV) -> None:
    if env_path.exists():
        load_dotenv(env_path)


def load_config(config_path: Path = _DEFAULT_CONFIG) -> dict:
    """Load and return the agents.yaml configuration."""
    _load_env()
    with open(config_path) as f:
        return yaml.safe_load(f)


def _build_provider(name: str, provider_cfg: dict) -> LLMProvider:
    """Instantiate a single LLMProvider from its config block."""
    is_anthropic = provider_cfg.get("type") == "anthropic"

    # Resolve API key from environment variable name
    api_key_env = provider_cfg.get("api_key_env", "")
    if api_key_env and api_key_env.lower() != "none":
        api_key = os.environ.get(api_key_env, "")
    else:
        api_key = ""

    default_model = provider_cfg.get("default_model", "")

    if is_anthropic:
        return AnthropicProvider(
            name=name,
            api_key=api_key,
            default_model=default_model,
        )

    return OpenAICompatProvider(
        name=name,
        base_url=provider_cfg.get("base_url", ""),
        api_key=api_key,
        default_model=default_model,
    )


class AgentConfig:
    """Holds the full agent configuration and provides provider instances."""

    def __init__(self, config_path: Path = _DEFAULT_CONFIG):
        self.raw = load_config(config_path)
        self.providers_cfg: dict = self.raw.get("providers", {})
        self.agents_cfg: dict = self.raw.get("agents", {})
        self.defaults: dict = self.raw.get("defaults", {})
        self._providers: dict[str, LLMProvider] = {}

    def get_provider(self, provider_name: str) -> LLMProvider:
        """Get or create a cached provider instance by name."""
        if provider_name not in self._providers:
            cfg = self.providers_cfg.get(provider_name)
            if cfg is None:
                raise ValueError(f"Unknown provider: {provider_name}")
            self._providers[provider_name] = _build_provider(provider_name, cfg)
        return self._providers[provider_name]

    def get_agent_provider(self, agent_name: str) -> tuple[LLMProvider, str | None]:
        """Return (provider, model_override) for a given agent.

        Falls back to defaults.fallback_provider if the agent's provider
        is not configured.
        """
        agent_cfg = self.agents_cfg.get(agent_name)
        if agent_cfg is None:
            raise ValueError(f"Unknown agent: {agent_name}")

        provider_name = agent_cfg.get("provider")
        model_override = agent_cfg.get("model")  # None means use default

        try:
            provider = self.get_provider(provider_name)
        except (ValueError, Exception):
            fallback = self.defaults.get("fallback_provider")
            if fallback and fallback != provider_name:
                provider = self.get_provider(fallback)
                model_override = None  # reset model when falling back
            else:
                raise

        return provider, model_override

    def list_providers(self) -> list[dict]:
        """Return a summary of all configured providers."""
        result = []
        for name, cfg in self.providers_cfg.items():
            api_key_env = cfg.get("api_key_env", "")
            has_key = bool(
                api_key_env
                and api_key_env.lower() != "none"
                and os.environ.get(api_key_env)
            )
            result.append({
                "name": name,
                "type": cfg.get("type", "openai-compatible"),
                "base_url": cfg.get("base_url", "N/A (Anthropic SDK)"),
                "default_model": cfg.get("default_model", ""),
                "api_key_env": api_key_env,
                "api_key_set": has_key,
            })
        return result

    def list_agents(self) -> list[dict]:
        """Return a summary of all configured agents."""
        result = []
        for name, cfg in self.agents_cfg.items():
            result.append({
                "name": name,
                "provider": cfg.get("provider", ""),
                "model": cfg.get("model", "(default)"),
                "description": cfg.get("description", ""),
            })
        return result
