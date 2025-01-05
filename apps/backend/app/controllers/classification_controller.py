import os
import json
from enum import Enum
from app.config.settings import settings
from app.models.classification import Classification, ClassificationDetail
from app.utils.singlton import SingletonMeta

class ClassificationController(metaclass=SingletonMeta):
    '''
    区分情報コントローラークラス
    '''

    class __ClassificationEnum(Enum):
        '''
        区分の列挙型
        :param ROLE: str: 権限区分
        '''
        ROLE = 'Role'

    _instance = None

    def __new__(cls, *args, **kwargs):
        '''
        シングルトンインスタンスを生成する
        :return: ClassificationController: 区分情報コントローラー
        '''
        if cls._instance is None:
            cls._instance = super(ClassificationController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        '''
        コンストラクタ
        '''
        if not hasattr(self, 'initialized'):  # 初期化が一度だけ行われるようにする
            classifications_json_path = os.path.join(settings.assets_path, 'classifications.json')
            if os.path.exists(classifications_json_path):
                with open(classifications_json_path, 'r', encoding='utf-8') as file:
                    json_data = json.load(file)
                    self.classifications = [Classification(**classification) for classification in json_data['classifications']]
            self.initialized = True

    def get_roles(self) -> list[ClassificationDetail]:
        '''
        権限区分情報一覧を取得する
        :return: list[ClassificationDetail]: 権限区分情報一覧
        '''
        return self.__get_classification_details(self.__ClassificationEnum.ROLE)
    
    def get_role(self, detail_number: int) -> ClassificationDetail:
        '''
        指定の明細番号の権限区分情報を取得する
        :param detail_number: int: 明細番号
        :return: ClassificationDetail: 権限区分情報
        '''
        return self.__get_classification_detail(self.__ClassificationEnum.ROLE, detail_number)
    
    def __get_classification_details(self, classification_enum: Enum) -> list[ClassificationDetail]:
        '''
        指定の区分列挙型の区分明細情報一覧を取得する
        :param classification_enum: Enum: 区分列挙型
        :return: list[ClassificationDetail]: 区分明細情報一覧
        '''
        for classification in self.classifications:
            if classification.classification_name == classification_enum.value:
                return classification.details

        raise ValueError(f"{classification_enum.value}の区分明細情報一覧が見つかりませんでした")
    
    def __get_classification_detail(self, classification_enum: Enum, detail_number: int) -> ClassificationDetail:
        '''
        指定の区分列挙型と明細番号の区分明細情報を取得する
        :param classification_enum: Enum: 区分列挙型
        :param detail_number: int: 明細番号
        :return: ClassificationDetail: 区分明細情報
        '''
        classification_details = self.__get_classification_details(classification_enum)
        for classification_detail in classification_details:
            if classification_detail.detail_number == detail_number:
                return classification_detail

        raise ValueError(f"{classification_enum.value}({detail_number})が見つかりませんでした")

# インスタンスの取得
classification_controller = ClassificationController()