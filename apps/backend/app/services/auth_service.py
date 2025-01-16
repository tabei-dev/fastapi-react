import redis as Redis
import jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.config.settings import settings
from app.errors.validation_error import ValidationError
from app.models.auth import Auth
from app.repositories.message_repository import get_message
from app.repositories.user_repository import UserRepository
from app.utils.datetime import DateTimeUtil

class AuthService:
    '''
    認証サービスクラス
    '''

    SECRET_KEY = settings.secret_key
    '''シークレットキー'''
    ALGORITHM = "HS256"
    '''アルゴリズム'''
    ACCESS_TOKEN_EXPIRE_MINUTES = int(settings.access_token_expire_minutes)
    '''トークンの有効期限(分)'''

    def __init__(self):
        '''
        コンストラクタ
        '''
        self.redis = Redis.Redis(host='redis', port=settings.redis_port, db=0)

    def authenticate(self, db: Session, username: str, password: str) -> Auth:
        '''
        ユーザー認証し、成功したらトークンを生成してこれを返します
        :param _db: Session: DBセッション
        :param username: str: ユーザ名
        :param password: str: パスワード
        :return: Auth: 認証情報
        :raise ValueError: ユーザが見つからない場合
        :raise ValueError: パスワードが一致しない場合
        '''
        user_repository = UserRepository(db)
        user = user_repository.authenticate(username, password)

        access_token = self.__create_access_token(username)

        auth = Auth(
            access_token=access_token,
            token_type="bearer",
            username=user.username,
            role_cls=user.role_cls,
        )

        return auth

    def verify_token(self, token: str) -> str:
        '''
        トークンを検証します
        検証に成功した場合、ユーザ名を返します
        :param token: str: トークン
        :return: str: ユーザー名
        :raise ValueError: トークンが不正な場合
        :raise ValueError: トークンがブラックリストにある場合
        '''
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise ValidationError(get_message('4003'), 'username')
        except jwt.PyJWTError:
            raise ValidationError(get_message('4003'), 'username')

        # トークンがブラックリストにあるか確認
        if self.redis.get(token):
            raise ValidationError(get_message('4003'), 'username')

        return username

    def revoke_token(self, token: str) -> None:
        '''
        トークンをブラックリストに登録します
        :param token: str: トークン
        '''
        self.redis.set(token, "revoked", ex=self.ACCESS_TOKEN_EXPIRE_MINUTES * 60)

    def __create_access_token(self, username: str) -> str:
        '''
        トークンを生成します
        :param username: str: ユーザ名
        :return: str: トークン
        '''
        expire = self.__create_expire()
        to_encode = {"sub": username, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def __create_expire(self) -> datetime:
        '''
        有効期限を生成します
        :return: timedelta: 有効期限
        '''
        expires_delta = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        if expires_delta:
            return DateTimeUtil.now() + expires_delta
        else:
            return DateTimeUtil.now() + timedelta(minutes=15)


auth_service = AuthService()