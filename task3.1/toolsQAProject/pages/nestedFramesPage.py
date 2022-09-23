from selenium.webdriver.common.by import By
from framework.base.elements import Text
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.forms.nestedFramesForm import NestedFramesForm


class NestedFramesPage:
    """RegistrationForm for working with frames page"""
    @property
    def parentFrame(self):
        DriverUtil.driver.switch_to.frame(DriverUtil.driver.find_element(By.XPATH, "//iframe[@id='frame1']"))
        return Text(By.XPATH, "//body", "'Parent frame' text")

    @property
    def childIframe(self):
        DriverUtil.driver.switch_to.frame(DriverUtil.driver.find_element(By.XPATH, "//iframe"))
        return Text(By.XPATH, "//p", "'Child iframe' text")

    @property
    def nestedFramesForm(self):
        return NestedFramesForm(self)
