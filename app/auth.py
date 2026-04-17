"""API Key authentication module for the Music Appreciation and Discovery API.

Implements a lightweight API key authentication scheme using FastAPI's
dependency injection. Read-only endpoints (GET) remain publicly accessible,
while write operations (POST, PUT, DELETE) require a valid API key passed
via the ``X-API-Key`` header.

Default demo key: ``music-api-demo-key-2026``
"""

import os

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# The demo key is suitable for coursework demonstration.  In a production
# environment this would be loaded from a secrets manager or environment
# variable exclusively.
VALID_API_KEYS: set[str] = {
    os.getenv("MUSIC_API_KEY", "music-api-demo-key-2026"),
}


# ---------------------------------------------------------------------------
# Dependency
# ---------------------------------------------------------------------------

async def require_api_key(
    api_key: str | None = Security(API_KEY_HEADER),
) -> str:
    """Validate the API key provided in the request header.

    Raises:
        HTTPException 401: If the header is missing.
        HTTPException 403: If the key is present but invalid.
    """
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "authentication_required",
                "message": "Missing API key. Provide a valid key via the X-API-Key header.",
            },
        )
    if api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "error": "invalid_api_key",
                "message": "The provided API key is not valid.",
            },
        )
    return api_key
