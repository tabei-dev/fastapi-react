import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()
# .envファイルの読み込み

class __Settings(BaseSettings):
    '''
    設定クラス
    :param environment: str: 環境
    :param allow_origins: str: CORSの許可元
    :param database_url: str: データベースのURL
    :param redis_port: int: Redisのポート
    :param secret_key: str: シークレットキー
    :param access_token_expire_minutes: int: トークンの有効期限
    '''
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    ALLOW_ORIGINS: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    model_config = SettingsConfigDict(env_file='settings.env')

settings = __Settings()
