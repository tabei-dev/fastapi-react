from pydantic import BaseModel

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
    :param classification_name: str: 区分名
    :param classification_jp_name: str: 区分日本語名
    :param classificationDetails: list[ClassificationDetail]: 区分明細情報リスト
    '''
    classification_name: str
    classification_jp_name: str
    details: list[ClassificationDetail]