from datetime import datetime, timedelta

import jwt
from django.core.cache import cache
from django.utils import timezone

from settings import ACCESS_TTL, JWT_SECRET, REFRESH_TTL
from src.apps.accounts.selectors import user_exists
from src.errors import InvalidRefresh


def gen_token(data):
    return jwt.encode(payload=data, key=JWT_SECRET, algorithm="HS512")


def __gen_tokens(user_id):
    data = {
        "user_id": user_id,
        "created_at": timezone.now().strftime("%Y-%m-%d %H:%M:%S %z"),
        "type": "access",
    }
    access_token = gen_token(data=data)
    data["type"] = "refresh"
    data["access"] = access_token
    refresh_token = gen_token(data=data)
    cache.set(access_token, "", timeout=ACCESS_TTL)
    cache.set(refresh_token, "", timeout=REFRESH_TTL * 60)
    return access_token, refresh_token


def login(user):
    access_token, refresh_token = __gen_tokens(user_id=str(user.id))
    return {"access_token": access_token, "refresh_token": refresh_token}


def claim_token(token):
    return jwt.decode(jwt=token, key=JWT_SECRET, algorithms=["HS512"])


def __has_keys(data: dict, *keys):
    return all([i in data.keys() for i in keys])


def validate_token(token, check_time=True):
    if check_time and not cache.has_key(token):
        return False
    try:
        data = claim_token(token)
    except Exception:
        return False
    if "type" not in data.keys():
        return False
    delta = timedelta(seconds=ACCESS_TTL)
    if data.get("type") == "refresh":
        if not __has_keys(data, "user_id", "created_at", "type", "access"):
            return False
        access = data.get("access")
        if not validate_token(access, check_time=False):
            return False
        delta = timedelta(minutes=REFRESH_TTL)
    elif data.get("type") != "access" or not __has_keys(
        data, "user_id", "created_at", "type"
    ):
        return False
    user_id = data.get("user_id")
    if not user_exists(id=user_id):
        return False
    data_created_at_str = data.get("created_at")
    data_created_at = datetime.strptime(
        data_created_at_str, "%Y-%m-%d %H:%M:%S %z"
    )
    if check_time and timezone.now() > data_created_at + delta:
        return False
    return True


def refresh(token):
    if not validate_token(token):
        raise InvalidRefresh()
    jwt_data = claim_token(token)
    if jwt_data.get("type") != "refresh":
        raise InvalidRefresh()
    cache.delete(token)
    data_access = jwt_data.get("access")
    cache.delete(data_access)
    user_id = jwt_data.get("user_id")
    return __gen_tokens(user_id=user_id)
