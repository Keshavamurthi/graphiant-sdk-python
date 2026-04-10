"""Raw REST calls against the Graphiant API (Bearer token)."""

from __future__ import annotations

import json
import urllib.parse
from collections.abc import Sequence
from typing import Any

import urllib3

# Query values: str/int or repeated keys (e.g. enterpriseIds) as a sequence.
QueryDict = dict[str, str | int | Sequence[str | int]]


def strip_bearer_prefix(token: str) -> str:
    """Return the JWT/opaque secret without a leading ``Bearer `` prefix (case-insensitive)."""
    t = (token or "").strip()
    if t.lower().startswith("bearer "):
        return t[7:].strip()
    return t


def _encode_query(query: QueryDict) -> str:
    pairs: list[tuple[str, str]] = []
    for key, val in query.items():
        if isinstance(val, (list, tuple)):
            for item in val:
                pairs.append((key, str(item)))
        else:
            pairs.append((key, str(val)))
    return urllib.parse.urlencode(pairs)


def request(
    host: str,
    method: str,
    path: str,
    token: str,
    body: dict[str, Any] | str | None = None,
    query: QueryDict | None = None,
    timeout: float = 120.0,
) -> tuple[int, str, dict[str, str]]:
    """Return (status_code, response_text, response_headers)."""
    base = host.rstrip("/")
    p = path if path.startswith("/") else f"/{path}"
    url = base + p
    if query:
        url = f"{url}?{_encode_query(query)}"

    http = urllib3.PoolManager()
    raw = strip_bearer_prefix(token)
    headers = {
        "Authorization": f"Bearer {raw}",
        "Accept": "application/json",
    }
    body_bytes: bytes | None = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        if isinstance(body, str):
            body_bytes = body.encode("utf-8")
        else:
            body_bytes = json.dumps(body).encode("utf-8")

    r = http.request(
        method.upper(),
        url,
        body=body_bytes,
        headers=headers,
        timeout=urllib3.Timeout(total=timeout),
    )
    text = r.data.decode("utf-8", errors="replace")
    return int(r.status), text, dict(r.headers)
