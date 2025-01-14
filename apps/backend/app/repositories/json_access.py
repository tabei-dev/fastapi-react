import os
import json
from functools import lru_cache
from app.config.settings import get_assets_path

@lru_cache(maxsize=1)
def __get_json_path(json_filename: str) -> str:
    '''
    JSONファイルのパスを取得します
    :param json_filename: str: JSONファイル名
    :return: str: JSONファイルのパス
    '''
    # current_file_dir = os.path.dirname(os.path.abspath(__file__))
    # assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    assets_path = get_assets_path()
    json_path = os.path.join(assets_path, json_filename)
    if not os.path.exists(json_path):
        # raise Exception(f"JSONファイル({json_filename})が見つかりませんでした")
        assert False, f"JSONファイル({json_filename})が見つかりませんでした"

    return json_path

@lru_cache(maxsize=1)
def get_json_data(json_filename: str) -> dict:
    '''
    JSONファイルを読み込み、JSONデータを取得します
    :param json_filename: str: JSONファイル名
    :return: dict: JSONデータ
    '''
    json_path = __get_json_path(json_filename)
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)

    assert False, f"JSONファイル({json_filename})の読み込みに失敗しました"