import logging
from typing import TypeVar, Type

from pages.base_page import BasePage
from pages.page_factory.page_type import PageType
from pages.page_factory.registry import PAGE_REGISTRY

T = TypeVar("T", bound=BasePage)
logger = logging.getLogger("autotests")


def register_page(page_type: PageType):

    def decorator(cls: Type[T]) -> Type[T]:

        if not issubclass(cls, BasePage):
            raise TypeError(f"{cls.__name__} must inherit from BasePage")

        registered_cls = PAGE_REGISTRY.get(page_type)

        if registered_cls is not None and registered_cls is not cls:
            raise ValueError(
                f"{page_type} already registered by {registered_cls.__name__}"
            )

        PAGE_REGISTRY[page_type] = cls
        cls.PAGE_TYPE = page_type

        logger.debug(f"Registered page {cls.__name__} -> {page_type.name}")

        return cls

    return decorator
