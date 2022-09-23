from selenium.webdriver.common.by import By
from framework.base.elements import Button
from toolsQAProject.pages.forms.homePageForm import HomePageForm


class HomePage:
    """Page header"""
    @property
    def headerLogo(self):
        return Button(By.XPATH, "//header//img", "Header logo")
    
    @property
    def elementsButton(self):
        return Button(By.XPATH, "//div[contains(@class,'top-card')]//h5[text()='Elements']", "'Elements' button")

    @property
    def alertsFrameWindowsButton(self):
        return Button(By.XPATH, "//div[contains(@class,'top-card')]//h5[text()='Alerts, Frame & Windows']",
                      "'Alerts, Frame & Windows' button")

    @property
    def homePageForm(self):
        return HomePageForm(self)