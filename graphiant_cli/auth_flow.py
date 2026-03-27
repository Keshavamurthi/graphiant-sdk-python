"""Store bearer tokens after login."""

from __future__ import annotations

from graphiant_cli.config_store import set_profile


def login_with_token(
    host: str,
    token: str,
    *,
    profile: str = "default",
    email: str | None = None,
) -> None:
    """Persist JWT and refresh ~/.graphiant/env.sh."""
    set_profile(profile, host, token.strip(), email=email, expires_at=None)
