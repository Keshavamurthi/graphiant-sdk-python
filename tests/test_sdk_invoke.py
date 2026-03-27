"""Tests for SDK method listing (no live API calls)."""

from graphiant_cli.sdk_invoke import list_api_methods


def test_list_api_methods_includes_auth_get() -> None:
    names = list_api_methods("v1_auth_")
    assert "v1_auth_get" in names
    assert "v1_auth_get_with_http_info" not in names


def test_list_api_methods_prefix_filter() -> None:
    edges = list_api_methods("v1_edges_summary")
    assert "v1_edges_summary_get" in edges
