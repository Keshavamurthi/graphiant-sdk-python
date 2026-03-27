"""Tests for config_store helpers."""

from graphiant_cli.config_store import format_env_export_line


def test_format_env_export_line_quoting() -> None:
    assert format_env_export_line("gr-auth-abc") == "export GRAPHIANT_ACCESS_TOKEN='gr-auth-abc'"
    assert format_env_export_line("a'b") == "export GRAPHIANT_ACCESS_TOKEN='a'\"'\"'b'"
