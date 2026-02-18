import os
from dataclasses import dataclass

ADMIN_USERNAME = "ADMIN_USERNAME"
ADMIN_PASSWORD = "ADMIN_PASSWORD"
USER_USERNAME = "USER_USERNAME"
USER_PASSWORD = "USER_PASSWORD"
USER_WRONG_USERNAME = "USER_WRONG_USERNAME"
USER_WRONG_PASSWORD = "USER_WRONG_PASSWORD"


@dataclass(frozen=True)
class Credentials:
    username: str
    password: str

    def __repr__(self) -> str:
        return f"Credentials(username='{self.username}', password='[HIDDEN]')"


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable '{name}' is not set")
    return value


def get_admin_credentials() -> Credentials:
    return Credentials(
        username=_get_env(ADMIN_USERNAME),
        password=_get_env(ADMIN_PASSWORD),
    )


def get_user_credentials() -> Credentials:
    return Credentials(
        username=_get_env(USER_USERNAME),
        password=_get_env(USER_PASSWORD),
    )


def get_user_wrong_username() -> Credentials:
    return Credentials(
        username=_get_env(USER_WRONG_USERNAME),
        password=_get_env(USER_PASSWORD),
    )


def get_user_wrong_password() -> Credentials:
    return Credentials(
        username=_get_env(USER_USERNAME),
        password=_get_env(USER_WRONG_PASSWORD),
    )
