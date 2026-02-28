from typing import Generator
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from testcontainers.redis import RedisContainer

from src.settings import settings
from src.bootstrap import bootstrap

redis = RedisContainer(image="redis:7", port=6379)


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    redis.start()

    settings.REDIS_HOST = redis.get_container_host_ip()
    settings.REDIS_PORT = redis.get_exposed_port(port=6379)

    def remove_container():
        redis.stop()

    request.addfinalizer(remove_container)


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI]:
    test_app = bootstrap()

    yield test_app


@pytest.fixture(scope="session")
def client(app: FastAPI) -> Generator[TestClient]:
    test_client = TestClient(app)
    yield test_client
