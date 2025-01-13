from enum import Enum
from pydantic import BaseModel

class ClassificationEnum(Enum):
    '''
    区分の列挙型
    :param ROLE: str: 権限区分
    '''
    ROLE = 'Role'

class ClassificationDetail(BaseModel):
    '''
    区分明細情報
    :param detail_number: int: 明細番号
    :param detail_name: str: 区分明細名
    :param detail_jp_name: str: 区分明細日本語名
    '''
    detail_number: int
    detail_name: str
    detail_jp_name: str

class Classification(BaseModel):
    '''
    区分情報
    :param classification_enum: ClassificationEnum: 区分列挙型
    :param details: dict[int, ClassificationDetail]: 区分明細情報辞書
    '''
    classification_enum: ClassificationEnum
    details: dict[int, ClassificationDetail]