import jwt
import redis as Redis
from datetime import datetime, timedelta
from app.config.settings import settings
from app.errors.validation_error import ValidationError
from app.services.message_service import message_service
from app.utils.datetime import DateTimeUtil

class TokenManager:
    '''
    トークンマネージャクラス
    '''
    SECRET_KEY = settings.secret_key
    '''シークレットキー'''
    ALGORITHM = "HS256"
    '''アルゴリズム'''
    ACCESS_TOKEN_EXPIRE_MINUTES = int(settings.access_token_expire_minutes)
    '''トークンの有効期限(分)'''
    TOKEN_TYPE = "bearer"
    '''トークンの種類'''

    def __init__(self):
        '''
        コンストラクタ
        '''
        self.redis = Redis.Redis(host='redis', port=settings.redis_port, db=0)

    def verify_token(self, token: str) -> str:
        '''
        トークンを検証します
        検証に成功した場合、ユーザー名を返します
        :param token: str: トークン
        :return: str: ユーザー名
        :raise ValueError: トークンが不正な場合
        :raise ValueError: トークンがブラックリストにある場合
        '''
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise ValidationError(message_service.get_message('4003'), 'username')
        except jwt.PyJWTError:
            raise ValidationError(message_service.get_message('4003'), 'username')

        # トークンがブラックリストにあるか確認
        if self.redis.get(token):
            raise ValidationError(message_service.get_message('4003'), 'username')

        return username

    # def has_token_on_blacklist(self, token: str) -> bool:
    #     '''
    #     トークンがブラックリストに存在するかを確認します
    #     :param token: str: トークン
    #     :return: bool: トークンが存在する場合はTrue
    #     '''
    #     return self.redis.exists(token)
    
    def add_token_to_blacklist(self, token: str) -> None:
        '''
        トークンをブラックリストに追加します
        :param token: str: トークン
        '''
        self.redis.set(token, "revoked", ex=self.ACCESS_TOKEN_EXPIRE_MINUTES * 60)

    def create_access_token(self, username: str) -> str:
        '''
        トークンを生成します
        :param username: str: ユーザー名
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

token_manager = TokenManager()