import pytest
from app.models.message import Message, get_message

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

    result = get_message(messages, number)

    assert result == ""
