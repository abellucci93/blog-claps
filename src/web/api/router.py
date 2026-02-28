from fastapi import APIRouter

from .claps.router import router as claps_router


router = APIRouter(prefix="/api")
router.include_router(claps_router)
