import redis as Redis
from sqlalchemy.orm import Session
from app.domain.value_objects.auth import Auth
from app.domain.value_objects.token import Token
from app.domain.value_objects.username import Username
from app.helpers.settings import settings
from app.errors.validation_error import ValidationError
from app.infrastrucure.dtos.user_dto import UserDTO
from app.usecases.message_usecase import get_message

__redis = Redis.Redis(host='redis', port=settings.REDIS_PORT, db=0)

def authenticate(db: Session, username: str, plain_password: str) -> Auth:
    user_dto = db.query(UserDTO).filter(UserDTO.username == username).first()
    if not user_dto:
        raise ValidationError(get_message('4001'), 'username')

    try:
        return Auth(username, plain_password, user_dto.hashed_password)
    except Exception:
        raise ValidationError(get_message('4002'), 'password')

def verify_token(access_token: str) -> Username:
    if not __exists(access_token):
        raise ValidationError(get_message('4003'), 'username')

    token = Token(access_token)
    try:
        return token.fetch_username()
    except Exception:
        raise ValidationError(get_message('4003'), 'username')

def revoke_token(access_token: str) -> None:
    __redis.set(access_token, "revoked", ex=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    # トークンをブラックリストに追加

def __exists(access_token: str) -> bool:
    return __redis.get(access_token) is not None
