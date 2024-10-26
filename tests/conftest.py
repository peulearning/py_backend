import pytest
from fastapi.testclient import TestClient

from api_fast.app import app


@pytest.fixture
def client():
    return TestClient(app)
