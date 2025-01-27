import redis as Redis
from sqlalchemy.orm import Session
from app.helpers.hash import verify_password
from app.helpers.settings import settings
from app.errors.validation_error import ValidationError
from app.models.auth import Auth
from app.models.token import Token
from app.models.user import User
from app.usecases.message_usecase import get_message

__redis = Redis.Redis(host='redis', port=settings.REDIS_PORT, db=0)

def authenticate(db: Session, username: str, password: str) -> Auth:
    # user = db.query(User).filter(User.username == username).first()
    user = db.query(User.username, User.password, User.email, User.role_cls).filter(User.username == username).first()
    if not user:
        raise ValidationError(get_message('4001'), 'username')

    if not verify_password(password, user.password):
        raise ValidationError(get_message('4002'), 'password')

    token = Token.create_token_by_username(username)

    auth = Auth(
        username=user.username,
        email=user.email,
        role_cls=user.role_cls,
        token_type=token.token_type,
        access_token=token.access_token,
    )
    return auth

def verify_token(access_token: str) -> str:
    token = Token.create_token_by_token(access_token)
    username = token.verify_token(__redis)
    if not username:
        raise ValidationError(get_message('4003'), 'username')

    return username

def revoke_token(token: str) -> None:
    __redis.set(token, "revoked", ex=Token.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    # トークンをブラックリストに追加
