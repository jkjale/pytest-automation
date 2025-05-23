import pytest
from utils.browser_factory import get_browser

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    drv = get_browser(browser)
    yield drv
    drv.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
