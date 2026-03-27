"""Invoke DefaultApi methods by name with JSON arguments (CLI)."""

from __future__ import annotations

import inspect
import json
from typing import Annotated, Any, Optional, get_args, get_origin

from pydantic import BaseModel

from graphiant_sdk import ApiClient, Configuration, DefaultApi


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


def _unwrap_annotated(annotation: Any) -> Any:
    if annotation is None or annotation is inspect.Parameter.empty:
        return annotation
    origin = get_origin(annotation)
    if origin is Annotated:
        args = get_args(annotation)
        if args:
            return args[0]
    return annotation


def _coerce_value(value: Any, annotation: Any) -> Any:
    if annotation is None or annotation is inspect.Parameter.empty:
        return value
    inner = _unwrap_annotated(annotation)
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
    cfg.api_key["jwtAuth"] = token
    cfg.api_key_prefix["jwtAuth"] = "Bearer"

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
                merged["authorization"] = f"Bearer {token}"

        for name, param in sig.parameters.items():
            if name.startswith("_"):
                continue
            if name not in merged:
                continue
            merged[name] = _coerce_value(merged[name], param.annotation)

        call_kw = {k: v for k, v in merged.items() if k in sig.parameters}
        return method(**call_kw)
