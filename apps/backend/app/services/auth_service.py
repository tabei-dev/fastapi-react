import redis as Redis
from sqlalchemy.orm import Session
from app.config.settings import settings
from app.errors.validation_error import ValidationError
from app.models.auth import Auth
from app.models.token import Token
from app.models.user import User
from app.managers.message_manager import get_message
from app.utils.hash import verify_password

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

    def verify_token(self, access_token: str) -> str:
        '''
        トークンを検証します
        検証に成功した場合、ユーザー名を返します
        :param access_token: str: トークン
        :return: str: ユーザー名
        :raise ValidationError: 検証に失敗した場合
        '''
        token = Token.create_token_by_token(access_token)
        username = token.verify_token(self.redis)
        if not username:
            raise ValidationError(get_message('4003'), 'username')

        return username

    def revoke_token(self, token: str) -> None:
        '''
        トークンを削除します
        :param token: str: トークン
        '''
        # トークンをブラックリストに追加
        self.redis.set(token, "revoked", ex=Token.ACCESS_TOKEN_EXPIRE_MINUTES * 60)

auth_service = AuthService()