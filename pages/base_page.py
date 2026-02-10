import logging
from time import sleep

from typing import Callable
from urllib.parse import urljoin
from playwright.sync_api import Page, expect
from pages.page_factory.page_type import PageType


class BasePage:

    PAGE_TYPE: PageType | None = None
    logger = logging.getLogger("autotests")

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, url: str = ""):
        final_url = urljoin(self.base_url, url)
        self.page.goto(final_url, wait_until="domcontentloaded", timeout=30000)
        expect(self.page).to_have_url(final_url)

    # *** Retry *** #
    def retry(self, action: Callable, retries: int = 2, delay: float = 1.0):
        last_error = None

        for attempt in range(retries + 1):
            try:
                return action()
            except Exception as e:
                last_error = e
                self.logger.warning(f"Attempt {attempt + 1}/{retries + 1} failed: {e}")
                sleep(delay)

        raise last_error

    # *** Locator helpers *** #
    def element(self, locator: str):
        return self.page.locator(locator)

    def all_elements(self, locator: str):
        pass

    def first_element(self, locator: str):
        pass

    # *** Waits *** #
    def wait_element_visible_and_enabled(self, locator: str):
        element = self.element(locator)
        expect(element).to_be_visible()
        expect(element).to_be_enabled()
        return element

    # *** Assertions *** #
    def should_be_visible(self, locator: str):
        expect(self.element(locator)).to_be_visible()

    def should_not_be_visible(self, locator: str):
        expect(self.element(locator)).not_to_be_visible()

    def should_be_enabled(self, locator: str):
        expect(self.element(locator)).to_be_enabled()

    def should_not_be_enabled(self, locator: str):
        expect(self.element(locator)).not_to_be_enabled()

    def should_contain_text(self, locator: str, text: str):
        expect(self.element(locator)).to_contain_text(text)

    def should_have_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    # *** Safe actions *** #
    def safe_click(self, locator: str):
        def action():
            element = self.wait_element_visible_and_enabled(locator)
            element.scroll_into_view_if_needed()
            element.click()

        self.retry(action)

    def safe_fill(self, locator: str, value: str):
        def action():
            element = self.wait_element_visible_and_enabled(locator)
            element.scroll_into_view_if_needed()
            element.fill(value)

        self.retry(action)

    def safe_hover(self, locator: str):
        pass

    def safe_double_click(self, locator: str):
        pass

    def safe_check(self, locator: str):
        pass

    def safe_uncheck(self, locator: str):
        pass

    def safe_select_option(self, locator: str, option: str):
        pass
