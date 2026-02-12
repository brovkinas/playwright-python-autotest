import allure  # noqa
from playwright.sync_api import Page

from core.enums.login_messages import LoginMessages
from core.page_elements.buton import Button
from core.page_factory.page_registrator import register_page
from core.page_factory.page_type import PageType
from core.page_elements.base_element import BaseElement
from core.page_elements.input import Input
from pages.base_page import BasePage


@register_page(PageType.LOGIN)
class LoginPage(BasePage):

    URL = "/login"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

        self.username_input = Input(page.locator("#username"), "Username input")
        self.password_input = Input(page.locator("#password"), "Password input")
        self.login_button = Button(
            page.locator("button[type='submit']"), "Login button"
        )
        self.login_flash_message = BaseElement(page.locator("#flash"), "Flash message")

    @allure.step(f"Open login page")
    def open(self):
        super().open(self.URL)

    @allure.step("Login with user: {username}")
    def login(self, username: str, password: str):
        Input.fill(self.username_input, username)
        Input.fill(self.password_input, password)
        Input.click(self.login_button)

    @allure.step("Expected Successful login message")
    def should_be_logged_in(self):
        self.login_flash_message.should_be_visible()
        self.login_flash_message.should_contain_text(
            LoginMessages.SUCCESS_LOGIN_TEXT.value
        )

    @allure.step("Expected Invalid username message")
    def should_have_invalid_username_error(self):
        self.login_flash_message.should_be_visible()
        self.login_flash_message.should_contain_text(
            LoginMessages.INVALID_USERNAME.value
        )

    @allure.step("Expected Invalid password message")
    def should_have_invalid_password_error(self):
        self.login_flash_message.should_be_visible()
        self.login_flash_message.should_contain_text(
            LoginMessages.INVALID_PASSWORD.value
        )
