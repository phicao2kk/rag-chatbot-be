import datetime
from concurrent.futures import ProcessPoolExecutor
from typing import Any

import jwt


def get_workspace_path():
    import os
    script_dir_os = os.path.dirname(os.path.abspath(__file__))
    return script_dir_os

def __encode(payload, secretkey, settings):
    return jwt.encode(payload, secretkey, algorithm=settings.JWT_ALGORITHM),

def jwt_encode(payload: dict[str,Any], settings) -> dict[str, str]:
    accesstoken_secretkey = settings.ACCESS_TOKEN_SECRET_KEY
    refrentoken_secretkey = settings.REFRESH_TOKEN_SECRET_KEY

    accesstoken_expire = settings.ACCESS_TOKEN_EXPIRED
    refrentoken_expire = settings.REFRESH_TOKEN_EXPIRED

    accesstoken_payload = {
        **payload,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=accesstoken_expire)
    }

    refreshtoken_payload = {
        **payload,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=refrentoken_expire)
    }

    collections = [
        (accesstoken_payload, accesstoken_secretkey, settings),
        (refreshtoken_payload, refrentoken_secretkey, settings)
    ]

    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(__encode, *params) for params in collections
        ]
        results = list(f.result() for f in futures)

    return {
        'access_token': results[0][0],
        'refresh_token': results[1][0]
    }
