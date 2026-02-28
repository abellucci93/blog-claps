from fastapi import APIRouter, Response, status

from .api.router import router as api_router


router = APIRouter()


@router.get(
    path="/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def root():
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/healthz", status_code=status.HTTP_204_NO_CONTENT)
def healthy() -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)


router.include_router(api_router)
