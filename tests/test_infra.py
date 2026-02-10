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


@allure.epic("Infra testing")
@allure.feature("Page_auto_discovery")
@allure.story("Autoimport fo page object registration")
def test_pages_should_be_registered():
    from pages.page_factory.registry import PAGE_REGISTRY

    assert PAGE_REGISTRY, "No pages registered"
