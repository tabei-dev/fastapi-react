import os
from functools import lru_cache
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def get_json_path(json_filename: str) -> str:
    '''
    JSONファイルのパスを取得します
    :param json_filename: str: JSONファイル名
    :return: str: JSONファイルのパス
    '''
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    # logger.info(f'current_file_dir: {current_file_dir}')  # デバッグ用ログ
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    json_path = os.path.join(assets_path, json_filename)
    # logger.info(f'json_path: {json_path}')  # デバッグ用ログ
    if not os.path.exists(json_path):
        raise Exception(f"JSONファイル({json_filename})が見つかりませんでした")

    return json_path
