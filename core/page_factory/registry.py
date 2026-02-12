from typing import Type
from pages.base_page import BasePage
from core.page_factory.page_type import PageType

PAGE_REGISTRY: dict[PageType, Type[BasePage]] = {}
