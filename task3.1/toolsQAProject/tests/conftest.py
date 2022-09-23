from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.forms.browser import Browser
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser(pytestconfig):
    browser = Browser(pytestconfig.getoption("browser"))
    yield browser
    DriverUtil.quit_driver()
