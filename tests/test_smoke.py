import allure  # noqa

from pages.page_factory.page_type import PageType


@allure.epic("SmokeTest")
@allure.feature("MainPage")
def test_open_main_page(pages):
    main_page = pages.create(PageType.MAIN)
    main_page.open()
    main_page.should_have_title()
