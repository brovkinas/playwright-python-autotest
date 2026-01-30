import allure  # noqa
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def _fill(self, locator: str, value: str):
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        element.fill(value)

    def _click(self, locator: str):
        element = self.page.locator(locator)
        expect(element).to_be_enabled()
        element.click()

    @allure.step('Open url: {url}')
    def open(self, url: str = ''):
        self.page.goto(
            f'{self.base_url}{url}', wait_until='domcontentloaded', timeout=30000
        )

    @allure.step('Check page title contains: {expected_title}')
    def should_have_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)
