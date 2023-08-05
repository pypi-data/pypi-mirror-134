import datetime
import hashlib
import uuid


class DatetimeUtils:

    @staticmethod
    def datetime_to_isoformat(date: datetime):
        return date.replace(microsecond=0, second=0).isoformat()


class HashLibUtils:

    @staticmethod
    def check_user_password(password: str, user_salt: bytes, user_key: bytes, iteration=100000) -> bool:
        pass_typed = hashlib.pbkdf2_hmac('sha256', password=password.encode('utf-8'),
                                         salt=user_salt, iterations=iteration)
        return user_key == pass_typed

    @staticmethod
    def hash_password(password: str, iteration=100000) -> dict:
        user_salt = uuid.uuid4().bytes
        user_key = hashlib.pbkdf2_hmac(hash_name='sha256', password=password.encode('utf-8'), salt=user_salt,
                                       iterations=iteration)
        return {"user_salt": user_salt, "user_key": user_key}
