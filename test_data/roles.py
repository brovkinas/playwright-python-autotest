from core.enums.user_roles import UserRole
from config.credentials import (
    get_admin_credentials,
    get_user_credentials,
    Credentials,
    get_user_wrong_username,
    get_user_wrong_password,
)


def get_user(role: UserRole) -> Credentials:
    if role == UserRole.ADMIN:
        return get_admin_credentials()

    if role == UserRole.USER:
        return get_user_credentials()

    if role == UserRole.USER_WRONG_NAME:
        return get_user_wrong_username()

    if role == UserRole.USER_WRONG_PASSWORD:
        return get_user_wrong_password()

    raise ValueError(f"Unsupported role: {role}")
