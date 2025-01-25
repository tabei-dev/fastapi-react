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
