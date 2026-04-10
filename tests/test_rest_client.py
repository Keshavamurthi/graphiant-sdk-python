"""Tests for graphiant_cli.rest_client helpers."""

from graphiant_cli.rest_client import strip_bearer_prefix


def test_strip_bearer_prefix_plain() -> None:
    assert strip_bearer_prefix("opaque-token") == "opaque-token"


def test_strip_bearer_prefix_removes_prefix() -> None:
    assert strip_bearer_prefix("Bearer jwt-here") == "jwt-here"
    assert strip_bearer_prefix("bearer jwt-here") == "jwt-here"


def test_strip_bearer_prefix_empty() -> None:
    assert strip_bearer_prefix("") == ""
