from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm


class AlertsForm(BaseForm):
    """RegistrationForm for working with alerts page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Alerts']", "Alerts header"))
        self.alertsPage = page

    def click_see_alerts_button(self) -> None:
        self.alertsPage.seeAlertButton.click()

    def click_confirm_box_will_appear_button(self) -> None:
        self.alertsPage.confirmBoxWillAppearButton.click()

    def click_prompt_box_will_appear_button(self) -> None:
        self.alertsPage.promptBoxWillAppearButton.click()

    def alert_is_open(self, text) -> bool:
        try:
            return self.alertsPage.alert.text == text
        except NoAlertPresentException as e:
            return False

    def alert_is_closed(self) -> bool:
        try:
            return "" not in self.alertsPage.alert.text
        except NoAlertPresentException:
            return True

    def click_OK_on_alert(self) -> None:
        """Clicks on OK button on alert box"""
        self.event_listener.before_click("Alert", self.driver)
        self.alertsPage.alert.accept()

    def enter_text_in_alert(self, text) -> None:
        """Sends keys to alert prompt"""
        self.event_listener.before_change_value_of("Alert text", self.driver)
        self.alertsPage.alert.send_keys(text)
        self.event_listener.after_change_value_of("Alert text", self.driver)

    def confirm_text_is_displayed(self, text) -> bool:
        return self.alertsPage.confirmResult.text == text

    def prompt_text_is_displayed(self, text) -> bool:
        return text in self.alertsPage.promptResult.text
