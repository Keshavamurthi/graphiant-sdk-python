"""Tests for CLI logging helpers."""

from graphiant_cli.cli_logging import safe_api_url_for_log


def test_safe_api_url_for_log_strips_query() -> None:
    u = "https://api.example.com/v1/foo?bar=token&x=1"
    s = safe_api_url_for_log(u)
    assert "?" not in s
    assert "/v1/foo" in s


def test_safe_api_url_for_log_truncates() -> None:
    long_path = "https://x/v1/" + ("a" * 200)
    s = safe_api_url_for_log(long_path, max_len=40)
    assert len(s) <= 40
    assert s.endswith("...")
