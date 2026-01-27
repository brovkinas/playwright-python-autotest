import os
import pytest
import logging

from pages.login_page import LoginPage
from pages.main_page import MainPage
from core.logger import setup_logger
from core.context import TestContext


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


@pytest.fixture(scope="function", autouse=True)
def test_context(request):
    logger = logging.getLogger(__name__)

    nodeid = request.node.nodeid.replace("::", "_").replace("/", "_").replace(".", "_")

    artifacts_dir = os.path.join("test-results", nodeid)
    os.makedirs(artifacts_dir, exist_ok=True)

    ctx = TestContext(nodeid=nodeid, artifacts_dir=artifacts_dir)

    logger.info(f"Start test: {nodeid}")

    yield ctx

    logger.info(f"Finish test: {nodeid}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)
