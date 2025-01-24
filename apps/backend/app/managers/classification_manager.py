from app.models.classification import (
    ClassificationEnum,
    Classification,
    ClassificationDetail,
)
from app.utils.yaml_reader import get_yaml_data
from app.models.classification import ClassificationEnum

class ClassificationManager:
    '''
    区分情報マネージャ
    '''
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.__classifications = self.__create_classifications()

    def __create_classifications(self) -> dict[str, Classification]:
        '''
        区分情報を生成します
        :return: dict[str, Classification]: 区分辞書
        '''
        yaml_data = get_yaml_data('classifications.yaml')
        classifications = {}
        for classification in yaml_data['classifications']:
            classification_name = ClassificationEnum[classification['classification_name']]
            details = {
                detail['detail_number']: ClassificationDetail(
                    detail_number=detail['detail_number'],
                    detail_name=detail['detail_name'],
                    detail_jp_name=detail['detail_jp_name']
                )
                for detail in classification['details']
            }
            classifications[classification_name] = Classification(
                classification_enum=classification_name,
                details=details
            )

        return classifications

    def get_classification(self, classification_enum: ClassificationEnum) -> Classification | None:
        '''
        指定の区分列挙型の区分情報を取得する
        :param classifications: dict[str, Classification]: 区分情報辞書
        :param classification_enum: Enum: 区分列挙型
        :return: Classification | None: 区分情報
        '''
        return self.__classifications.get(classification_enum)

__classification_manager = ClassificationManager()

def get_classification_details(classification_enum: ClassificationEnum) -> dict[str, ClassificationDetail]:
    '''
    指定の区分列挙型の区分明細情報一覧を取得する
    :param classification_enum: Enum: 区分列挙型
    :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
    :raise ValueError: 区分明細情報が見つからない場合
    '''
    classification = __classification_manager.get_classification(classification_enum)
    if classification:
        return classification.details

    raise ValueError(f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした")

def get_classification_detail(classification_enum: ClassificationEnum, detail_number: str) -> ClassificationDetail:
    '''
    指定の区分列挙型と明細番号の区分明細情報を取得する
    :param classification_enum: Enum: 区分列挙型
    :param detail_number: str: 明細番号
    :return: ClassificationDetail: 区分明細情報
    :raise ValueError: 区分明細情報が見つからない場合
    '''
    classification_details = get_classification_details(classification_enum)
    detail = classification_details.get(detail_number)
    if detail:
        return detail

    raise ValueError(f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした")
