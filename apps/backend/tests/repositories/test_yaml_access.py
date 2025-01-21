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

# import pytest
# import os
# from app.repositories.yaml_access import get_yaml_data

# # テスト用のYAMLファイルのパス
# TEST_YAML_FILE = 'test.yaml'
# INVALID_YAML_FILE = 'invalid.yaml'

# # テスト用のYAMLデータ
# TEST_YAML_CONTENT = """
# key1: value1
# key2: value2
# """

# @pytest.fixture(scope='module', autouse=True)
# def setup_and_teardown():
#     # テスト用のYAMLファイルを作成
#     with open(TEST_YAML_FILE, 'w') as file:
#         file.write(TEST_YAML_CONTENT)

#     yield

#     # テスト終了後にYAMLファイルを削除
#     os.remove(TEST_YAML_FILE)

# def test_get_yaml_data_success():
#     """
#     YAMLファイルを正しく読み込んでyamlデータが正しく取得できるかを確認するテスト
#     """
#     expected_data = {
#         'key1': 'value1',
#         'key2': 'value2'
#     }
#     yaml_data = get_yaml_data(TEST_YAML_FILE)
#     assert yaml_data == expected_data

# def test_get_yaml_data_failure():
#     """
#     YAMLファイルが存在しない場合に正しくエラーが発生するかを確認するテスト
#     """
#     with pytest.raises(AssertionError) as excinfo:
#         get_yaml_data(INVALID_YAML_FILE)
#     assert f"YAMLファイル({INVALID_YAML_FILE})が見つかりませんでした" in str(excinfo.value)