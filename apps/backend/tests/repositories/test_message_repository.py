import os
import json
import pytest
from app.repositories.message_repository import get_message, __load_messages_json
from app.models.message import Message

# @pytest.fixture(scope="module", autouse=True)
# def setup_messages():
#     # テスト用のJSONファイルを作成
#     test_json_filename = "test_messages.json"
#     current_file_dir = os.path.dirname(os.path.abspath(__file__))
#     assets_path = os.path.join(current_file_dir, '..', '..', 'assets')
#     os.makedirs(assets_path, exist_ok=True)
#     test_json_path = os.path.join(assets_path, test_json_filename)
#     test_data = {
#         "messages": [
#             {"number": 1, "message": "Test message 1"},
#             {"number": 2, "message": "Test message 2"}
#         ]
#     }
#     with open(test_json_path, 'w') as f:
#         json.dump(test_data, f)

#     # メッセージをロード
#     __load_messages_json.cache_clear()
#     global _messages
#     _messages = __load_messages_json()

#     yield

#     # テスト用のJSONファイルを削除
#     os.remove(test_json_path)

def test_get_message_valid():
    assert get_message(4001) == "ユーザーが見つかりません"
    assert get_message(4002) == "パスワードが一致しません"

def test_get_message_invalid():
    with pytest.raises(ValueError) as exc_info:
        get_message(9999)
    assert "メッセージ番号(9999)に該当するメッセージが見つかりませんでした" in str(exc_info.value)