import jwt
from datetime import datetime, timedelta
from app.domain.value_objects.username import Username
from app.helpers.settings import settings
from app.helpers.datetime import get_now

__ALGORITHM = "HS256"

class Token:
    def __init__(self, access_token: str):
        self.value = access_token

    def fetch_username(self) -> Username | None:
        try:
            payload = jwt.decode(self.value, settings.SECRET_KEY, algorithms=[__ALGORITHM])
            username: str = payload.get("sub")
            if username:
                return Username(username)
        except jwt.PyJWTError:
            pass

        # raise ValidationError(get_message('4003'), 'username')
        return None

def create_token(username: str) -> Token:
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
