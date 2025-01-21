'''
メッセージ情報リポジトリ
'''
import yaml
from functools import lru_cache
from app.models.message import Message
from app.repositories.yaml_access import get_yaml_data

@lru_cache(maxsize=1)
def __load_messages_yaml() -> dict[str, Message]:
    '''
    massages.yamlを読み込み、メッセージ情報辞書を取得します
    :return: dict[Message]: メッセージ情報辞書
    '''
    yaml_data = get_yaml_data('messages.yaml')
    return {message['number']: Message(**message) for message in yaml_data['messages']}

def get_message(number: str) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param number: str: メッセージ番号
    :return: str: メッセージ
    :raise ValueError: メッセージが見つからない場合
    '''
    messages = __load_messages_yaml()
    message = messages.get(number)
    if message:
        return message.message

    # raise ValueError(f"メッセージ番号({number})に該当するメッセージが見つかりませんでした")
    assert False, f"メッセージ番号({number})に該当するメッセージが見つかりませんでした"
