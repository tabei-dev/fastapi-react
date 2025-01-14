import os
import yaml
from functools import lru_cache
from app.config.settings import get_assets_path

@lru_cache(maxsize=1)
def __get_yaml_path(yaml_filename: str) -> str:
    '''
    YAMLファイルのパスを取得します
    :param yaml_filename: str: YAMLファイル名
    :return: str: YAMLファイルのパス
    '''
    # current_file_dir = os.path.dirname(os.path.abspath(__file__))
    # assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    assets_path = get_assets_path()
    yaml_path = os.path.join(assets_path, yaml_filename)
    if not os.path.exists(yaml_path):
        # raise Exception(f"JSONファイル({json_filename})が見つかりませんでした")
        assert False, f"YAMLファイル({yaml_filename})が見つかりませんでした"

    return yaml_path

@lru_cache(maxsize=1)
def get_yaml_data(yaml_filename: str) -> dict:
    '''
    YAMLファイルを読み込み、JSONデータを取得します
    :param yaml_filename: str: YAMLファイル名
    :return: dict: YAMLデータ
    '''
    yaml_path = __get_yaml_path(yaml_filename)
    with open(yaml_path) as file:
        return yaml.safe_load(file)

    assert False, f"YAMLファイル({yaml_filename})の読み込みに失敗しました"