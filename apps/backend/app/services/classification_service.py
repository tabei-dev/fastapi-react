from app.domain.value_objects.classification import ClassificationEnum, Classification
from app.domain.value_objects.classification_detail import ClassificationDetail
from app.helpers.yaml import get_yaml_data

__yaml_data = get_yaml_data('classifications.yaml')
__classifications = {}
for classification in __yaml_data['classifications']:
    classification_name = ClassificationEnum[classification['classification_name']]
    details = {
        detail['detail_number']: ClassificationDetail(
            detail_number=detail['detail_number'],
            detail_name=detail['detail_name'],
            detail_jp_name=detail['detail_jp_name']
        )
        for detail in classification['details']
    }
    __classifications[classification_name] = Classification(
        classification_enum=classification_name,
        details=details
    )

def get_classification_details(classification_enum: ClassificationEnum) -> dict[str, ClassificationDetail]:
    '''
    指定の区分列挙型の区分明細情報一覧を取得する
    :param classification_enum: Enum: 区分列挙型
    :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
    :raise ValueError: 区分明細情報が見つからない場合
    '''
    classification: Classification | None = __classifications.get(classification_enum)
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