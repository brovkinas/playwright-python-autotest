from playwright.sync_api import Page

from pages.page_factory.registry import PAGE_REGISTRY
from pages.page_factory.page_type import PageType


class PagesFactory:
    """
    Мини-фабрика страниц.
    Создаёт и возвращает экземпляр класса страницы,
    соответствующий переданному PageType, используя PAGE_REGISTRY.
    """

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def create(self, page_type: PageType):
        try:
            page_class = PAGE_REGISTRY[page_type]
            return page_class(self.page, self.base_url)
        except KeyError:
            raise ValueError(f'"{page_type}" не зарегистрирован в PAGE_REGISTRY')
