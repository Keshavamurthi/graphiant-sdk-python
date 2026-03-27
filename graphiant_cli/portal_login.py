"""Portal URL helpers, open browser, and re-exports for tests and ``main``."""

from __future__ import annotations

import webbrowser

from graphiant_cli.browser_capture import PLAYWRIGHT_AVAILABLE, capture_token_via_browser
from graphiant_cli.cli_logging import get_logger
from graphiant_cli.config_store import DEFAULT_PORTAL_URL, load_config
from graphiant_cli.token_parsing import (
    eligible_capture as _eligible_capture,
    extract_token_from_graphiant_api_response,
    extract_token_from_paste,
    extract_token_from_refresh_json,
    extract_token_from_refresh_response,
    extract_token_from_url,
    is_auth_refresh_url as _is_auth_refresh_url,
    is_graphiant_api_url as _is_graphiant_api_url,
    is_plausible_access_token as _is_plausible_access_token,
    portal_root_url,
    url_ignored_for_bearer_capture as _url_ignored_for_bearer_capture,
)

logger = get_logger("portal_login")


def portal_url_from_config() -> str:
    cfg = load_config()
    return (cfg.get("portal_url") or DEFAULT_PORTAL_URL).rstrip("/") + "/"


def effective_portal_url(cli_override: str | None) -> str:
    if cli_override:
        return cli_override.rstrip("/") + "/"
    return portal_url_from_config()


def open_portal(portal_url: str) -> None:
    try:
        webbrowser.open(portal_url)
    except Exception as e:
        logger.warning("webbrowser.open failed: %s", e)


__all__ = [
    "PLAYWRIGHT_AVAILABLE",
    "_eligible_capture",
    "_is_auth_refresh_url",
    "_is_graphiant_api_url",
    "_is_plausible_access_token",
    "_url_ignored_for_bearer_capture",
    "capture_token_via_browser",
    "effective_portal_url",
    "extract_token_from_graphiant_api_response",
    "extract_token_from_paste",
    "extract_token_from_refresh_json",
    "extract_token_from_refresh_response",
    "extract_token_from_url",
    "open_portal",
    "portal_root_url",
    "portal_url_from_config",
]
