'''
YAMLファイルの読み込みを行うユーティリティ
'''
import os
import yaml
from typing import Any

def __get_assets_path() -> str:
    '''
    アセットディレクトリのパスを取得します
    :return: str: アセットディレクトリのパス
    '''
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    return assets_path

def __get_yaml_path(yaml_filename: str) -> str:
    '''
    YAMLファイルのパスを取得します
    :param yaml_filename: str: YAMLファイル名
    :return: str: YAMLファイルのパス
    '''
    assets_path = __get_assets_path()
    yaml_path = os.path.join(assets_path, yaml_filename)
    if not os.path.exists(yaml_path):
        # assert False, f"YAMLファイル({yaml_filename})が見つかりませんでした"
        raise Exception(f"JSONファイル({yaml_filename})が見つかりませんでした")

    return yaml_path

def get_yaml_data(yaml_filename: str) -> dict[str, Any]:
    '''
    YAMLファイルを読み込み、YAMLデータを取得します
    :param yaml_filename: str: YAMLファイル名
    :return: dict: YAMLデータ
    '''
    yaml_path = __get_yaml_path(yaml_filename)
    with open(yaml_path) as file:
        return yaml.safe_load(file)

    # assert False, f"YAMLファイル({yaml_filename})の読み込みに失敗しました"
    raise Exception(f"YAMLファイル({yaml_filename})の読み込みに失敗しました")