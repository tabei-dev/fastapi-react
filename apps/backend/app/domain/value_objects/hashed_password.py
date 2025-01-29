from app.helpers.hash import verify_password

class HashedPassword:
    def __init__(self, plain_password: str, hashed_password: str):
        if not verify_password(plain_password, hashed_password):
            raise Exception("Invalid password")

        self.hashed_password = hashed_password

    def __str__(self) -> str:
        return self.hashed_password
