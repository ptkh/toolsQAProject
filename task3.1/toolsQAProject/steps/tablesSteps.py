from toolsQAProject.pages.forms.dropdownMenuForm import DropdownMenu
from framework.utilities.driverUtil import DriverUtil
from toolsQAProject.pages.homePage import HomePage


class TablesSteps:
    @property
    def homePage(self):
        return HomePage()

    @staticmethod
    def navigate_to_main_page() -> None:
        DriverUtil.navigate_to(DriverUtil.url)

    def main_page_is_open(self) -> bool:
        return self.homePage.homePageForm.main_page_is_open()

    def click_elements_button(self) -> None:
        self.homePage.homePageForm.click_elements_button()

    @property
    def dropdownMenu(self):
        return DropdownMenu()

    def click_web_tables_button(self) -> None:
        self.dropdownMenu.elementsMenu.click_web_tables_button()

    def web_tables_form_is_open(self) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.is_open()

    def click_add_button(self):
        self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.click_add_button()

    def registration_form_is_open(self) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.registration_form_is_open()

    def enter_user_data(self, user_data: dict) -> None:
        self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.enter_user_data(user_data)

    def click_submit(self) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.click_submit_on_registration_form()

    def registration_form_is_closed(self) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.registration_form_is_closed()

    def user_in_table(self, user_data) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.user_in_table(user_data)

    @property
    def number_of_records(self) -> int:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.number_of_records

    def delete_user(self, user_data: dict) -> None:
        self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.delete_user(user_data)

    def user_not_in_table(self, user_data: dict) -> bool:
        return self.dropdownMenu.elementsMenu.tablesPage.webTablesForm.user_not_in_table(user_data)
