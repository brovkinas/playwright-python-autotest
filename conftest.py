import pytest
import logging

from pages.login_page import LoginPage
from pages.main_page import MainPage
from core.logger import setup_logger

pytest_plugins = ["pytest_plugins.allure_hooks"]


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function")
def main_page(page, base_url):
    return MainPage(page, base_url)


@pytest.fixture(scope="function")
def login_page(page, base_url):
    return LoginPage(page, base_url)


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
