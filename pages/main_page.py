import allure  # noqa

from pages.base_page import BasePage
from pages.page_factory.decorators import register_page
from pages.page_factory.page_type import PageType


@register_page(PageType.MAIN)
class MainPage(BasePage):
    URL = "/"
    EXPECTED_TITLE = "The Internet"

    @allure.step("Open main page")
    def open(self):
        super().open(self.URL)

    @allure.step("Main page should have title")
    def should_have_title(self):
        super().should_have_title(self.EXPECTED_TITLE)
