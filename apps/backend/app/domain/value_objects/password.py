from app.errors.validation_error import ValidationError
from app.helpers.hash import verify_password
from app.usecases.message_usecase import get_message

class Password:
    def __init__(self, plain_password: str, hashed_password: str):
        if not verify_password(plain_password, hashed_password):
            raise ValidationError(get_message('4002'), 'password')

        self.value = hashed_password