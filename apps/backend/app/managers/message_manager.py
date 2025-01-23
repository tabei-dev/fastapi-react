from app.models.message import Message
from app.utils.yaml_access import get_yaml_data

def create_messages() -> dict[str, Message]:
    '''
    メッセージ情報を生成します
    :return: dict[str, Message]: メッセージ辞書
    '''
    yaml_data = get_yaml_data('messages.yaml')
    messages = {message['number']: Message(**message) for message in yaml_data['messages']}
    return messages

def get_message(messages: dict[str, Message], number: str) -> str:
    '''
    メッセージ番号に該当するメッセージを取得します
    :param messages: dict[str, Message]: メッセージ辞書
    :param number: str: メッセージ番号
    :return: str: メッセージ
    '''
    message = messages.get(number)
    if message:
        return message.message
    else:
        return ""
