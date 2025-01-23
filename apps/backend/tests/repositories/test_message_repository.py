import pytest
from app.repositories.message_repository import get_message
from app.models.message import Message

def test_get_message_success():
    messages = {
        "1001": Message(number="1001", message="これはテストメッセージです。"),
        "1002": Message(number="1002", message="これは別のテストメッセージです。")
    }
    number = "1001"
    expected_message = "これはテストメッセージです。"
    
    result = get_message(messages, number)
    
    assert result == expected_message

def test_get_message_not_found():
    messages = {
        "1001": Message(number="1001", message="これはテストメッセージです。"),
        "1002": Message(number="1002", message="これは別のテストメッセージです。")
    }
    number = "9999"
    
    with pytest.raises(AssertionError) as exc_info:
        get_message(messages, number)
    
    assert str(exc_info.value) == "メッセージ番号(9999)に該当するメッセージが見つかりませんでした"