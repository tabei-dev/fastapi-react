import pytest
import os
from app.utils.yaml_access import get_yaml_data

# テスト用のYAMLファイルのパス
TEST_YAML_FILE = 'test.yaml'
INVALID_YAML_FILE = 'invalid.yaml'

# テスト用のYAMLデータ
TEST_YAML_CONTENT = """
key1: value1
key2: value2
"""

@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    # テスト用のアセットディレクトリを作成
    assets_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    # テスト用のYAMLファイルを作成
    test_yaml_path = os.path.join(assets_dir, TEST_YAML_FILE)
    with open(test_yaml_path, 'w') as file:
        file.write(TEST_YAML_CONTENT)

    yield

    # テスト終了後にYAMLファイルを削除
    os.remove(test_yaml_path)

def test_get_yaml_data_success():
    expected_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    yaml_data = get_yaml_data(TEST_YAML_FILE)
    assert yaml_data == expected_data

def test_get_yaml_data_failure():
    with pytest.raises(AssertionError) as excinfo:
        get_yaml_data(INVALID_YAML_FILE)
    assert f"YAMLファイル({INVALID_YAML_FILE})が見つかりませんでした" in str(excinfo.value)