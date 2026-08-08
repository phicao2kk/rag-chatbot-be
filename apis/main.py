from fastapi import APIRouter
from apis import core
from core.config import settings

router = APIRouter()
router.include_router(core.router)

"""
add local api
"""
# if settings.ENVIRONMENT == "local":
#     router.include_router
