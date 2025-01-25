import jwt
from redis import Redis
from datetime import datetime, timedelta
from app.config.settings import settings
from app.utils.datetime import DateTimeUtil

class Token:
    '''
    トークン情報
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    '''
    SECRET_KEY = settings.secret_key
    '''シークレットキー'''
    ALGORITHM = "HS256"
    '''アルゴリズム'''
    ACCESS_TOKEN_EXPIRE_MINUTES = int(settings.access_token_expire_minutes)
    '''トークンの有効期限(分)'''
    TOKEN_TYPE = "bearer"
    '''トークンの種類'''

    def __init__(self, access_token: str):
        '''
        プライベートコンストラクタ
        :param access_token: str: トークン
        '''
        if not hasattr(self, '_Token__initialized'):
            self.access_token = access_token
            self.token_type = self.TOKEN_TYPE

    @classmethod
    def create_token_by_username(cls, username: str) -> 'Token':
        '''
        トークン情報インスタンスを生成します
        :param access_token: str: トークン
        :return: Token: トークン情報
        '''
        access_token = Token.__create_access_token(username)
        return cls(access_token)

    @classmethod
    def create_token_by_token(cls, access_token: str) -> 'Token':
        '''
        トークン情報インスタンスを生成します
        :param access_token: str: トークン
        :return: Token: トークン情報
        '''
        return cls(access_token)

    def verify_token(self, redis: Redis) -> str | None:
        '''
        トークンを検証します
        検証に成功した場合はユーザー名を返し、検証に失敗した場合はNoneを返します
        :param redis: Redis: Redisインスタンス
        :return: str | None: ユーザー名
        '''
        try:
            payload = jwt.decode(self.access_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                return None
        except jwt.PyJWTError:
            return None

        if redis.exists(self.token):
            return None

        return username

    # def has_token_on_blacklist(self, redis: Redis) -> bool:
    #     '''
    #     トークンがブラックリストに存在するかを確認します
    #     :param redis: Redis: Redisインスタンス
    #     :param token: str: トークン
    #     :return: bool: トークンが存在する場合はTrue
    #     '''
    #     return redis.exists(self.token)

    @staticmethod
    def __create_access_token(username: str) -> str:
        '''
        トークンを生成します
        :param username: str: ユーザー名
        :return: str: トークン
        '''
        expire = Token.__create_expire()
        to_encode = {"sub": username, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, Token.SECRET_KEY, algorithm=Token.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def __create_expire() -> datetime:
        '''
        有効期限を生成します
        :return: datetime: 有効期限
        '''
        expires_delta = timedelta(minutes=Token.ACCESS_TOKEN_EXPIRE_MINUTES)
        if expires_delta:
            return DateTimeUtil.now() + expires_delta
        else:
            return DateTimeUtil.now() + timedelta(minutes=15)
