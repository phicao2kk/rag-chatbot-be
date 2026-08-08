from fastapi import APIRouter

router = APIRouter(tags=["core"])

@router.get("/ping")
def do_ping():
    return {
        "message": "pong"
    }