import redis as Redis
from sqlalchemy.orm import Session
from app.config.settings import settings
from app.errors.validation_error import ValidationError
from app.models.auth import Auth, create_auth
from app.models.user import User
from app.services.message_service import message_service
from app.utils.token import (
    create_access_token,
    verify_token,
    has_token_on_blacklist,
    TOKEN_TYPE,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

class AuthService:
    '''
    認証サービスクラス
    '''
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.redis = Redis.Redis(host='redis', port=settings.redis_port, db=0)

    def authenticate(self, db: Session, username: str, password: str) -> Auth:
        '''
        ユーザー認証し、成功したら認証情報を生成してこれを返します
        :param _db: Session: DBセッション
        :param username: str: ユーザー名
        :param password: str: パスワード
        :return: Auth: 認証情報
        :raise ValidationError: ユーザーが見つからない場合
        :raise ValidationError: パスワードが一致しない場合
        '''
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise ValidationError(message_service.get_message('4001'), 'username')

        if not user.verify_password(password):
            raise ValidationError(message_service.get_message('4002'), 'password')

        access_token = create_access_token(username)

        auth = create_auth(
            access_token,
            TOKEN_TYPE,
            user.username,
            user.email,
            user.role_cls,
        )

        return auth

    def verify_token(self, token: str) -> str:
        '''
        トークンを検証します
        検証に成功した場合、ユーザー名を返します
        :param token: str: トークン
        :return: str: ユーザー名
        :raise ValueError: トークンが不正な場合
        :raise ValueError: トークンがブラックリストにある場合
        '''
        username = verify_token(token)
        if not username:
            raise ValidationError(message_service.get_message('4003'), 'username')

        if not has_token_on_blacklist(self.redis, token):
            raise ValidationError(message_service.get_message('4003'), 'username')

        return username

    def revoke_token(self, token: str) -> None:
        '''
        トークンを削除します
        :param token: str: トークン
        '''
        # トークンをブラックリストに追加
        self.redis.set(token, "revoked", ex=ACCESS_TOKEN_EXPIRE_MINUTES * 60)

auth_service = AuthService()