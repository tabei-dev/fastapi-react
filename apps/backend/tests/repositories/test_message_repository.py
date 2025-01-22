import pytest
from app.repositories.message_repository import get_message

def test_get_message_success():
    assert get_message('4001') == "ユーザーが見つかりません"
    assert get_message('4002') == "パスワードが一致しません"

def test_get_message_failure():
    with pytest.raises(AssertionError) as exc_info:
        number = '9999'
        get_message(number)
    assert f"メッセージ番号({number})に該当するメッセージが見つかりませんでした" in str(exc_info.value)

# import pytest
# from unittest.mock import patch
# from app.repositories.message_repository import get_message, __load_messages_yaml

# # テスト用のメッセージデータ
# TEST_MESSAGES = {
#     'messages': [
#         {'number': '001', 'message': 'テストメッセージ1'},
#         {'number': '002', 'message': 'テストメッセージ2'}
#     ]
# }

# @pytest.fixture
# def mock_get_yaml_data():
#     with patch('app.repositories.message_repository.get_yaml_data') as mock:
#         mock.return_value = TEST_MESSAGES
#         # キャッシュをクリア
#         __load_messages_yaml.cache_clear()
#         yield mock
#         # テスト後にキャッシュをクリア
#         __load_messages_yaml.cache_clear()

# def test_get_message_success(mock_get_yaml_data):
#     """
#     メッセージ番号に該当するメッセージが正しく取得できるかを確認するテスト
#     """
#     message = get_message('001')
#     assert message == 'テストメッセージ1'

# def test_get_message_failure(mock_get_yaml_data):
#     """
#     存在しないメッセージ番号を指定した場合に正しくエラーが発生するかを確認するテスト
#     """
#     with pytest.raises(AssertionError):
#         get_message('999')