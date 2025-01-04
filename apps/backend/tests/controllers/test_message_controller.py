import os
import json
import pytest
from io import StringIO
from app.controllers.message_controller import message_controller

@pytest.fixture
def mock_messages(monkeypatch):
    messages = [
        {"number": 1, "message": "Test message 1"},
        {"number": 2, "message": "Test message 2"},
        {"number": 3, "message": "Test message 3"},
    ]

    def mock_open(*args, **kwargs):
        if args[0].endswith('messages.json'):
            return StringIO(json.dumps({"messages": messages}))
        return open(*args, **kwargs)

    monkeypatch.setattr('builtins.open', mock_open)
    monkeypatch.setattr('os.path.exists', lambda x: True)

    # message_controllerの状態をリセット
    if hasattr(message_controller, 'initialized'):
        del message_controller.initialized
        message_controller.__init__()

    return messages

def test_get_message(mock_messages):
    controller = message_controller
    assert controller.get_message(1) == "Test message 1"
    assert controller.get_message(2) == "Test message 2"
    assert controller.get_message(3) == "Test message 3"

def test_get_message_not_found(mock_messages):
    controller = message_controller
    with pytest.raises(ValueError) as excinfo:
        controller.get_message(999)
    assert str(excinfo.value) == "メッセージ番号(999)に該当するメッセージが見つかりませんでした"