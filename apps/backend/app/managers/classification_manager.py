from app.models.classification import ClassificationEnum, Classification, ClassificationDetail
from app.utils.yaml_access import get_yaml_data

def create_classifications() -> dict[str, Classification]:
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

def get_classification(
        classifications: dict[str, Classification],
        classification_enum: ClassificationEnum
    ) -> Classification | None:
    '''
    指定の区分列挙型の区分情報を取得する
    :param classifications: dict[str, Classification]: 区分情報辞書
    :param classification_enum: Enum: 区分列挙型
    :return: Classification | None: 区分情報
    '''
    return classifications.get(classification_enum.value)

def get_classification_detail(
        classifications: dict[str, Classification],
        classification_enum: ClassificationEnum, detail_number: str
    ) -> ClassificationDetail | None:
    '''
    指定の区分列挙型と明細番号の区分明細情報を取得する
    :param classifications: dict[str, Classification]: 区分情報辞書
    :param classification_enum: Enum: 区分列挙型
    :param detail_number: str: 明細番号
    :return: ClassificationDetail: 区分明細情報
    '''
    classification = get_classification(classifications, classification_enum)
    if classification:
        return classification.details.get(detail_number)

    return None
