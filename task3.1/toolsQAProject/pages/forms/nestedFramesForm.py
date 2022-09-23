from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm


class NestedFramesForm(BaseForm):
    """RegistrationForm for working with frames page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Nested Frames']", "Nested Frames header"))
        self.nestedFramesPage = page

    def parent_frame_is_displayed(self) -> bool:
        return self.nestedFramesPage.parentFrame.is_displayed()

    def child_iframe_is_displayed(self) -> bool:
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(self.driver.find_element(By.ID, 'frame1'))
        return self.nestedFramesPage.childIframe.is_displayed()
