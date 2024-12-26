import pytest
from app.utils.hash import Hash

def test_get_password_hash():
    password = "mysecretpassword"
    hashed_password = Hash.get_password_hash(password)

    assert hashed_password != password
    assert Hash.verify_password(password, hashed_password)

def test_verify_password():
    password = "mysecretpassword"
    hashed_password = Hash.get_password_hash(password)

    assert Hash.verify_password(password, hashed_password)
    assert not Hash.verify_password("wrongpassword", hashed_password)

if __name__ == "__main__":
    pytest.main()