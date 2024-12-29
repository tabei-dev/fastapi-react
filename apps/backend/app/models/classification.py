from pydantic import BaseModel
from enum import Enum

class ClassificationEnum(Enum):
    '''
    区分の列挙型
    :param ROLE: str: 権限区分
    '''
    ROLE = "Role"

# class RoleEnum(Enum):
#     '''
#     権限区分の列挙型
#     :param ADMINISTRATOR: str: 管理者
#     :param GENERAL: str: 一般
#     '''
#     ADMINISTRATOR = "Administrator"
#     GENERAL = "General"

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

class ClassificationManager:
    '''
    区分情報管理クラス
    '''

    def __init__(self, classifications: list[Classification]):
        '''
        区分情報リストを設定する
        :param classifications: list[Classification]: 区分情報リスト
        '''
        self.classifications = classifications

    def get_classifications(self, classification_enum: ClassificationEnum) -> list[ClassificationDetail]:
        '''
        区分の列挙型に該当する区分明細情報リストを取得する
        :param classification_enum: ClassificationEnum: 区分の列挙型
        :return: list[ClassificationDetail]: 区分明細情報リスト
        '''
        for classification in self.classifications:
            if classification.classification_name == classification_enum.value:
                return classification.details

        raise ValueError(f"区分({classification_enum.value})に該当する区分明細情報が見つかりませんでした")

    def get_classification(self, classification_enum: ClassificationEnum, detail_number: int) -> ClassificationDetail:
        '''
        区分の列挙型と明細番号に該当する区分明細情報を取得する
        :param classification_enum: ClassificationEnum: 区分の列挙型
        :param detail_number: int: 明細番号
        :return: ClassificationDetail: 区分明細情報
        :raise ValueError: 区分明細情報が見つからない場合
        '''
        for classificationDetail in self.get_classifications(classification_enum):
            if classificationDetail.detail_number == detail_number:
                return classificationDetail

        raise ValueError(f"区分({classification_enum.value})の明細番号({detail_number})に該当する区分明細情報が見つかりませんでした")
