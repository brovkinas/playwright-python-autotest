from urllib.parse import urljoin

import allure
from playwright.sync_api import Page, expect, Locator

from pages.page_factory.page_type import PageType


class BasePage:

    PAGE_TYPE: PageType | None = None

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @allure.step("Open url: {url}")
    def open(self, url: str = ""):
        final_url = urljoin(self.base_url, url)

        self.page.goto(final_url, wait_until="domcontentloaded", timeout=20000)

        expect(self.page).to_have_url(final_url)

    # ===== Locators ===== #
    def element(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def first_element(self, locator: str) -> Locator:
        return self.page.locator(locator).first

    def all_elements(self, locator: str) -> Locator:
        return self.page.locator(locator)

    # ===== Assertions ===== #
    @allure.step("Element {locator} should be visible")
    def should_be_visible(self, locator: str):
        expect(self.element(locator)).to_be_visible()

    @allure.step("Element {locator} should NOT be visible")
    def should_not_be_visible(self, locator: str):
        expect(self.element(locator)).not_to_be_visible()

    @allure.step("Element {locator} should be enabled")
    def should_be_enabled(self, locator: str):
        expect(self.element(locator)).to_be_enabled()

    @allure.step("Element {locator} should NOT be enabled")
    def should_not_be_enabled(self, locator: str):
        expect(self.element(locator)).not_to_be_enabled()

    @allure.step("Element {locator} should have text {text}")
    def should_contain_text(self, locator: str, text: str):
        expect(self.element(locator)).to_contain_text(text)

    @allure.step("Expected title: {expected_title}")
    def should_have_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    # ===== Actions ===== #
    @allure.step("Click element: {locator}")
    def click(self, locator: str):
        self.element(locator).click()

    @allure.step("Fill element {locator} with value {value}")
    def fill(self, locator: str, value: str):
        self.element(locator).fill(value)

    @allure.step("Hover over element: {locator}")
    def hover(self, locator: str):
        self.element(locator).hover()

    @allure.step("Double click element: {locator}")
    def double_click(self, locator: str):
        self.element(locator).dblclick()

    @allure.step("Check checkbox: {locator}")
    def check(self, locator: str):
        self.element(locator).check()

    @allure.step("Uncheck checkbox: {locator}")
    def uncheck(self, locator: str):
        self.element(locator).uncheck()

    @allure.step("Select option {option} in {locator}")
    def select_option(self, locator: str, option: str):
        self.element(locator).select_option(option)
