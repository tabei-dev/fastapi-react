import jwt
from datetime import datetime, timedelta
from app.domain.value_objects.token import Token
from app.helpers.settings import settings
from app.helpers.datetime import get_now

__ALGORITHM = "HS256"

def create_token(access_token: str) -> Token:
    return Token(access_token)

def create_token_by_username(username: str) -> Token:
    access_token = __generate_access_token(username)
    return Token(access_token)

def __generate_access_token(username: str) -> str:
    token_expiration_date = __genecate_token_expiration_date()
    to_encode = {"sub": username, "exp": token_expiration_date}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=__ALGORITHM)
    return encoded_jwt

def __genecate_token_expiration_date() -> datetime:
    expirtion_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    if expirtion_delta:
        return get_now() + expirtion_delta
    else:
        return get_now() + timedelta(minutes=15)