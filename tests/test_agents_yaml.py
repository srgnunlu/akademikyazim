"""
test_agents_yaml.py — Validate agents.yaml configuration schema.

Replaces the inline Python validation from CI.
"""

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
AGENTS_YAML = REPO_ROOT / "agents.yaml"

VALID_PROVIDER_TYPES = {"openai-compatible", "anthropic"}


@pytest.fixture(scope="module")
def config():
    with open(AGENTS_YAML) as f:
        return yaml.safe_load(f)


class TestAgentsYamlSchema:
    def test_file_exists(self):
        assert AGENTS_YAML.exists(), "agents.yaml not found"

    def test_has_required_sections(self, config):
        assert "providers" in config, "Missing providers section"
        assert "agents" in config, "Missing agents section"
        assert "defaults" in config, "Missing defaults section"

    def test_all_agents_have_provider(self, config):
        for name, agent_cfg in config["agents"].items():
            assert "provider" in agent_cfg, f"Agent '{name}' missing provider"

    def test_all_agent_providers_exist(self, config):
        provider_names = set(config["providers"].keys())
        for name, agent_cfg in config["agents"].items():
            provider = agent_cfg["provider"]
            assert provider in provider_names, (
                f"Agent '{name}' references unknown provider '{provider}'"
            )

    def test_provider_types_valid(self, config):
        for name, pcfg in config["providers"].items():
            ptype = pcfg.get("type", "openai-compatible")
            assert ptype in VALID_PROVIDER_TYPES, (
                f"Provider '{name}' has invalid type '{ptype}'"
            )

    def test_providers_have_default_model(self, config):
        for name, pcfg in config["providers"].items():
            assert pcfg.get("default_model"), (
                f"Provider '{name}' missing default_model"
            )
