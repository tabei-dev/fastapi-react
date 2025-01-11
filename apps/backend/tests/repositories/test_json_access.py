import os
import pytest
from apps.backend.app.repositories.json_access import get_json_path

def test_get_json_path_valid():
    # テスト用のJSONファイルを作成
    test_json_filename = "test_valid.json"
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    os.makedirs(assets_path, exist_ok=True)
    test_json_path = os.path.join(assets_path, test_json_filename)
    with open(test_json_path, 'w') as f:
        f.write('{}')

    # 関数を呼び出してパスを取得
    result = get_json_path(test_json_filename)
    assert os.path.abspath(result) == os.path.abspath(test_json_path)

    # テスト用のJSONファイルを削除
    os.remove(test_json_path)

def test_get_json_path_invalid():
    with pytest.raises(Exception) as exc_info:
        get_json_path("non_existent.json")
    assert "JSONファイル(non_existent.json)が見つかりませんでした" in str(exc_info.value)