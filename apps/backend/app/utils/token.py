'''
トークンユーティリティ
'''
import jwt
import redis as Redis
from datetime import datetime, timedelta
from app.config.settings import settings
from app.utils.datetime import DateTimeUtil

SECRET_KEY = settings.secret_key
'''シークレットキー'''
ALGORITHM = "HS256"
'''アルゴリズム'''
ACCESS_TOKEN_EXPIRE_MINUTES = int(settings.access_token_expire_minutes)
'''トークンの有効期限(分)'''
TOKEN_TYPE = "bearer"
'''トークンの種類'''

def create_access_token(username: str) -> str:
    '''
    トークンを生成します
    :param username: str: ユーザー名
    :return: str: トークン
    '''
    expire = __create_expire()
    to_encode = {"sub": username, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def __create_expire() -> datetime:
    '''
    有効期限を生成します
    :return: timedelta: 有効期限
    '''
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        return DateTimeUtil.now() + expires_delta
    else:
        return DateTimeUtil.now() + timedelta(minutes=15)

def verify_token(token: str) -> str | None:
    '''
    トークンを検証します
    検証に成功した場合はユーザー名を返し、検証に失敗した場合はNoneを返します
    :param token: str: トークン
    :return: str | None: ユーザー名
    '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
    except jwt.PyJWTError:
        return None

    return username

def has_token_on_blacklist(redis: Redis, token: str) -> bool:
    '''
    トークンがブラックリストに存在するかを確認します
    :param redis: Redis: Redisインスタンス
    :param token: str: トークン
    :return: bool: トークンが存在する場合はTrue
    '''
    return redis.exists(token)

