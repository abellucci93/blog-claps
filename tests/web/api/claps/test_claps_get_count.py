from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from src.web.api.claps.schemas import (
    ClapsCreateRequest,
    ClapsGetCountRequest,
    ClapsGetCountResponse,
)
from tests.factories.web.api.claps import ClapsCreateRequestFactory


def test_claps_get_count(app: FastAPI, client: TestClient):
    count_expected = 1
    request: ClapsCreateRequest = ClapsCreateRequestFactory.create()

    response = client.post(
        url=app.url_path_for("claps_create"), json=request.model_dump()
    )
    assert response.status_code == status.HTTP_200_OK

    request: ClapsCreateRequest = ClapsCreateRequestFactory.create(
        identifier=request.identifier
    )
    response = client.get(
        url=app.url_path_for("claps_get_count"), params=request.model_dump()
    )

    assert response.status_code == status.HTTP_200_OK
    data = ClapsGetCountResponse(**response.json())
    assert data.clap.identifier == request.identifier
    assert data.clap.count == count_expected


def test_claps_get_count_returns_not_found_when_identifier_not_exists(
    app: FastAPI, client: TestClient
):
    request: ClapsGetCountRequest = ClapsCreateRequestFactory.create()

    response = client.get(
        url=app.url_path_for("claps_get_count"), params=request.model_dump()
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
