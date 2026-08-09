from fastapi import APIRouter

from core.config import settings
from core.models import auth
from utils import jwt_encode

router = APIRouter(prefix="/auth", tags=["core"])

@router.post("/login")
def gen_token(
    login_payload: auth.AuthLoginModel
):
    return jwt_encode(login_payload.dict(), settings)


# TODO: register
# TODO: logout
# TODO: refresh token
# TODO: reset password
# TODO: change password
