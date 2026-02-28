from fastapi import APIRouter, Depends, HTTPException, status
from redis.asyncio import Redis

from src.services.redis import get_redis

from .schemas import (
    Clap,
    ClapsCreateRequest,
    ClapsCreateResponse,
    ClapsGetCountResponse,
)


router = APIRouter(
    prefix="/claps",
    tags=["Claps"],
)


@router.post("/", response_model=ClapsCreateResponse)
async def claps_create(
    request: ClapsCreateRequest, redis: Redis = Depends(get_redis)
) -> ClapsCreateResponse:
    # using redis incr for atomic counter increment.
    # If key doesn't exists, it initializes the counter.
    count: int = await redis.incr(request.identifier)

    return ClapsCreateResponse(clap=Clap(identifier=request.identifier, count=count))


@router.get("/count", response_model=ClapsGetCountResponse)
async def claps_get_count(
    identifier: str, redis: Redis = Depends(get_redis)
) -> ClapsGetCountResponse:
    count = await redis.get(identifier)

    if count is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return ClapsGetCountResponse(clap=Clap(identifier=identifier, count=count))
