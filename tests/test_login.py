import allure


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Successful Login by username and password")
def test_success_login(login_page):
    login_page.open()
    login_page.login('tomsmith', 'SuperSecretPassword!')
    login_page.should_be_logged_in()


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Username Login error")
def test_invalid_username_login(login_page):
    login_page.open()
    login_page.login('tomsmithh', 'SuperSecretPassword!')
    login_page.should_have_invalid_username_error


@allure.epic("Authentication")
@allure.feature("Login by username and password")
@allure.story("Password Login error")
def test_invalid_password_login(login_page):
    login_page.open()
    login_page.login('tomsmith', 'SuperSecretPassword!!')
    login_page.should_have_invalid_password_error
