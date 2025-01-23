from app.models.classification import ClassificationEnum, Classification, ClassificationDetail
from app.managers.classification_manager import create_classifications, get_classification, get_classification_detail
# from app.utils.yaml_access import get_yaml_data

class ClassificationService:
    '''
    区分情報サービス
    '''
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.__classifications = create_classifications()

    def get_classification_details(self, classification_enum: ClassificationEnum) -> dict[str, ClassificationDetail]:
        '''
        指定の区分列挙型の区分明細情報一覧を取得する
        :param classification_enum: Enum: 区分列挙型
        :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
        :raise ValueError: 区分明細情報が見つからない場合
        '''
        classification = get_classification(self.__classifications, classification_enum)
        if classification:
            return classification.details

        # assert False, f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした"
        raise ValueError(f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした")

    def get_classification_detail(self, classification_enum: ClassificationEnum, detail_number: str) -> ClassificationDetail:
        '''
        指定の区分列挙型と明細番号の区分明細情報を取得する
        :param classification_enum: Enum: 区分列挙型
        :param detail_number: str: 明細番号
        :return: ClassificationDetail: 区分明細情報
        :raise ValueError: 区分明細情報が見つからない場合
        '''
        classification_detail = get_classification_detail(self.__classifications, classification_enum, detail_number)
        if classification_detail:
            return classification_detail

        # assert False, f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした"
        raise ValueError(f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした")

classification_service = ClassificationService()