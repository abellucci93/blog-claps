from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from src.web.api.claps.schemas import ClapsCreateRequest, ClapsCreateResponse
from tests.factories.web.api.claps import ClapsCreateRequestFactory


def test_claps_create(app: FastAPI, client: TestClient):
    count_expected = 1
    request: ClapsCreateRequest = ClapsCreateRequestFactory.create()

    response = client.post(
        url=app.url_path_for("claps_create"), json=request.model_dump()
    )

    assert response.status_code == status.HTTP_200_OK
    data = ClapsCreateResponse(**response.json())
    assert data.clap.identifier == request.identifier
    assert data.clap.count == count_expected


def test_claps_create_increment_count_for_existing_identifier(
    app: FastAPI, client: TestClient
):
    count_expected = 2
    request: ClapsCreateRequest = ClapsCreateRequestFactory.create()

    response = client.post(
        url=app.url_path_for("claps_create"), json=request.model_dump()
    )
    assert response.status_code == status.HTTP_200_OK

    response = client.post(
        url=app.url_path_for("claps_create"), json=request.model_dump()
    )

    assert response.status_code == status.HTTP_200_OK
    data = ClapsCreateResponse(**response.json())
    assert data.clap.identifier == request.identifier
    assert data.clap.count == count_expected
