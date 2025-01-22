from app.models.classification import ClassificationEnum, Classification, ClassificationDetail
from app.utils.yaml_access import get_yaml_data

class ClassificationService:
    '''
    区分情報サービス
    '''

    def __init__(self):
        '''
        コンストラクタ
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
        self.__classifications = classifications

    def get_classification_details(self, classification_enum: ClassificationEnum) -> dict[str, ClassificationDetail]:
        '''
        指定の区分列挙型の区分明細情報一覧を取得する
        :param classification_enum: Enum: 区分列挙型
        :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
        '''
        classification = self.__classifications.get(classification_enum.value)
        if classification:
            return classification.details

        # raise ValueError(f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした")
        assert False, f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした"

    def get_classification_detail(self, classification_enum: ClassificationEnum, detail_number: str) -> ClassificationDetail:
        '''
        指定の区分列挙型と明細番号の区分明細情報を取得する
        :param classification_enum: Enum: 区分列挙型
        :param detail_number: str: 明細番号
        :return: ClassificationDetail: 区分明細情報
        '''
        classification_details = self.get_classification_details(classification_enum)
        classification_detail = classification_details.get(detail_number)
        if classification_detail:
            return classification_detail

        # raise ValueError(f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした")
        assert False, f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした"

classification_service = ClassificationService()