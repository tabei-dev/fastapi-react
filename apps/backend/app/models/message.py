from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

class Message(BaseModel):
    '''
    メッセージ情報
    :param number: str: メッセージ番号
    :param message: str: メッセージ
    '''
    number: Annotated[str, StringConstraints(min_length=1, max_length=4)]
    message: Annotated[str, StringConstraints(min_length=1, max_length=256)]

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
