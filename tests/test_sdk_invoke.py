"""Tests for SDK method listing (no live API calls)."""

from graphiant_cli.sdk_invoke import list_api_method_rows, list_api_methods


def test_list_api_methods_includes_auth_get() -> None:
    names = list_api_methods("v1_auth_")
    assert "v1_auth_get" in names
    assert "v1_auth_get_with_http_info" not in names


def test_list_api_methods_prefix_filter() -> None:
    edges = list_api_methods("v1_edges_summary")
    assert "v1_edges_summary_get" in edges


def test_list_api_method_rows_includes_raw_http() -> None:
    rows = {name: (verb, path) for name, verb, path in list_api_method_rows("v1_edges_summary")}
    assert rows["v1_edges_summary_get"] == ("GET", "/v1/edges-summary")
    assert rows["v1_edges_summary_post"][0] == "POST"
