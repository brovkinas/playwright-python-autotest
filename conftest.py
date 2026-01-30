import pytest
import logging

from pages.factory import PagesFactory
from core.logger import setup_logger

pytest_plugins = ["pytest_plugins.allure_hooks"]


@pytest.fixture(scope="session")
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
