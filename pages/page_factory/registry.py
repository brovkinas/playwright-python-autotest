from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.page_factory.page_type import PageType

PAGE_REGISTRY = {
    PageType.LOGIN: LoginPage,
    PageType.MAIN: MainPage,
}
