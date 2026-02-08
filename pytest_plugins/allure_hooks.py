import logging

import pytest
import allure  # noqa

from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    logger = logging.getLogger("autotests")

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        item.stash["test_failed"] = report.failed

        page = getattr(item, "page", None)
        if not page:
            return

        # page source runtime attach
        try:
            allure.attach(
                page.content(),
                name="Page source (runtime)",
                attachment_type=allure.attachment_type.HTML,
            )
        except Exception:
            logger.exception("Failed to attach page source")

        # screenshot runtime attach
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="Screenshot (runtime)",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            logger.exception("Failed to attach screenshot")

        # store pw video path on stash
        try:
            video = page.video
            if video:
                video_path = Path(video.path())
                item.stash["pw_video_dir"] = video_path.parent
        except Exception:
            logger.exception("Failed to get video path for %s", item.nodeid)
