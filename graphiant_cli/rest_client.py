"""Raw REST calls against the Graphiant API (Bearer token)."""

from __future__ import annotations

import json
import urllib.parse
from typing import Any

import urllib3


def request(
    host: str,
    method: str,
    path: str,
    token: str,
    body: dict[str, Any] | str | None = None,
    query: dict[str, str] | None = None,
    timeout: float = 120.0,
) -> tuple[int, str, dict[str, str]]:
    """Return (status_code, response_text, response_headers)."""
    base = host.rstrip("/")
    p = path if path.startswith("/") else f"/{path}"
    url = base + p
    if query:
        url = f"{url}?{urllib.parse.urlencode(query)}"

    http = urllib3.PoolManager()
    headers = {
        "Authorization": f"Bearer {token}",
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
