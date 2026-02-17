import allure  # noqa

from core.page_factory.page_type import PageType
from core.enums.user_roles import UserRole
from test_data.roles import get_user


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Successful Login by Admin")
def test_success_login_admin(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.user_login(get_user(UserRole.ADMIN))
    login_page.should_be_logged_in()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Successful Login by common User")
def test_success_login_user(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.user_login(get_user(UserRole.USER))
    login_page.should_be_logged_in()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Login error: username")
def test_invalid_username_login(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.user_login(get_user(UserRole.USER_WRONG_NAME))
    login_page.should_have_invalid_username_error()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Login error: password")
def test_invalid_password_login(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.user_login(get_user(UserRole.USER_WRONG_PASSWORD))
    login_page.should_have_invalid_password_error()
