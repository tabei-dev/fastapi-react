'''
メッセージリポジトリ
'''

import json
from functools import lru_cache
from app.models.message import Message
from apps.backend.app.repositories.json_access import get_json_path
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def __load_messages_json() -> dict[int, Message]:
    '''
    massages.jsonを読み込み、メッセージ一覧を取得します
    :return: dict[Message]: メッセージ辞書
    '''
    messages_json_path = get_json_path('messages.json')
    # logger.info(f'messages_json_path: {messages_json_path}') # デバッグ用ログ
    with open(messages_json_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return {message['number']: Message(**message) for message in json_data['messages']}

_messages = __load_messages_json()

def get_message(number: int) -> str:
    '''
    メッセージ番号に該当するメッセージを取得する
    :param number: int: 番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    message = _messages.get(number)
    if message:
        return message.message

    raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")