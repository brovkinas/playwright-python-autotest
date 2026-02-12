from urllib.parse import urljoin

import allure  # noqa
from playwright.sync_api import Page, expect, Locator

from core.page_factory.page_type import PageType


class BasePage:

    PAGE_TYPE: PageType | None = None

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, url: str = ""):
        final_url = urljoin(self.base_url, url)
        with allure.step(f"Open '{final_url}'"):
            self.page.goto(final_url, wait_until="domcontentloaded", timeout=20000)
            expect(self.page).to_have_url(final_url)

    def should_have_title(self, expected_title: str):
        with allure.step(f"Expected title: '{expected_title}'"):
            expect(self.page).to_have_title(expected_title)
