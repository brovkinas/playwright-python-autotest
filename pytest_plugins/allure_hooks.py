import pytest
import allure  # noqa
import logging

from utils.helpers import nodeid_to_dir_path

logger = logging.getLogger("autotests")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':

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

    if report.when == "teardown":

        artifacts_dir = nodeid_to_dir_path(item)

        if not artifacts_dir.exists():
            return

        # Video teardown attach
        for video in artifacts_dir.glob("*.webm"):

            if video.stat().st_size > 0:
                allure.attach.file(
                    video, name="Video", attachment_type=allure.attachment_type.MP4
                )

        # Traces teardown attach
        for trace in artifacts_dir.glob("*.zip"):
            if trace.exists():
                allure.attach.file(
                    trace,
                    name="Traces in .html => SaveAs .zip file",
                    attachment_type=allure.attachment_type.HTML,
                )
