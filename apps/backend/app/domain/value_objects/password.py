from app.helpers.hash import verify_password

class Password:
    def __init__(self, plain_password: str, hashed_password: str):
        if not verify_password(plain_password, hashed_password):
            raise Exception("Invalid password")

        self.value = hashed_password

    def __str__(self) -> str:
        return self.value
