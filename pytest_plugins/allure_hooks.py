import pytest
import allure  # noqa
import logging

logger = logging.getLogger("autotests")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        item.stash["test_failed"] = report.failed

        page = getattr(item, "page", None)

        if not page:
            return

        # page source runtime attach
        allure.attach(
            page.content(),
            name="Page source (runtime)",
            attachment_type=allure.attachment_type.HTML,
        )

        # screenshot runtime attach
        allure.attach(
            page.screenshot(),
            name="Screenshot (runtime)",
            attachment_type=allure.attachment_type.PNG,
        )
