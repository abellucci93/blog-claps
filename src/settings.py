import os


class Settings:
    DEBUG: bool = bool(os.getenv("DEBUG", False))

    # Redis connection
    REDIS_HOST: str = os.getenv("REDIS_HOST", "")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 0))


settings = Settings()
