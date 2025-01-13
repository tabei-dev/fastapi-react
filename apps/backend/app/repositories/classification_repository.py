'''
区分情報リポジトリ
'''
import json
from enum import Enum
from functools import lru_cache
from app.models.classification import ClassificationEnum, Classification, ClassificationDetail
from app.repositories.json_access import get_json_path

@lru_cache(maxsize=1)
def __load_classifications_json() -> dict[ClassificationEnum, Classification]:
    '''
    classifications.jsonを読み込み、区分一覧を取得します
    :return: dict[ClassificationEnum, Classification]: 区分辞書
    '''
    classifications_json_path = get_json_path('classifications.json')
    with open(classifications_json_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        classifications = {}
        for classification in json_data['classifications']:
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

__classifications = __load_classifications_json()

def get_classification_details(classification_enum: Enum) -> dict[int, ClassificationDetail]:
    '''
    指定の区分列挙型の区分明細情報一覧を取得する
    :param classification_enum: Enum: 区分列挙型
    :return: dict[ClassificationEnum, ClassificationDetail]: 区分明細情報辞書
    '''
    classification = __classifications.get(classification_enum.value)
    if classification:
        return classification.details

    raise ValueError(f"区分列挙型({classification_enum.value})に該当する区分明細情報が見つかりませんでした")

def get_classification_detail(classification_enum: Enum, detail_number: int) -> ClassificationDetail:
    '''
    指定の区分列挙型と明細番号の区分明細情報を取得する
    :param classification_enum: Enum: 区分列挙型
    :param detail_number: int: 明細番号
    :return: ClassificationDetail: 区分明細情報
    '''
    classification_details = get_classification_details(classification_enum)
    classification_detail = classification_details.get(detail_number)
    if classification_detail:
        return classification_detail

    raise ValueError(f"区分列挙型({classification_enum.value})の区分明細情報({detail_number})が見つかりませんでした")
