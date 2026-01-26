import allure
from playwright.sync_api import Page, expect


class BasePage():
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @allure.step('Open url: {url}')
    def open(self, url: str = ''):
        self.page.goto(
            f'{self.base_url}{url}',
            wait_until='domcontentloaded',
            timeout=60000
        )

    @allure.step('Check page title contains: {expected_title}')
    def should_have_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)
