from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.forms.browser import Browser
import pytest


@pytest.fixture
def browser():
    browser = Browser()
    yield browser
    DriverUtil.quit_driver()
