import allure  # noqa


@allure.epic("SmokeTest")
@allure.feature("MainPage")
def test_open_main_page(pages):
    main_page = pages.create("main")
    main_page.open()
    main_page.should_have_title()
