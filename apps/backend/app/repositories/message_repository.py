'''
メッセージ情報リポジトリ
'''
from functools import lru_cache
from app.models.message import Message
from app.repositories.json_access import get_json_data

@lru_cache(maxsize=1)
def __load_messages_json() -> dict[int, Message]:
    '''
    massages.jsonを読み込み、メッセージ情報辞書を取得します
    :return: dict[Message]: メッセージ情報辞書
    '''
    json_data = get_json_data('messages.json')
    return {message['number']: Message(**message) for message in json_data['messages']}

__messages = __load_messages_json()

def get_message(number: int) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param number: int: メッセージ番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    message = __messages.get(number)
    if message:
        return message.message

    # raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")
    assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"