import allure  # noqa


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Successful Login by username and password")
def test_success_login(login_page):
    try:
        login_page.open()
        login_page.login('tomsmith', 'SuperSecretPassword!')
        login_page.should_be_logged_in()
    except Exception:
        login_page.attach_page_source()
        raise


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Username Login error")
def test_invalid_username_login(login_page):
    try:
        login_page.open()
        login_page.login('tomsmithh', 'SuperSecretPassword!')
        login_page.should_have_invalid_username_error()
    except Exception:
        login_page.attach_page_source()
        raise


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Password Login error")
def test_invalid_password_login(login_page):
    try:
        login_page.open()
        login_page.login('tomsmith', 'SuperSecretPassword!')
        login_page.should_have_invalid_password_error()
    except Exception:
        login_page.attach_page_source()
        raise
