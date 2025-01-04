import os
import json
import unittest
from app.config.settings import settings
from app.models.message import Message, MessageManager
from app.models.classification import Classification, ClassificationManager, ClassificationEnum

class TestSettings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ["ENVIRONMENT"] = "development"
        os.environ["ALLOW_ORIGINS"] = "http://example.com"
        os.environ["DATABASE_URL"] = "sqlite:///./test.db"
        os.environ["REDIS_PORT"] = "6379"
        os.environ["SECRET_KEY"] = "secret"
        os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "30"
        # 環境変数を再読み込み
        settings.environment = os.getenv("ENVIRONMENT", "development")
        settings.allow_origins = os.getenv("ALLOW_ORIGINS", "http://example.com")
        settings.database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
        settings.redis_port = int(os.getenv("REDIS_PORT", 6379))
        settings.secret_key = os.getenv("SECRET_KEY", "secret")
        settings.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    def test_environment(self):
        self.assertEqual(settings.environment, os.getenv("ENVIRONMENT", "development"))

    def test_allow_origins(self):
        self.assertEqual(settings.allow_origins, os.getenv("ALLOW_ORIGINS", "http://example.com"))

    def test_database_url(self):
        self.assertEqual(settings.database_url, os.getenv("DATABASE_URL", "sqlite:///./test.db"))

    def test_redis_port(self):
        self.assertEqual(settings.redis_port, int(os.getenv("REDIS_PORT", 6379)))

    def test_secret_key(self):
        self.assertEqual(settings.secret_key, os.getenv("SECRET_KEY", "secret"))

    def test_access_token_expire_minutes(self):
        self.assertEqual(settings.access_token_expire_minutes, int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))

    # def test_messages(self):
    #     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #     messages_path = os.path.join(base_dir, 'assets', 'messages.json')
    #     with open(messages_path, 'r', encoding='utf-8') as file:
    #         expected_messages = json.load(file)
    #         expected_messages = [Message(**message) for message in expected_messages['messages']]
    #         expected_message_manager = MessageManager(expected_messages)
    #     print("settings.messages: ", settings.message_manager, "\n")
    #     self.assertEqual(settings.message_manager.get_message(1), expected_message_manager.get_message(1))

    # def test_classifications(self):
    #     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #     classifications_path = os.path.join(base_dir, 'assets', 'classifications.json')
    #     with open(classifications_path, 'r', encoding='utf-8') as file:
    #         expected_classifications = json.load(file)
    #         expected_classifications = [Classification(**classification) for classification in expected_classifications['classifications']]
    #         expected_classification_manager = ClassificationManager(expected_classifications)
    #     print("settings.classification_manager: ", settings.classification_manager.get_classifications(ClassificationEnum.ROLE), "\n")
    #     self.assertEqual(settings.classification_manager.get_classifications(ClassificationEnum.ROLE), expected_classification_manager.get_classifications(ClassificationEnum.ROLE))

if __name__ == '__main__':
    unittest.main()