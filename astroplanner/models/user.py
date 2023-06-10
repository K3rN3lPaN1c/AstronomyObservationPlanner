import re


class User:
    def __init__(self, user_id=None, username=None, password=None, email=None):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email

    @staticmethod
    def _is_valid_userid(userid: int) -> bool:
        if not isinstance(userid, int):
            return False

        if userid <= 0:
            return False

        return True

    @staticmethod
    def _is_valid_username(username: str) -> bool:
        if not isinstance(username, str):
            return False

        if not username:
            return False

        if len(username) < 3:
            return False

        if len(username) > 32:
            return False

        return True

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def _is_valid_password(password: str) -> bool:
        if len(password) < 8:
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char.isupper() for char in password):
            return False

        special_characters = "@$!%*#?&_-:"
        if not any(char in special_characters for char in password):
            return False

        return True

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value: int):
        if not self._is_valid_userid(value):
            raise TypeError("User ID must be an integer and must be a positive integer.")

        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if not self._is_valid_username(value):
            raise ValueError("Username must be a non-empty string and at least 3 and a maximum of 32 characters long.")

        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        if not self._is_valid_password(value):
            raise ValueError(
                "Password must be at least 8 characters long, contain at least one number, one uppercase letter, "
                "and one special character (@, $, !, %, *, #, ?, &).")

        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not self._is_valid_email(value):
            raise ValueError("The provided email address is invalid. Please ensure it has the format "
                             "'username@domain.com'.")

        self._email = value
