import pytest
from app.utils.hash import HashUtil

def test_get_password_hash():
    password = "mysecretpassword"
    hashed_password = HashUtil.get_hashed_password(password)

    assert hashed_password != password
    assert HashUtil.verify_password(password, hashed_password)

def test_verify_password():
    password = "mysecretpassword"
    hashed_password = HashUtil.get_hashed_password(password)

    assert HashUtil.verify_password(password, hashed_password)
    assert not HashUtil.verify_password("wrongpassword", hashed_password)

if __name__ == "__main__":
    pytest.main()