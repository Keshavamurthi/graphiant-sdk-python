"""Credentials and CLI config under ~/.graphiant/."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

DEFAULT_PROFILE = "default"
DEFAULT_PORTAL_URL = "https://portal.graphiant.com/"
CONFIG_DIR = Path(os.environ.get("GRAPHIANT_CONFIG_DIR", Path.home() / ".graphiant"))
CREDENTIALS_FILE = CONFIG_DIR / "credentials.json"
CONFIG_FILE = CONFIG_DIR / "config.json"
ENV_EXPORT_FILE = CONFIG_DIR / "env.sh"


def shell_single_quote(value: str) -> str:
    return "'" + value.replace("'", "'\"'\"'") + "'"


def format_env_export_line(token: str) -> str:
    """Single POSIX line for ``eval`` in bash/zsh: ``export GRAPHIANT_ACCESS_TOKEN='…'``."""
    return f"export GRAPHIANT_ACCESS_TOKEN={shell_single_quote(token)}"


def write_access_token_env(token: str | None) -> None:
    """Write ~/.graphiant/env.sh with export GRAPHIANT_ACCESS_TOKEN=..."""
    _ensure_dir()
    if not token:
        content = (
            "# graphiant: no active token. Run: graphiant login\n"
        )
    else:
        content = (
            "# Source: source ~/.graphiant/env.sh\n"
            f"{format_env_export_line(token)}\n"
        )
    ENV_EXPORT_FILE.write_text(content, encoding="utf-8")
    os.chmod(ENV_EXPORT_FILE, 0o600)


def _ensure_dir() -> None:
    CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)


def load_credentials() -> dict[str, Any]:
    if not CREDENTIALS_FILE.is_file():
        return {"profiles": {}}
    with open(CREDENTIALS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_credentials(data: dict[str, Any]) -> None:
    _ensure_dir()
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.chmod(CREDENTIALS_FILE, 0o600)


def get_profile(name: str | None = None) -> dict[str, Any] | None:
    profile = name or os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE)
    creds = load_credentials()
    return creds.get("profiles", {}).get(profile)


def set_profile(
    name: str,
    host: str,
    access_token: str,
    email: str | None = None,
    expires_at: float | None = None,
) -> None:
    creds = load_credentials()
    creds.setdefault("profiles", {})
    creds["profiles"][name] = {
        "host": host.rstrip("/"),
        "access_token": access_token,
        "email": email,
        "expires_at": expires_at,
    }
    save_credentials(creds)
    write_access_token_env(access_token)


def clear_profile(name: str | None = None) -> None:
    profile = name or os.environ.get("GRAPHIANT_PROFILE", DEFAULT_PROFILE)
    creds = load_credentials()
    if profile in creds.get("profiles", {}):
        del creds["profiles"][profile]
        save_credentials(creds)
    creds_after = load_credentials()
    default_prof = creds_after.get("profiles", {}).get(DEFAULT_PROFILE)
    write_access_token_env(
        default_prof.get("access_token") if default_prof else None
    )


def load_config() -> dict[str, Any]:
    if not CONFIG_FILE.is_file():
        return {}
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_config(data: dict[str, Any]) -> None:
    _ensure_dir()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.chmod(CONFIG_FILE, 0o600)
