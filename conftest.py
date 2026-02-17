import re

import allure  # noqa
import pytest
import logging

from dotenv import load_dotenv

from core.page_factory.factory import PagesFactory
from core.logger import setup_logger
from utils.helpers import get_pw_artifacts_dir
from core.page_factory.auto_discovery import auto_discover_pages

pytest_plugins = ["pytest_plugins.allure_hooks", "pytest_plugins.pytest_hooks"]


# ========== Session scope fixtures ========== #
@pytest.fixture(scope="session", autouse=True)
def init_pages():
    auto_discover_pages()


@pytest.fixture(scope="session", autouse=True)
def init_dotenv():
    load_dotenv()


@pytest.fixture(scope="session", autouse=False)
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session", autouse=True)
def session_logger():
    logger = setup_logger()
    logger.info("=== LOGGER INITIALIZED ===")

    yield

    logging.shutdown()


# ========== Function scope fixtures ========== #
@pytest.fixture(scope="function", autouse=False)
def pages(page, base_url):
    return PagesFactory(page, base_url)


@pytest.fixture(scope="function", autouse=True)
def test_context(request):
    logger = logging.getLogger("autotests")
    nodeid = request.node.nodeid
    nodeid_clear = re.sub(r"[^a-zA-Z0-9]+", "-", nodeid).strip("-")

    logger.info(f"Start test: {nodeid_clear}")

    yield

    logger.info(f"Finish test: {nodeid_clear}")


@pytest.fixture(scope="function", autouse=True)
def bind_page(request, page):

    request.node.page = page

    yield


@pytest.fixture(scope="function", autouse=True)
def allure_attach_on_failure(request):

    yield

    failed = request.node.stash.get("test_failed", False)
    if not failed:
        return

    pw_video_dir = request.node.stash.get("pw_video_dir", False)
    if not pw_video_dir:
        return

    # Video attach
    for video in pw_video_dir.glob("*.webm"):
        if video.stat().st_size > 0:
            allure.attach.file(
                video, name="Video", attachment_type=allure.attachment_type.MP4
            )

    # Trace attach
    aftifacts_dir = get_pw_artifacts_dir(request)

    for trace in aftifacts_dir.glob("*.zip"):
        if trace.stat().st_size > 0:
            allure.attach.file(
                trace,
                name="Trace in .html => SaveAs .zip",
                attachment_type=allure.attachment_type.HTML,
            )


@pytest.fixture(scope="function", autouse=True)
def page_events_logger(request, page):
    """
    Includes Playwright events into global logger.
    - console.log
    - network request/response
    - page errors
    """
    logger = logging.getLogger("autotests")

    def handle_console(msg):
        msg_type = msg.type
        text = msg.text
        if msg_type in ("log", "debug", "info"):
            logger.info(f"JS CONSOLE ({msg_type}): {text}")
        elif msg_type == "warning":
            logger.warning(f"JS CONSOLE ({msg_type}): {text}")
        elif msg_type == "error":
            logger.error(f"JS CONSOLE ({msg_type}): {text}")
        else:
            logger.info(f"JS CONSOLE ({msg_type}): {text}")

    page.on("console", handle_console)

    # Network events
    page.on("request", lambda r: logger.info(f"REQ: {r.method} {r.url}"))
    page.on("response", lambda r: logger.info(f"RES: {r.status} {r.url}"))

    # Page errors
    page.on("pageerror", lambda e: logger.error(f"PAGE ERROR: {e}"))

    yield
