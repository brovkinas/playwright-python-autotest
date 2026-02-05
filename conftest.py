import allure  # noqa
import pytest
import logging

from pages.page_factory.factory import PagesFactory
from core.logger import setup_logger
from utils.helpers import nodeid_to_dir_path

pytest_plugins = ["pytest_plugins.allure_hooks", "pytest_plugins.pytest_hooks"]


@pytest.fixture(scope="session", autouse=False)
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function", autouse=False)
def pages(page, base_url):
    return PagesFactory(page, base_url)


@pytest.fixture(scope="session", autouse=True)
def session_logger():
    logger = setup_logger()
    logger.info("=== LOGGER INITIALIZED ===")

    yield

    logging.shutdown()


@pytest.fixture(scope="function", autouse=True)
def test_context(request):
    logger = logging.getLogger("autotests")
    nodeid = request.node.nodeid.replace("::", "_").replace("/", "_").replace(".", "_")

    logger.info(f"Start test: {nodeid}")

    yield

    logger.info(f"Finish test: {nodeid}")


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

    artifacts_dir = nodeid_to_dir_path(request.node)
    if not artifacts_dir.exists():
        return

    # Video attach
    for video in artifacts_dir.glob("*.webm"):
        if video.stat().st_size > 0:
            allure.attach.file(
                video, name="Video", attachment_type=allure.attachment_type.MP4
            )

    # Traces attach
    for trace in artifacts_dir.glob("*.zip"):
        if trace.exists():
            allure.attach.file(
                trace,
                name="Traces in .html => SaveAs .zip file",
                attachment_type=allure.attachment_type.HTML,
            )
