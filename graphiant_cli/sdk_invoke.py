"""Invoke DefaultApi methods by name with JSON arguments (CLI)."""

from __future__ import annotations

import inspect
import json
import re
import types
from functools import lru_cache
from pathlib import Path
from typing import Annotated, Any, Optional, Union, get_args, get_origin

from pydantic import BaseModel

from graphiant_cli.rest_client import strip_bearer_prefix
from graphiant_sdk import ApiClient, Configuration, DefaultApi

_ROUTE_FROM_SERIALIZE = re.compile(
    r"def _(v[0-9]+_[a-z0-9_]+)_serialize\("
    r"[\s\S]*?"
    r"return self\.api_client\.param_serialize\(\s*"
    r"method='([A-Z]+)',\s*"
    r"resource_path='([^']+)'",
    re.MULTILINE,
)


@lru_cache(maxsize=1)
def _default_api_route_index() -> dict[str, tuple[str, str]]:
    """Map DefaultApi operation name → (HTTP verb, path) from generated client source."""
    import graphiant_sdk.api.default_api as mod

    text = Path(mod.__file__).read_text(encoding="utf-8")
    return {m: (verb, path) for m, verb, path in _ROUTE_FROM_SERIALIZE.findall(text)}


def list_api_methods(prefix: str = "") -> list[str]:
    """List callable DefaultApi operation methods (excludes *_with_http_info, etc.)."""
    out: list[str] = []
    for name in sorted(dir(DefaultApi)):
        if name.startswith("_"):
            continue
        attr = getattr(DefaultApi, name, None)
        if not callable(attr):
            continue
        if name.endswith("_with_http_info") or name.endswith("_without_preload_content"):
            continue
        if prefix and not name.startswith(prefix):
            continue
        out.append(name)
    return out


def list_api_method_rows(prefix: str = "") -> list[tuple[str, str, str]]:
    """(sdk_method_name, http_verb, path) for each operation, sorted by method name."""
    routes = _default_api_route_index()
    rows: list[tuple[str, str, str]] = []
    for name in list_api_methods(prefix):
        verb, path = routes.get(name, ("—", "—"))
        rows.append((name, verb, path))
    return rows


def _unwrap_annotated(annotation: Any) -> Any:
    if annotation is None or annotation is inspect.Parameter.empty:
        return annotation
    origin = get_origin(annotation)
    if origin is Annotated:
        args = get_args(annotation)
        if args:
            return args[0]
    return annotation


def _is_union_origin(origin: Any) -> bool:
    if origin is Union:
        return True
    ut = getattr(types, "UnionType", None)
    return ut is not None and origin is ut


def _coerce_value(value: Any, annotation: Any) -> Any:
    if annotation is None or annotation is inspect.Parameter.empty:
        return value
    inner = _unwrap_annotated(annotation)
    origin = get_origin(inner)
    args = get_args(inner)

    if _is_union_origin(origin):
        non_none = [a for a in args if a is not type(None)]
        if value is None:
            return None
        if len(non_none) == 1:
            return _coerce_value(value, non_none[0])
        return value

    if origin is list:
        if not isinstance(value, list) or len(args) != 1:
            return value
        elt_ann = _unwrap_annotated(args[0])
        elt_origin = get_origin(elt_ann)
        elt_args = get_args(elt_ann)
        if _is_union_origin(elt_origin):
            nn = [a for a in elt_args if a is not type(None)]
            if len(nn) == 1:
                elt_ann = nn[0]
        if isinstance(elt_ann, type) and issubclass(elt_ann, BaseModel):
            return [
                elt_ann.model_validate(item) if isinstance(item, dict) else item
                for item in value
            ]
        return value

    if isinstance(value, dict) and isinstance(inner, type) and issubclass(inner, BaseModel):
        return inner.model_validate(value)
    return value


def invoke_method(
    host: str,
    token: str,
    method_name: str,
    args_json: Optional[str],
    kwargs_json: Optional[str],
) -> Any:
    cfg = Configuration(host=host)
    # Do not set api_key["jwtAuth"]: operations already send Authorization from the
    # `authorization` argument. jwtAuth would add a second header (lowercase key
    # "authorization"), which Azure Application Gateway rejects with 400.

    with ApiClient(cfg) as client:
        api = DefaultApi(client)
        if not hasattr(api, method_name):
            raise AttributeError(
                f"Unknown DefaultApi method {method_name!r}. Try: graphiant api list --prefix v1_"
            )
        method = getattr(api, method_name)
        sig = inspect.signature(method)
        public = [p for p in sig.parameters.values() if not p.name.startswith("_")]

        raw_args: list[Any] = json.loads(args_json) if args_json else []
        merged: dict[str, Any] = json.loads(kwargs_json) if kwargs_json else {}

        ai = 0
        for p in public:
            if p.name in merged:
                continue
            if ai < len(raw_args):
                merged[p.name] = raw_args[ai]
                ai += 1
                continue
            if p.name == "authorization":
                merged["authorization"] = f"Bearer {strip_bearer_prefix(token)}"

        for name, param in sig.parameters.items():
            if name.startswith("_"):
                continue
            if name not in merged:
                continue
            merged[name] = _coerce_value(merged[name], param.annotation)

        call_kw = {k: v for k, v in merged.items() if k in sig.parameters}
        return method(**call_kw)
