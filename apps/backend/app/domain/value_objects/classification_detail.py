# from enum import Enum
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

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