import pytest
from playwright.sync_api import Playwright
from pygments.styles import default


def pytest_addoption(parser):
    parser.addoption("--br_name", action="store", default="chrome", help="browser name")

@pytest.fixture(scope="session")
def user_credentails(request):
    return request.param

@pytest.fixture
def browserInstance(playwright:Playwright, request):
    browser_name = request.config.getoption("--br_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
