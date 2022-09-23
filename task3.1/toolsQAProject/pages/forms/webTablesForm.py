from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Button
from framework.models.userModel import User
from selenium.webdriver.support import expected_conditions as ec
from framework.utilities.driverUtil import DriverUtil


class WebTablesForm(BaseForm):
    """Form for working with web tables page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Web Tables']", "Web Tables header"))
        self.webTablesPage = page

    def user_in_table(self, user: User) -> bool:
        email_path = f"//div[@class='rt-td'][contains(text(),'{user.email}')]"
        user_email = self.driver.find_elements(By.XPATH, email_path)
        if user_email:
            if user.email in user_email[0].text:
                return True
        return False

    def delete_user(self, user: User) -> None:
        rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']//div[contains(text(),'@')]")
        current_user = self.driver.find_elements(By.XPATH, f"//div[@class='rt-tr-group']"
                                                           f"//div[contains(text(),'{user.email}')]")[0]
        for i in range(len(rows)):
            if rows[i].text == current_user.text:
                delete = Button(By.ID, f"delete-record-{i+1}")
                delete.click()

    @property
    def number_of_records(self):
        rows = self.driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']//div[contains(text(),'@')]")
        return len(rows)

    def registration_form_is_open(self) -> bool:
        return self.webTablesPage.registrationForm.is_open()

    def click_submit_on_registration_form(self):
        self.webTablesPage.registrationForm.click_submit()

    def enter_user_data(self, user_data: dict):
        self.webTablesPage.registrationForm.enter_user_data(user_data)

    def registration_form_is_closed(self) -> bool:
        reg_form = self.driver.find_elements(By.ID, "registration-form-modal")
        if reg_form:
            DriverUtil.wait_until(ec.invisibility_of_element(reg_form[0]))
        return not bool(self.driver.find_elements(By.ID, "registration-form-modal"))

    def click_add_button(self) -> None:
        self.webTablesPage.addButton.click()
