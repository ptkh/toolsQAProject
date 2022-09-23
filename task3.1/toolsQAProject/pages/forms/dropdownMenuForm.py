from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from toolsQAProject.pages.forms.alertsFrameWindowsMenuForm import AlertsFrameWindowsMenu
from framework.base.elements import Button
from toolsQAProject.pages.forms.elementsMenuForm import ElementsMenu


class DropdownMenu(BaseForm):
    """Dropdown menu on sub-categories' page"""
    def __init__(self):
        super().__init__((By.CLASS_NAME, "left-pannel", "DropdownMenu"))

    @property
    def alertsFrameWindowsMenu(self):
        return AlertsFrameWindowsMenu()

    @property
    def elementsMenu(self):
        return ElementsMenu()

    @property
    def elementsButton(self):
        return Button(By.XPATH, "//*[@class='header-wrapper'][//*[text()='Elements']]", "'Elements' button")

    def click_elements_button(self):
        self.elementsButton.click()
