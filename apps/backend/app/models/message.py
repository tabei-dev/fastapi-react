from pydantic import BaseModel

class Message(BaseModel):
    '''
    メッセージ情報
    :param number: int: メッセージ番号
    :param message: str: メッセージ
    '''
    number: int
    message: str