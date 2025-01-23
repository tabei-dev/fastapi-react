import pytest
from app.repositories.classification_repository import get_classification_details, get_classification_detail
from app.models.classification import ClassificationEnum, Classification, ClassificationDetail

def test_get_classification_details_success():
    classifications = {
        "Role": Classification(
            classification_enum=ClassificationEnum.ROLE,
            details={
                "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
                "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
            }
        )
    }
    classification_enum = ClassificationEnum.ROLE
    expected_details = {
        "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
        "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
    }
    
    result = get_classification_details(classifications, classification_enum)
    
    assert result == expected_details

def test_get_classification_details_not_found():
    classifications = {
        "Role": Classification(
            classification_enum=ClassificationEnum.ROLE,
            details={
                "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
                "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
            }
        )
    }
    classification_enum = ClassificationEnum.NONE
    
    with pytest.raises(AssertionError) as exc_info:
        get_classification_details(classifications, classification_enum)
    
    assert str(exc_info.value) == "区分列挙型(None)に該当する区分明細情報が見つかりませんでした"

def test_get_classification_detail_success():
    classifications = {
        "Role": Classification(
            classification_enum=ClassificationEnum.ROLE,
            details={
                "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
                "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
            }
        )
    }
    classification_enum = ClassificationEnum.ROLE
    detail_number = "01"
    expected_detail = ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者")
    
    result = get_classification_detail(classifications, classification_enum, detail_number)
    
    assert result == expected_detail

def test_get_classification_detail_not_found():
    classifications = {
        "Role": Classification(
            classification_enum=ClassificationEnum.ROLE,
            details={
                "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
                "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
            }
        )
    }
    classification_enum = ClassificationEnum.ROLE
    detail_number = "999"
    
    with pytest.raises(AssertionError) as exc_info:
        get_classification_detail(classifications, classification_enum, detail_number)
    
    assert str(exc_info.value) == "区分列挙型(Role)の区分明細情報(999)が見つかりませんでした"