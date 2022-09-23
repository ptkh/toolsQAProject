from selenium.webdriver.common.by import By
from framework.base.elements import Text
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.forms.framesForm import FramesForm


class FramesPage:
    """RegistrationForm for working with frames page"""
    @property
    def upperFrameMessage(self):
        DriverUtil.driver.switch_to.frame(DriverUtil.driver.find_element(By.ID, 'frame1'))
        return Text(By.ID, 'sampleHeading').text

    @property
    def lowerFrameMessage(self):
        DriverUtil.driver.switch_to.parent_frame()
        DriverUtil.driver.switch_to.frame(DriverUtil.driver.find_element(By.ID, 'frame2'))
        return Text(By.ID, 'sampleHeading').text

    @property
    def framesForm(self):
        return FramesForm(self)
