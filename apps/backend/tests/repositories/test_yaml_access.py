import os
import pytest
from app.repositories.yaml_access import get_yaml_data

def test_get_yaml_data_valid():
    # テスト用のYAMLファイルを作成
    test_yaml_filename = "test_valid.yaml"
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
    os.makedirs(assets_path, exist_ok=True)
    test_yaml_path = os.path.join(assets_path, test_yaml_filename)
    with open(test_yaml_path, 'w') as f:
        f.write('{"key": "value"}')

    # 関数を呼び出してデータを取得
    result = get_yaml_data(test_yaml_filename)
    assert result == {"key": "value"}

    # テスト用のYAMLファイルを削除
    os.remove(test_yaml_path)

def test_get_yaml_data_invalid():
    with pytest.raises(AssertionError) as exc_info:
        get_yaml_data("non_existent.yaml")
    assert "YAMLファイル(non_existent.yaml)が見つかりませんでした" in str(exc_info.value)