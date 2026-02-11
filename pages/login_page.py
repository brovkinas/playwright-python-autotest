import allure  # noqa

from pages.base_page import BasePage
from pages.page_factory.decorators import register_page
from pages.page_factory.page_type import PageType


@register_page(PageType.LOGIN)
class LoginPage(BasePage):

    URL = "/login"
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = 'button[type="submit"]'
    FLASH_MESSAGE = "#flash"
    SUCCESS_LOGIN_TEXT = "You logged into a secure area!"
    INVALID_USERNAME_TEXT = "Your username is invalid!"
    INVALID_PASSWORD_TEXT = "Your password is invalid!"

    @allure.step(f"Open login page")
    def open(self):
        super().open(self.URL)

    @allure.step("Login with user: {username}")
    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Expected Successful login message")
    def should_be_logged_in(self):
        super().should_be_visible(self.FLASH_MESSAGE)
        super().should_contain_text(self.FLASH_MESSAGE, self.SUCCESS_LOGIN_TEXT)

    @allure.step("Expected Invalid username message")
    def should_have_invalid_username_error(self):
        super().should_be_visible(self.FLASH_MESSAGE)
        super().should_contain_text(self.FLASH_MESSAGE, self.INVALID_USERNAME_TEXT)

    @allure.step("Expected Invalid password message")
    def should_have_invalid_password_error(self):
        super().should_be_visible(self.FLASH_MESSAGE)
        super().should_contain_text(self.FLASH_MESSAGE, self.INVALID_PASSWORD_TEXT)
