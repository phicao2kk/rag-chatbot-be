from fastapi import APIRouter

from apis import core
from apis.routes import auth, feedback

router = APIRouter()
router.include_router(core.router)
router.include_router(auth.router)
router.include_router(feedback.router)

"""
add local api
"""
# if settings.ENVIRONMENT == "local":
#     router.include_router
