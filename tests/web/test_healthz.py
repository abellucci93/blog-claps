from fastapi import FastAPI, status
from fastapi.testclient import TestClient


def test_healthz(app: FastAPI, client: TestClient):
    response = client.get(url=app.url_path_for("healthz"))

    assert response.status_code == status.HTTP_204_NO_CONTENT
