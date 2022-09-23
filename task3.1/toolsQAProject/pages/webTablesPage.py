from selenium.webdriver.common.by import By
from framework.base.elements import Button
from toolsQAProject.pages.forms.registrationForm import RegistrationForm
from toolsQAProject.pages.forms.webTablesForm import WebTablesForm


class WebTablesPage:
    """RegistrationForm for working with web tables page"""
    @property
    def addButton(self):
        return Button(By.ID, "addNewRecordButton", "'Home' link")

    @property
    def registrationForm(self):
        form_inputs = {
                            'f_name': (By.XPATH, "//div[@id='firstName-wrapper']//input", "'First Name' input"),
                            'l_name': (By.XPATH, "//div[@id='lastName-wrapper']//input", "'Last Name' input"),
                            'email': (By.XPATH, "//div[@id='userEmail-wrapper']//input", "'Email' input"),
                            'age': (By.XPATH, "//div[@id='age-wrapper']//input", "'Age' input"),
                            'salary': (By.XPATH, "//div[@id='salary-wrapper']//input", "'Salary' input"),
                            'dept': (By.XPATH, "//div[@id='department-wrapper']//input", "'Department' input")
                        }
        form_submit = (By.ID, "submit", "'Submit' button")
        return RegistrationForm(inputs=form_inputs, submit=form_submit)

    @property
    def webTablesForm(self):
        return WebTablesForm(self)
