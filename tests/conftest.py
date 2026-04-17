"""Shared test fixtures for the Music Appreciation and Discovery API test suite."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

# The demo API key used across all write-operation tests.
DEMO_API_KEY = "music-api-demo-key-2026"
AUTH_HEADERS = {"X-API-Key": DEMO_API_KEY}


@pytest.fixture(scope="session")
def test_client():
    """Provide a TestClient that properly triggers the lifespan context manager."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def auth_headers():
    """Return the authentication headers required for write operations."""
    return AUTH_HEADERS.copy()
