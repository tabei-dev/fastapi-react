
import os
import json
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from app.models.message import Message, MessageManager
from app.models.classification import Classification, ClassificationManager

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
    :param messages: Messages: メッセージ情報
    :param classification_manager: ClassificationManager: 区分管理クラス
    '''

    environment: str = os.getenv("ENVIRONMENT", "development")
    allow_origins: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    redis_port: str | int = os.getenv("REDIS_PORT", 6379)
    secret_key: str = os.getenv("SECRET_KEY", "secret")
    access_token_expire_minutes: str | int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    message_manager: MessageManager = Field(default_factory=lambda: MessageManager(messages=[]))
    classification_manager: ClassificationManager = Field(default_factory=lambda: ClassificationManager(classifications=[]))

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '../../assets', 'settings.env'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        messages_path = os.path.join(base_dir, 'assets', 'messages.json')
        if os.path.exists(messages_path):
            with open(messages_path, 'r', encoding='utf-8') as file:
                messages_data = json.load(file)
                messages = [Message(**message) for message in messages_data['messages']]
                self.message_manager = MessageManager(messages)

        classifications_path = os.path.join(base_dir, 'assets', 'classifications.json')
        if os.path.exists(classifications_path):
            with open(classifications_path, 'r', encoding='utf-8') as file:
                classifications_data = json.load(file)
                classifications = [Classification(**classification) for classification in classifications_data['classifications']]
                self.classification_manager = ClassificationManager(classifications)

settings = Settings()
'''
設定
'''