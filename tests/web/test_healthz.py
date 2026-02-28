from fastapi import status
from fastapi.testclient import TestClient


def test_healthz(client: TestClient):
    response = client.get("/healthz")
    assert response.status_code == status.HTTP_204_NO_CONTENT
