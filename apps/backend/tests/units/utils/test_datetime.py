import pytest
from datetime import datetime
from app.helpers.datetime import get_now, get_now_str, from_str, to_str

def test_now():
    now = get_now()
    assert isinstance(now, datetime)
    assert now.tzinfo.key == "Asia/Tokyo"

def test_now_str():
    now_str = get_now_str()
    assert isinstance(now_str, str)
    # 現在日時の文字列が正しい形式であることを確認
    datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")

def test_from_str():
    date_str = "2023-01-01 12:00:00"
    date = from_str(date_str)
    assert isinstance(date, datetime)
    assert date == datetime(2023, 1, 1, 12, 0, 0)

def test_to_str():
    date = datetime(2023, 1, 1, 12, 0, 0)
    date_str = to_str(date)
    assert isinstance(date_str, str)
    assert date_str == "2023-01-01 12:00:00"

if __name__ == "__main__":
    pytest.main()