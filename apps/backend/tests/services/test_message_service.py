import pytest
from app.services.message_service import message_service

def test_get_message_success():
    assert message_service.get_message('4001') == "ユーザーが見つかりません"
    assert message_service.get_message('4002') == "パスワードが一致しません"

def test_get_message_failure():
    with pytest.raises(AssertionError) as exc_info:
        number = '9999'
        message_service.get_message(number)
    assert f"メッセージ番号({number})に該当するメッセージが見つかりませんでした" in str(exc_info.value)
