from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.utilities.driverUtil import DriverUtil


class WindowsForm(BaseForm):
    """RegistrationForm for working with windows page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Browser Windows']", "Browser Windows header"))
        self.windowsPage = page

    def click_new_tab_button(self) -> None:
        self.windowsPage.newTabButton.click()

    def sample_page_is_open(self) -> bool:
        DriverUtil.switch_to_tab(1)
        return self.windowsPage.samplePageText.is_displayed()
