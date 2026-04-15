"""Shared test fixtures for the Music Appreciation and Discovery API test suite."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def test_client():
    """Provide a TestClient that properly triggers the lifespan context manager."""
    with TestClient(app) as c:
        yield c
