
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

class Settings(BaseSettings):
    '''
    設定クラス
    :param environment: str: 環境
    :param allow_origins: str: CORSの許可元
    :param database_url: str: データベースのURL
    :param redis_port: int: Redisのポート
    :param secret_key: str: シークレットキー
    :param access_token_expire_minutes: int: トークンの有効期限
    '''

    environment: str = os.getenv("ENVIRONMENT", "development")
    allow_origins: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    redis_port: str | int = os.getenv("REDIS_PORT", 6379)
    secret_key: str = os.getenv("SECRET_KEY", "secret")
    access_token_expire_minutes: str | int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '../..', 'settings.env'))

settings = Settings()
'''
設定
'''