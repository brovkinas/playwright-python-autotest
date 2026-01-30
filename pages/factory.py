from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage


class PagesFactory:
    """
    Мини-фабрика страниц. Возвращает объект PageObject по имени.
    ==>> Нет дублирования фикстур для каждой страницы.
    """

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.page_registry = {
            "login": LoginPage,
            "main": MainPage,
        }

    def create(self, page_name: str):
        """
        Создаёт экземпляр страницы по ключу.
        :raises KeyError: если ключ не найден
        """
        try:
            page_class = self.page_registry[page_name]

        except KeyError as exc:

            raise KeyError(
                f"Страница '{page_name}' не зарегистрирована в PagesFactory"
            ) from exc

        return page_class(self.page, self.base_url)
