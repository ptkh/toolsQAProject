from toolsQAProject.pages.forms.dropdownMenuForm import DropdownMenu
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.homePage import HomePage


class AlertsSteps:
    @property
    def homePage(self):
        return HomePage()

    @staticmethod
    def navigate_to_main_page() -> None:
        DriverUtil.navigate_to(DriverUtil.url)

    def main_page_is_open(self) -> bool:
        return self.homePage.homePageForm.main_page_is_open()

    def click_alertsFrameWindows_button(self) -> None:
        self.homePage.homePageForm.click_alertsFrameWindows_button()

    @property
    def dropdownMenu(self):
        return DropdownMenu()

    def click_alerts_button(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.click_alerts_button()

    def alerts_form_is_open(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.is_open()

    def click_see_alerts_button(self):
        self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.click_see_alerts_button()

    def alert_is_open(self, text: str) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.alert_is_open(text)

    def click_OK_on_alert(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.click_OK_on_alert()

    def alert_is_closed(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.alert_is_closed()

    def click_confirm_box_will_appear_button(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.click_confirm_box_will_appear_button()

    def confirm_text_is_displayed(self, text: str) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.confirm_text_is_displayed(text)

    def click_prompt_box_will_appear_button(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.click_prompt_box_will_appear_button()

    def enter_text_in_alert(self, text: str) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.enter_text_in_alert(text)

    def prompt_text_is_displayed(self, text: str) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.alertsPage.alertsForm.prompt_text_is_displayed(text)
