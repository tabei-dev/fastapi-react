import pytest
from app.repositories.classification_repository import get_classification_details, get_classification_detail
from app.models.classification import ClassificationEnum

def get_classification_details_success():
    # 区分情報は静的データのため、実データをテストデータとして使用します
    defails = {
        ClassificationEnum.ROLE: [
            {"detail_number": '01', "detail_name": "Admin", "detail_jp_name": "管理者"},
            {"detail_number": '02', "detail_name": "User", "detail_jp_name": "ユーザー"}
        ]
    }
    assert get_classification_details(ClassificationEnum.ROLE) == defails

def get_classification_details_failure():
    with pytest.raises(AssertionError) as exc_info:
        get_classification_details("INVALID")
    # assert f"区分列挙型(INVALID)に該当する区分明細情報が見つかりませんでした" in str(exc_info.value)

def get_classification_detail_success():
    # 区分情報は静的データのため、実データをテストデータとして使用します
    detail = {"detail_number": '01', "detail_name": "Admin", "detail_jp_name": "管理者"}
    assert get_classification_detail(ClassificationEnum.ROLE, 1) == detail

def get_classification_detail_failure():
    with pytest.raises(AssertionError) as exc_info:
        get_classification_detail(ClassificationEnum.ROLE, '9999')
    # assert f"区分列挙型(ROLE)の区分明細情報(9999)が見つかりませんでした" in str(exc_info.value)
