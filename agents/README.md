# TezAtlas Multi-Agent System

A hybrid multi-agent orchestration layer for TezAtlas. Claude Code remains the primary orchestrator; this Python bridge enables external LLM calls for specialized tasks.

## Architecture

Any **OpenAI-compatible** LLM provider works out of the box (Gemini, DeepSeek, Grok, Groq, Ollama, Together, MiniMax, OpenAI, etc.). Anthropic uses a separate SDK path.

```
agents/
├── config.py              ← Load .env + agents.yaml
├── providers/
│   ├── base.py            ← Abstract LLMProvider
│   ├── openai_compat.py   ← Generic provider (covers 90% of LLMs)
│   └── anthropic.py       ← Anthropic-specific provider
├── core/
│   ├── source_hunter.py
│   ├── methodology_checker.py
│   └── citation_verifier.py
├── prompts/               ← System prompts (markdown)
└── run.py                 ← CLI entry point
```

## Setup

1. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   cp .env.example .env
   ```

2. Install dependencies:
   ```bash
   pip install openai anthropic pyyaml python-dotenv pymupdf
   ```

3. Edit `agents.yaml` to assign providers to agents.

## Usage

### List configured providers
```bash
python agents/run.py --list-providers
```

### Health check all providers
```bash
python agents/run.py --test-providers
```

### Source Hunter
```bash
python agents/run.py source_hunter \
  --research-question "Merkez bankası dijital paralarının para politikasına etkisi" \
  --field economics \
  --existing-sources sources/ \
  --language both
```

### Methodology Checker
```bash
python agents/run.py methodology_checker \
  --input methodology_section.md \
  --research-question "Impact of CBDCs on monetary policy" \
  --field economics \
  --document-type thesis
```

### Citation Verifier
```bash
python agents/run.py citation_verifier \
  --claim "CBDC adoption reduces cash usage by 40% (BIS, 2023)" \
  --source sources/BIS_2023_CBDC_Report.pdf
```

## Adding a New Provider

Add a block to `agents.yaml` under `providers:`:

```yaml
providers:
  my_provider:
    base_url: "https://api.example.com/v1"
    api_key_env: "MY_PROVIDER_API_KEY"
    default_model: "my-model-name"
```

Then set the env var in `.env` and assign agents to it.

## Agents

| Agent | Purpose | Default Provider |
|-------|---------|-----------------|
| `source_hunter` | Discover and recommend academic sources | Gemini |
| `methodology_checker` | Validate methodological consistency | Gemini |
| `citation_verifier` | Cross-check citations against source PDFs | DeepSeek |

## Claude Code Integration

During a TezAtlas session, Claude Code calls these agents via `python agents/run.py ...` in the background using the Bash tool, then integrates findings into the conversation.
