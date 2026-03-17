"""Shared logging configuration for TezAtlas.

Usage:
    from core.log import get_logger
    logger = get_logger(__name__)
    logger.info("Processing %s", filename)
"""

from __future__ import annotations

import logging
import os
import sys

_CONFIGURED = False


def get_logger(name: str) -> logging.Logger:
    """Return a logger with the TezAtlas standard configuration.

    Log level is controlled by TEZATLAS_LOG_LEVEL env var (default: INFO).
    Output goes to stderr so it does not interfere with JSON/CLI output.
    """
    global _CONFIGURED
    if not _CONFIGURED:
        level_name = os.environ.get("TEZATLAS_LOG_LEVEL", "INFO").upper()
        level = getattr(logging, level_name, logging.INFO)
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        )
        root = logging.getLogger("tezatlas")
        root.setLevel(level)
        root.addHandler(handler)
        _CONFIGURED = True

    return logging.getLogger(name)
