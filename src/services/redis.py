from typing import AsyncGenerator

from redis.asyncio import Redis

from src.settings import settings


async def get_redis() -> AsyncGenerator[Redis, None]:
    REDIS_URL = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"

    redis = Redis.from_url(
        REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
    )

    try:
        yield redis
    finally:
        await redis.close()
