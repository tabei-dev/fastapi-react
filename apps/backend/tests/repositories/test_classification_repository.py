import os
import json
import pytest
from app.repositories.classification_repository import get_classification_details, get_classification_detail
from app.models.classification import ClassificationEnum

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

def get_classification_details_valid():
    defails = {
        ClassificationEnum.ROLE: [
            {"detail_number": 1, "detail_name": "Admin", "detail_jp_name": "管理者"},
            {"detail_number": 2, "detail_name": "User", "detail_jp_name": "ユーザー"}
        ]
    }
    assert get_classification_details(ClassificationEnum.ROLE) == defails

def get_classification_details_invalid():
    with pytest.raises(ValueError) as exc_info:
        get_classification_details("INVALID")
    assert "区分列挙型(INVALID)に該当する区分明細情報が見つかりませんでした" in str(exc_info.value)

def get_classification_detail_valid():
    detail = {"detail_number": 1, "detail_name": "Admin", "detail_jp_name": "管理者"}
    assert get_classification_detail(ClassificationEnum.ROLE, 1) == detail

def get_classification_detail_invalid():
    with pytest.raises(ValueError) as exc_info:
        get_classification_detail(ClassificationEnum.ROLE, 9999)
    assert "区分列挙型(ROLE)の区分明細情報(9999)が見つかりませんでした" in str(exc_info.value)
