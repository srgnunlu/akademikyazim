# TezAtlas — Reproducible Development Environment
# Eliminates "works on my machine" friction, especially on Windows / university machines
#
# Usage:
#   docker build -t tezatlas .
#   docker run -it --rm -v $(pwd):/workspace tezatlas
#
# VS Code / GitHub Codespaces:
#   Open in Dev Container (uses .devcontainer/devcontainer.json)

FROM python:3.12-slim-bookworm

LABEL maintainer="TezAtlas"
LABEL description="TezAtlas academic workflow environment"

# ── System dependencies ────────────────────────────────────────────────────────

RUN apt-get update && apt-get install -y --no-install-recommends \
    # Tesseract OCR with Turkish + English language packs
    tesseract-ocr \
    tesseract-ocr-tur \
    tesseract-ocr-eng \
    # Tesseract legacy engine support
    tesseract-ocr-script-latn \
    # PDF utilities
    poppler-utils \
    # Git (for pre-commit hooks and session commits)
    git \
    # curl (for health checks)
    curl \
    # Build tools (for some Python packages)
    build-essential \
    # Terminal goodies (optional, for banner)
    figlet \
    && rm -rf /var/lib/apt/lists/*

# ── Python environment ─────────────────────────────────────────────────────────

WORKDIR /workspace

# Copy dependency files first (layer cache optimization)
COPY pyproject.toml ./
COPY README.md ./

# Install Python packages (all optional groups)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        pymupdf \
        pytesseract \
        pyyaml \
        python-dotenv \
        openai \
        anthropic \
        mcp \
        pre-commit

# ── Non-root user (VS Code devcontainer convention) ───────────────────────────

RUN useradd -ms /bin/bash vscode
RUN chown -R vscode:vscode /workspace
USER vscode

# ── Working directory ─────────────────────────────────────────────────────────

VOLUME ["/workspace"]

# ── Healthcheck ───────────────────────────────────────────────────────────────

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import pymupdf, pytesseract, yaml; print('OK')" || exit 1

# ── Entrypoint ────────────────────────────────────────────────────────────────

CMD ["bash", "-c", "figlet 'TezAtlas' 2>/dev/null || echo 'TezAtlas'; echo 'Environment ready. Run: python3 agents/run.py --list-providers'; bash"]
