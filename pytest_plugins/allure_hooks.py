import pytest
import allure

from utils.helpers import nodeid_to_dir


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "teardown":

        artifacts_dir = nodeid_to_dir(item.nodeid)

        if not artifacts_dir.exists():
            return

        # Video
        for video in artifacts_dir.glob("*.webm"):

            if video.stat().st_size > 0:
                allure.attach.file(
                    video, name="Video", attachment_type=allure.attachment_type.MP4
                )

        # Screenshot
        for screenshot in artifacts_dir.glob("test-*.png"):

            allure.attach.file(
                screenshot,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

        # Trace
        trace = artifacts_dir / "trace.zip"

        if trace.exists():
            allure.attach.file(
                trace,
                name="Traces in .html => SaveAs .zip file",
                attachment_type=allure.attachment_type.HTML,
            )
