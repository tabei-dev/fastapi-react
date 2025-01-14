# from pydantic.dataclasses import dataclass
from pydantic import BaseModel, constr

# @dataclass
class Message(BaseModel):
    '''
    メッセージ情報
    :param number: int: メッセージ番号
    :param message: str: メッセージ
    '''
    number: constr(min_length=1, max_length=4) # type: ignore
    message: constr(min_length=1, max_length=256) # type: ignore
