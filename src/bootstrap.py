from fastapi import FastAPI

from .web.router import router
from .settings import settings


def bootstrap() -> FastAPI:
    """
    Bootstrap and configure FastAPI app and returns it.
    """
    app = FastAPI(debug=settings.DEBUG)  # @TODO: Configure fastapi app

    app.include_router(router)

    return app
