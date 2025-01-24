import pytest
from app.managers.classification_manager import get_classification_details, get_classification_detail
from app.models.classification import ClassificationEnum, ClassificationDetail

def test_get_classification_success():
    classification_enum = ClassificationEnum.ROLE
    classification_details = {
        "00": ClassificationDetail(detail_number="00", detail_name="ADMIN", detail_jp_name="管理者"),
        "01": ClassificationDetail(detail_number="01", detail_name="USER", detail_jp_name="ユーザー")
    }

    result = get_classification_details(classification_enum)

    assert result == classification_details

def test_get_classification_not_found():
    classification_enum = ClassificationEnum.NONE

    with pytest.raises(ValueError) as exc_info:
        get_classification_details(classification_enum)

    assert str(exc_info.value) == f"区分列挙型(NONE)に該当する区分明細情報が見つかりませんでした"

def test_get_classification_detail_success():
    classification_enum = ClassificationEnum.ROLE
    detail_number = "00"
    expected_detail = ClassificationDetail(detail_number="00", detail_name="ADMIN", detail_jp_name="管理者")

    result = get_classification_detail(classification_enum, detail_number)

    assert result == expected_detail

def test_get_classification_detail_not_found():
    classification_enum = ClassificationEnum.ROLE
    detail_number = "999"

    with pytest.raises(ValueError) as exc_info:
        get_classification_detail(classification_enum, detail_number)

    assert str(exc_info.value) == f"区分列挙型(ROLE)の区分明細情報(999)が見つかりませんでした"
