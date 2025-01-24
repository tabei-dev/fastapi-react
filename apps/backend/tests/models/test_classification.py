import pytest
from app.models.classification import (
    ClassificationEnum,
    Classification,
    ClassificationDetail,
    get_classification,
    get_classification_detail,
)

def test_get_classification_success():
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
    expected_classification = Classification(
        classification_enum=ClassificationEnum.ROLE,
        details={
            "01": ClassificationDetail(detail_number="01", detail_name="Admin", detail_jp_name="管理者"),
            "02": ClassificationDetail(detail_number="02", detail_name="User", detail_jp_name="ユーザー")
        }
    )

    result = get_classification(classifications, classification_enum)

    assert result == expected_classification

def test_get_classification_not_found():
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

    result = get_classification(classifications, classification_enum)

    assert result == None

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

    result = get_classification_detail(classifications, classification_enum, detail_number)

    assert result == None
