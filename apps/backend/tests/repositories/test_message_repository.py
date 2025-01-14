import pytest
from app.repositories.message_repository import get_message

def test_get_message_valid():
    assert get_message('4001') == "ユーザーが見つかりません"
    assert get_message('4002') == "パスワードが一致しません"

def test_get_message_invalid():
    with pytest.raises(AssertionError) as exc_info:
        number = '9999'
        get_message(number)
    assert f"メッセージ番号({number})に該当するメッセージが見つかりませんでした" in str(exc_info.value)