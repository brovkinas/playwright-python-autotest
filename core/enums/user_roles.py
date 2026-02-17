from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    USER_WRONG_NAME = "user_wrong_username"
    USER_WRONG_PASSWORD = "user_wrong_password"
