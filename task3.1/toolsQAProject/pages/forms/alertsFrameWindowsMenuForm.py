from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Button
from toolsQAProject.pages.alertsPage import AlertsPage
from toolsQAProject.pages.framesPage import FramesPage
from toolsQAProject.pages.nestedFramesPage import NestedFramesPage
from toolsQAProject.pages.windowsPage import WindowsPage


class AlertsFrameWindowsMenu(BaseForm):
    """RegistrationForm for working with alerts, frame and windows page"""
    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Alerts, Frame & Windows']", "Alerts, Frame & Windows Menu"))

    @property
    def alertsPage(self):
        return AlertsPage()

    @property
    def alertsButton(self):
        return Button(By.XPATH, "//span[text()='Alerts']", "'Alerts' button")

    @property
    def nestedFramesButton(self):
        return Button(By.XPATH, "//span[text()='Nested Frames']", "'Nested Frames' button")

    @property
    def framesButton(self):
        self.driver.switch_to.default_content()
        return Button(By.XPATH, "//span[text()='Frames']", "'Frames' button")

    @property
    def browserWindowsButton(self):
        return Button(By.XPATH, "//span[text()='Browser Windows']", "'Browser Windows' button")

    @property
    def nestedFramesPage(self):
        return NestedFramesPage()

    @property
    def framesPage(self):
        return FramesPage()

    @property
    def windowsPage(self):
        return WindowsPage()

    def click_alerts_button(self) -> None:
        self.alertsButton.click()

    def click_nested_frames_button(self) -> None:
        self.nestedFramesButton.click()

    def click_frames_button(self) -> None:
        self.framesButton.click()

    def click_browser_windows_button(self) -> None:
        self.browserWindowsButton.click()

