# TezAtlas MCP Server — Academic APIs

Semantic Scholar, OpenAlex, and CrossRef via MCP tools — usable directly from Claude Code.

## Installation

```bash
pip install mcp
```

## Configure in Claude Code

Add to `~/.claude/mcp.json` (or the project-level `.claude/mcp.json`):

```json
{
  "mcpServers": {
    "tezatlas-academic": {
      "command": "python3",
      "args": ["/absolute/path/to/TezAtlas/mcp_server/server.py"],
      "env": {
        "S2_API_KEY": "your-semantic-scholar-key-optional"
      }
    }
  }
}
```

Semantic Scholar API key is optional but raises rate limit from 100 req/5min to 1 req/sec.
Get one free at: https://www.semanticscholar.org/product/api

## Available Tools

| Tool | Description |
|------|-------------|
| `search_papers` | Search across S2 + OpenAlex + CrossRef |
| `get_paper_details` | Full metadata for a DOI or S2 paper ID |
| `get_citations` | Papers citing a given paper (forward snowball) |
| `get_references` | Papers cited by a given paper (backward snowball) |
| `doi_to_bibtex` | Convert DOI → BibTeX entry |
| `search_authors` | Find researcher profiles (affiliation, h-index) |
| `get_related_papers` | Full citation graph expansion (both directions) |

## Test without MCP (CLI mode)

```bash
# Search papers
python3 mcp_server/server.py search "merkez bankası dijital para CBDC"

# Get BibTeX for a DOI
python3 mcp_server/server.py bibtex 10.1016/j.jmoneco.2021.09.001

# Get paper details
python3 mcp_server/server.py paper DOI:10.1234/example

# Snowball sampling — get all references and citations
python3 mcp_server/server.py references <paper_id>
python3 mcp_server/server.py citations <paper_id>

# Author search
python3 mcp_server/server.py author "Daron Acemoglu"
```

## TezAtlas Integration

During a TezAtlas session, Claude Code can call these tools directly:

- **Phase 2 (Source Discovery):** `search_papers` to find initial sources
- **Phase 3 (Snowball Sampling):** `get_references` + `get_citations` per source
- **Citation Management:** `doi_to_bibtex` to generate `.bib` entries
- **Author Research:** `search_authors` to verify credentials and find more work

## API Rate Limits

| API | Limit | Notes |
|-----|-------|-------|
| Semantic Scholar | 100 req/5min (unauthenticated) | Use S2_API_KEY for 1 req/sec |
| OpenAlex | 10 req/sec | Free, no key needed |
| CrossRef | Polite pool (no limit stated) | Uses `mailto` header |
