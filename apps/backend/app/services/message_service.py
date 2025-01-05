import os
import json
from app.config.settings import settings
from app.models.message import Message
from app.utils.singlton import SingletonMeta

class MessageService(metaclass=SingletonMeta):
    '''
    メッセージ情報サービスクラス
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        '''
        シングルトンインスタンスを生成する
        :return: MessageService: メッセージ情報サービス
        '''
        if cls._instance is None:
            cls._instance = super(MessageService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        '''
        コンストラクタ
        '''
        if not hasattr(self, 'initialized'):  # 初期化が一度だけ行われるようにする
            messages_json_path = os.path.join(settings.assets_path, 'messages.json')
            if os.path.exists(messages_json_path):
                with open(messages_json_path, 'r', encoding='utf-8') as file:
                    json_data = json.load(file)
                    self.messages = [Message(**message) for message in json_data['messages']]
            self.initialized = True

    def get_message(self, number: int) -> str:
        '''
        メッセージ番号に該当するメッセージを取得する
        :param number: int: 番号
        :return: str: メッセージ
        :raise ValueError: メッセージが見つからない場合
        '''
        for message in self.messages:
            if message.number == number:
                return message.message

        raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")


message_service = MessageService()