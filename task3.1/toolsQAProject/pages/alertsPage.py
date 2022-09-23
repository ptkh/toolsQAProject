from selenium.webdriver.common.by import By
from framework.base.elements import Button, Text
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.forms.alertsForm import AlertsForm


class AlertsPage:
    """RegistrationForm for working with alerts page"""
    @property
    def promptBoxWillAppearButton(self):
        return Button(By.ID, 'promtButton', "'On button click, prompt box will appear' button")

    @property
    def confirmBoxWillAppearButton(self):
        return Button(By.ID, 'confirmButton', "'On button click, confirm box will appear' button")

    @property
    def seeAlertButton(self):
        return Button(By.ID, 'alertButton', "'Click Button to see alert' button")

    @property
    def alert(self):
        return DriverUtil.get_alert()

    @property
    def confirmResult(self):
        return Text(By.ID, 'confirmResult', "'You selected Ok' text")

    @property
    def promptResult(self):
        return Text(By.ID, 'promptResult', "'You entered ...' text")

    @property
    def alertsForm(self):
        return AlertsForm(self)
