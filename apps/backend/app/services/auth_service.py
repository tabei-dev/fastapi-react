import redis as Redis
from sqlalchemy.orm import Session
from app.domain.factories.auth_factory import create_auth
from app.domain.factories.token_factory import create_token
from app.domain.value_objects.auth import Auth
from app.domain.value_objects.username import Username
from app.helpers.settings import settings
from app.infrastrucure.repositories.user_repository import fetch_user
from app.services.message_service import get_message
from app.services.validation_error import ValidationError

__redis = Redis.Redis(host='redis', port=settings.REDIS_PORT, db=0)

def authenticate(db: Session, username: str, plain_password: str) -> Auth:
    try:
        user_dto = fetch_user(db, username)
    except Exception:
        raise ValidationError(get_message('4001'), 'username')

    try:
        return create_auth(username, plain_password, user_dto.hashed_password)
    except Exception:
        raise ValidationError(get_message('4002'), 'password')

def verify_token(access_token: str) -> Username:
    if not __exists(access_token):
        raise ValidationError(get_message('4003'), 'username')

    token = create_token(access_token)
    try:
        username = token.fetch_username()
        return username
    except Exception:
        raise ValidationError(get_message('4003'), 'username')

def revoke_token(access_token: str):
    __redis.set(access_token, "revoked", ex=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    # トークンをブラックリストに追加

def __exists(access_token: str) -> bool:
    return __redis.get(access_token) is not None
