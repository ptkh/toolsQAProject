from selenium.webdriver.common.by import By
from framework.base.elements import Button, Text
from toolsQAProject.pages.forms.windowsForm import WindowsForm


class WindowsPage:
    """RegistrationForm for working with windows page"""
    @property
    def newTabButton(self):
        return Button(By.ID, 'tabButton', "'New Tab' button")

    @property
    def samplePageText(self):
        return Text(By.XPATH, "//h1[text()='This is a sample page']")

    @property
    def windowsForm(self):
        return WindowsForm(self)
