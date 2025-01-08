import os
import json
from functools import lru_cache
from app.config.settings import settings
from app.models.message import Message
from app.utils.singlton import SingletonMeta
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# import os
# import json
# from functools import lru_cache
# from app.models.message import Message

@lru_cache(maxsize=1)
def __load_messages():
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    messages_json_path = os.path.join(assets_path, 'messages.json')
    if os.path.exists(messages_json_path):
        with open(messages_json_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return [Message(**message) for message in json_data['messages']]
    return []

_messages = __load_messages()

def get_message(number: int) -> str:
    '''
    メッセージ番号に該当するメッセージを取得する
    :param number: int: 番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    # logger.info(f"メッセージ一覧: {_messages}")
    # if not self.messages:
    #     self.__init__()
    for message in _messages:
        if message.number == number:
            return message.message

    raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")

# class MessageService(metaclass=SingletonMeta):
#     '''
#     メッセージ情報サービスクラス
#     '''
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         '''
#         コンストラクタ
#         シングルトンインスタンスを生成する
#         :return: MessageService: メッセージ情報サービス
#         '''
#         logger.debug(f"メッセージサービスのNEW")
#         if cls._instance is None:
#             cls._instance = super(MessageService, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

#     def __init__(self):
#         '''
#         コンストラクタ
#         '''
#         logger.debug(f"メッセージサービスのコンストラクタ")
#         if not hasattr(self, 'initialized_massage_controller'):  # 初期化が一度だけ行われるようにする
#             current_file_dir = os.path.dirname(os.path.abspath(__file__))
#             assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
#             messages_json_path = os.path.join(assets_path, 'messages.json')
#             logger.debug(f"メッセージJSONのパス: {messages_json_path}")
#             if os.path.exists(messages_json_path):
#                 with open(messages_json_path, 'r', encoding='utf-8') as file:
#                     json_data = json.load(file)
#                     self.messages = [Message(**message) for message in json_data['messages']]
#             self.initialized = True

#     def get_message(self, number: int) -> str:
#         '''
#         メッセージ番号に該当するメッセージを取得する
#         :param number: int: 番号
#         :return: str: メッセージ
#         :raise ValueError: メッセージが見つからない場合
#         '''
#         logger.debug(f"メッセージ一覧: {self.messages}")
#         if not self.messages:
#             self.__init__()
#         for message in self.messages:
#             if message.number == number:
#                 return message.message

#         raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")


# message_service = MessageService()
