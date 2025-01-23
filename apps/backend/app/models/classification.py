from enum import Enum
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

class ClassificationEnum(Enum):
    '''
    区分の列挙型
    :param NONE: str: 未設定
    :param ROLE: str: 権限区分
    '''
    NONE = 'None'
    ROLE = 'Role'

class ClassificationDetail(BaseModel):
    '''
    区分明細情報
    :param detail_number: str: 明細番号
    :param detail_name: str: 区分明細名
    :param detail_jp_name: str: 区分明細日本語名
    '''
    detail_number: Annotated[str, StringConstraints(min_length=1, max_length=2)]
    detail_name: Annotated[str, StringConstraints(min_length=1, max_length=15)]
    detail_jp_name: Annotated[str, StringConstraints(min_length=1, max_length=20)]

class Classification(BaseModel):
    '''
    区分情報
    :param classification_enum: ClassificationEnum: 区分列挙型
    :param details: dict[int, ClassificationDetail]: 区分明細情報辞書
    '''
    classification_enum: ClassificationEnum
    details: dict[str, ClassificationDetail]