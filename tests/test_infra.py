import allure  # noqa

from pages.page_factory.page_type import PageType


@allure.epic("Infra testing")
@allure.feature("Allure attach")
@allure.story("Attach on failure")
def test_always_fails_for_attach_on_failure_check(pages):
    main_page = pages.create(PageType.MAIN)
    main_page.open()
    main_page.should_have_title()
    assert 1 == 2
