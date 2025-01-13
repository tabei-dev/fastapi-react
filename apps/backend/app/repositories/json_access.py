import os
from functools import lru_cache

@lru_cache(maxsize=1)
def get_json_path(json_filename: str) -> str:
    '''
    JSONファイルのパスを取得します
    :param json_filename: str: JSONファイル名
    :return: str: JSONファイルのパス
    '''
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    json_path = os.path.join(assets_path, json_filename)
    if not os.path.exists(json_path):
        raise Exception(f"JSONファイル({json_filename})が見つかりませんでした")

    return json_path