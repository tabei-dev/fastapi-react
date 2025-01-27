import pytest
from app.helpers.hash import to_hashed_password, verify_password

def test_get_password_hash():
    password = "mysecretpassword"
    hashed_password = to_hashed_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password)

def test_verify_password():
    password = "mysecretpassword"
    hashed_password = to_hashed_password(password)

    assert verify_password(password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)
