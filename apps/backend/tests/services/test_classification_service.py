import os
import json
import pytest
from io import StringIO
from app.services.classification_service import classification_service

@pytest.fixture
def mock_classifications(monkeypatch):
    classifications = [
        {
            "classification_name": "Role",
            "classification_jp_name": "権限",
            "details": [
                {"detail_number": 1, "detail_name": "Administrator", "detail_jp_name": "管理者"},
                {"detail_number": 2, "detail_name": "General", "detail_jp_name": "一般"}
            ]
        }
    ]

    def mock_open(*args, **kwargs):
        if args[0].endswith('classifications.json'):
            return StringIO(json.dumps({"classifications": classifications}))
        return open(*args, **kwargs)

    monkeypatch.setattr('builtins.open', mock_open)
    monkeypatch.setattr('os.path.exists', lambda x: True)

    # classification_serviceの状態をリセット
    if hasattr(classification_service, 'initialized'):
        del classification_service.initialized
        classification_service.__init__()

    return classifications

def test_get_roles(mock_classifications):
    service = classification_service
    roles = service.get_roles()
    assert len(roles) == 2
    assert roles[0].detail_name == "Administrator"
    assert roles[1].detail_name == "General"

def test_get_role(mock_classifications):
    service = classification_service
    role = service.get_role(1)
    assert role.detail_name == "Administrator"
    role = service.get_role(2)
    assert role.detail_name == "General"

def test_get_role_not_found(mock_classifications):
    service = classification_service
    with pytest.raises(ValueError) as excinfo:
        service.get_role(999)
    assert str(excinfo.value) == "Role(999)が見つかりませんでした"