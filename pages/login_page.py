import allure

from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = '/login'
    USERNAME_INPUT = '#username'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = 'button[type="submit"]'
    FLASH_MESSAGE = '#flash'
    SUCCESS_LOGIN_TEXT = 'You logged into a secure area!'
    INVALID_USERNAME_TEXT = 'Your username is invalid!'
    INVALID_PASSWORD_TEXT = 'Your password is invalid!'

    @allure.step('Open login page')
    def open(self):
        super().open(self.URL)
        expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible()

    @allure.step('Login with username: {username} and password: {password}')
    def login(self, username: str, password: str):
        self._fill(self.USERNAME_INPUT, username)
        self._fill(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)

    @allure.step('Expected Successful login message')
    def should_be_logged_in(self):
        expect(self.page.locator(self.FLASH_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.FLASH_MESSAGE)).to_contain_text(
            self.SUCCESS_LOGIN_TEXT
        )

    @allure.step('Expected Invalid username message')
    def should_have_invalid_username_error(self):
        expect(self.page.locator(self.FLASH_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.FLASH_MESSAGE)).to_contain_text(
            self.INVALID_USERNAME_TEXT
        )

    @allure.step('Expected Invalid password message')
    def should_have_invalid_password_error(self):
        expect(self.page.locator(self.FLASH_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.FLASH_MESSAGE)).to_contain_text(
            self.INVALID_PASSWORD_TEXT
        )
