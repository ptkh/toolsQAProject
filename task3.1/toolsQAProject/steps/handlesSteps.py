from toolsQAProject.pages.forms.dropdownMenuForm import DropdownMenu
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.homePage import HomePage


class HandlesSteps:
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

    def click_browser_windows_button(self) -> None:
        self.dropdownMenu.alertsFrameWindowsMenu.click_browser_windows_button()

    def windows_form_is_open(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.windowsPage.windowsForm.is_open()

    def click_new_tab_button(self):
        self.dropdownMenu.alertsFrameWindowsMenu.windowsPage.windowsForm.click_new_tab_button()

    def sample_page_is_open(self) -> bool:
        return self.dropdownMenu.alertsFrameWindowsMenu.windowsPage.windowsForm.sample_page_is_open()

    @property
    def number_of_windows(self) -> int:
        return len(DriverUtil.windows())

    @staticmethod
    def close_current_tab() -> None:
        DriverUtil.close_current_tab()
        DriverUtil.switch_to_tab(0)

    def click_elements_button(self) -> None:
        self.dropdownMenu.click_elements_button()

    def click_links_button(self) -> None:
        self.dropdownMenu.elementsMenu.click_links_button()

    def links_form_is_open(self) -> bool:
        return self.dropdownMenu.elementsMenu.linksPage.linksForm.is_open()

    def click_home_link_and_switch_to_new_tab(self) -> None:
        self.dropdownMenu.elementsMenu.linksPage.linksForm.click_home_link()
        DriverUtil.switch_to_tab(1)

    @staticmethod
    def resume_to_previous_tab() -> None:
        DriverUtil.switch_to_tab(0)
