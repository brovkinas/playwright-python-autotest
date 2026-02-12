from enum import Enum


class LoginMessages(str, Enum):
    SUCCESS_LOGIN_TEXT = "You logged into a secure area!"
    INVALID_USERNAME = "Your username is invalid!"
    INVALID_PASSWORD = "Your password is invalid!"
