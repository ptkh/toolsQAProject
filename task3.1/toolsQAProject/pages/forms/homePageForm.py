from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Button


class HomePageForm(BaseForm):
    """Categories menu on main page"""
    def __init__(self, page):
        super().__init__((By.CLASS_NAME, "banner-image", "Banner image"))
        self.homePage = page

    def click_alertsFrameWindows_button(self):
        self.homePage.alertsFrameWindowsButton.click()

    def click_elements_button(self):
        self.homePage.elementsButton.click()

    def main_page_is_open(self) -> bool:
        return self.homePage.alertsFrameWindowsButton.is_displayed()
