"""Shared login flows: persist credentials and print post-login instructions."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from graphiant_cli.auth_flow import login_with_token
from graphiant_cli.config_store import ENV_EXPORT_FILE, format_env_export_line
from rich.console import Console


CREDENTIALS_WRITE_ERRORS = (OSError, PermissionError, json.JSONDecodeError, TypeError)


def try_persist_login(
    host: str,
    token: str,
    profile: str,
    *,
    console: Console,
    logger: object,
) -> bool:
    """Persist token; print error and return False on filesystem/JSON failures."""
    try:
        login_with_token(host, token, profile=profile)
        return True
    except CREDENTIALS_WRITE_ERRORS as e:
        logger.exception("Failed to save credentials: %s", e)
        console.print(
            f"[red]Could not write credentials or env file:[/red] {e}\n"
            f"  Check permissions on [cyan]~/.graphiant/[/cyan] (or GRAPHIANT_CONFIG_DIR)."
        )
        return False


def print_login_success(
    console: Console,
    *,
    export_shell: bool,
    env_file: Path | None = None,
    verbose: bool = False,
) -> None:
    """Post-login instructions. Default is short; ``verbose`` adds child-process and stdout details."""
    env_path = str(env_file or ENV_EXPORT_FILE)
    console.print("\n[bold green]Login saved.[/bold green]")
    console.print(f"Run [cyan]source {env_path}[/cyan] in this terminal to set [bold]GRAPHIANT_ACCESS_TOKEN[/bold].")
    if verbose:
        console.print(
            "[dim]Why: a child process cannot change your shell’s environment; the token is in the file above.[/dim]"
        )
        console.print(
            f"[dim]Alternative (no browser): [cyan]eval \"$(graphiant login env-export)\"[/cyan][/dim]"
        )
        if export_shell:
            console.print(
                "[dim]An [cyan]export GRAPHIANT_ACCESS_TOKEN=…[/cyan] line was also sent to **stdout** for scripts.[/dim]"
            )
        console.print(f"[dim]Credentials file:[/dim] [cyan]{env_path}[/cyan]")


def write_export_line_to_stdout(token: str) -> None:
    """Emit POSIX export line for ``eval`` / scripts (stdout)."""
    print(format_env_export_line(token), file=sys.stdout)
