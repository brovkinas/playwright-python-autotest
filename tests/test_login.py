import allure  # noqa

from core.page_factory.page_type import PageType


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Successful Login")
def test_success_login(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.should_be_logged_in()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Login error: username")
def test_invalid_username_login(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.login("invalid-username", "SuperSecretPassword!")
    login_page.should_have_invalid_username_error()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Login error: password")
def test_invalid_password_login(pages):
    login_page = pages.create(PageType.LOGIN)
    login_page.open()
    login_page.login("tomsmith", "invalid-password")
    login_page.should_have_invalid_password_error()
