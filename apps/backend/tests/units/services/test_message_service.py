import pytest
# from app.domain.value_objects.message import Message
from app.services.message_service import get_message

def test_get_message_success():
    # messages = {
    #     "1001": Message(number="1001", message="これはテストメッセージです。"),
    #     "1002": Message(number="1002", message="これは別のテストメッセージです。")
    # }
    number = "4001"
    expected_message = "ユーザーが見つかりません"

    result = get_message(number)

    assert result == expected_message

def test_get_message_not_found():
    # messages = {
    #     "1001": Message(number="1001", message="これはテストメッセージです。"),
    #     "1002": Message(number="1002", message="これは別のテストメッセージです。")
    # }
    number = "9999"

    with pytest.raises(ValueError) as exc_info:
        get_message(number)

    assert str(exc_info.value)