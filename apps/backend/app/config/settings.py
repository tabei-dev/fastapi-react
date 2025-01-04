import os
import json
from typing import ClassVar
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
    :param assets_path: str: アセットのパス
    '''

    __base_path = os.path.join(os.path.dirname(__file__), '../../assets')
    model_config = SettingsConfigDict(env_file=os.path.join(__base_path, 'settings.env'))

    environment: str = os.getenv("ENVIRONMENT", "development")
    allow_origins: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    redis_port: int = int(os.getenv("REDIS_PORT", 6379))
    secret_key: str = os.getenv("SECRET_KEY", "secret")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    # assets_path: ClassVar[str] = os.path.join(os.path.dirname(__file__), '../../assets')
    assets_path: str = os.path.join(__base_path, os.getenv("ASSETS_PATH", "."))

settings = Settings()