import dataclasses
from enum import Enum
from pydantic import BaseModel
from app.domain.value_objects.classification_detail import ClassificationDetail

class ClassificationEnum(Enum):
    '''
    区分の列挙型
    :param NONE: str: 未設定
    :param ROLE: str: 権限区分
    '''
    NONE = 'NONE'
    ROLE = 'ROLE'

@dataclasses.dataclass(frozen=True)
class Classification(BaseModel):
    '''
    区分情報
    :param classification_enum: ClassificationEnum: 区分列挙型
    :param details: dict[int, ClassificationDetail]: 区分明細情報辞書
    '''
    classification_enum: ClassificationEnum
    details: dict[str, ClassificationDetail]