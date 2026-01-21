import pytest

from pages.main_page import MainPage


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base-url')


@pytest.fixture(scope='function')
def main_page(page, base_url):
    return MainPage(page, base_url)
