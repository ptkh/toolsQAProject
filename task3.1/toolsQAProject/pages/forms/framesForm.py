from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm


class FramesForm(BaseForm):
    """RegistrationForm for working with frames page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Frames']", "Frames header"))
        self.framesPage = page

    @property
    def upperFrameMessage(self):
        return self.framesPage.upperFrameMessage

    @property
    def lowerFrameMessage(self):
        return self.framesPage.lowerFrameMessage
