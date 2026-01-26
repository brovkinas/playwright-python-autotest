import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = '/'
    EXPECTED_TITLE = 'The Internet'

    @allure.step('Open main page')
    def open(self):
        super().open(self.URL)

    @allure.step('Verify main page title')
    def should_have_title(self):
        super().should_have_title(self.EXPECTED_TITLE)
