from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Button


class Header(BaseForm):
    """Page header"""
    def __init__(self):
        super().__init__((By.XPATH, "//header//img", "Header logo"))

    @property
    def headerLogo(self):
        return Button(By.XPATH, "//header//img", "Header logo")

    def click_logo(self):
        self.headerLogo.click()
