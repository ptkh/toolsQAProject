from toolsQAProject.pages.forms.dropdownMenuForm import DropdownMenu
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.homePage import HomePage


class IframeSteps:
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

    def click_nested_frames_button(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.click_nested_frames_button()

    def nested_frames_form_is_open(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.nestedFramesPage.nestedFramesForm.is_open()

    def parent_frame_is_displayed(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.nestedFramesPage.nestedFramesForm.parent_frame_is_displayed()

    def child_iframe_is_displayed(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.nestedFramesPage.nestedFramesForm.child_iframe_is_displayed()

    def click_frames_button(self):
        self.dropdownMenu.alertsFrameWindowsMenu.click_frames_button()

    def frames_form_is_open(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.framesPage.framesForm.is_open()

    @property
    def upper_frame_message(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.framesPage.framesForm.upperFrameMessage

    @property
    def lower_frame_message(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.framesPage.framesForm.lowerFrameMessage
