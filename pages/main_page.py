import allure  # noqa

from core.enums.page_titles import PageTitle
from pages.base_page import BasePage
from core.page_factory.page_registrator import register_page
from core.page_factory.page_type import PageType


@register_page(PageType.MAIN)
class MainPage(BasePage):

    URL = "/"

    @allure.step("Open main page")
    def open(self):
        super().open(self.URL)

    @allure.step("Main page should have title")
    def should_have_title(self):
        super().should_have_title(PageTitle.MAIN_PAGE.value)
