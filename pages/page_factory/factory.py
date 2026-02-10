from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.page_factory.registry import PAGE_REGISTRY
from pages.page_factory.page_type import PageType


class PagesFactory:

    def __init__(self, page: Page, base_url: str):

        self.page = page
        self.base_url = base_url

    def create(self, page_type: PageType) -> BasePage:

        page_cls = PAGE_REGISTRY.get(page_type)

        if page_cls is None:
            raise ValueError(f"PageType {page_type.name} not registered")

        return page_cls(self.page, self.base_url)
