"""CLI logging: stderr, no secrets (never log bearer tokens or raw JWTs)."""

from __future__ import annotations

import logging
import os
import sys
from typing import Final

_PARENT: Final = "graphiant_cli"


def get_logger(component: str) -> logging.Logger:
    """Child logger under ``graphiant_cli`` (e.g. ``portal_login``, ``login``)."""
    return logging.getLogger(f"{_PARENT}.{component}")


def configure_logging(*, verbose: bool = False) -> None:
    """
    Configure the ``graphiant_cli`` logger once. Levels:

    * ``--verbose`` / ``-v`` → DEBUG
    * ``GRAPHIANT_LOG=debug|info|warning`` (overrides default when not verbose)
    * otherwise → WARNING (errors and warnings only)
    """
    log = logging.getLogger(_PARENT)
    env = os.environ.get("GRAPHIANT_LOG", "").strip().lower()
    if verbose:
        level = logging.DEBUG
    elif env in ("debug", "1", "true", "yes"):
        level = logging.DEBUG
    elif env in ("info",):
        level = logging.INFO
    elif env in ("warning", "warn"):
        level = logging.WARNING
    else:
        level = logging.WARNING
    log.setLevel(level)

    if log.handlers:
        return

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        logging.Formatter("%(levelname)s [%(name)s] %(message)s")
    )
    log.addHandler(handler)
    log.propagate = False


def ensure_cli_logging() -> None:
    """Attach stderr logging if nothing configured yet (e.g. capture called in isolation)."""
    log = logging.getLogger(_PARENT)
    if not log.handlers:
        configure_logging(verbose=False)


def safe_api_url_for_log(url: str, max_len: int = 120) -> str:
    """Truncate URL for logs; strips query string to reduce accidental sensitive data."""
    try:
        from urllib.parse import urlparse, urlunparse

        p = urlparse(url)
        safe = urlunparse((p.scheme, p.netloc, p.path, "", "", ""))
        if len(safe) > max_len:
            return safe[: max_len - 3] + "..."
        return safe or url[:max_len]
    except Exception:
        return (url[: max_len - 3] + "...") if len(url) > max_len else url
