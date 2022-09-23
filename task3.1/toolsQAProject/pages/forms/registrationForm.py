from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Input, Button
from framework.models.userModel import User


class RegistrationForm(BaseForm):
    """Class for working with user form"""
    def __init__(self, inputs: dict, submit: tuple):
        super().__init__(unique_locator=(By.ID, "userForm", "Registration form"))
        self.inputs = inputs
        self.submit_ = submit

    @property
    def f_name(self):
        return Input(*self.inputs['f_name'])

    @property
    def l_name(self):
        return Input(*self.inputs['l_name'])

    @property
    def email(self):
        return Input(*self.inputs['email'])

    @property
    def age(self):
        return Input(*self.inputs['age'])

    @property
    def salary(self):
        return Input(*self.inputs['salary'])

    @property
    def dept(self):
        return Input(*self.inputs['dept'])

    @property
    def submit(self):
        return Button(*self.submit_)

    def enter_user_data(self, user: User) -> None:
        """Enters user data in the form"""
        self.f_name.click()
        self.f_name.enter_text(user.f_name)
        self.l_name.click()
        self.l_name.enter_text(user.l_name)
        self.email.click()
        self.email.enter_text(user.email)
        self.age.click()
        self.age.enter_text(user.age)
        self.salary.click()
        self.salary.enter_text(user.salary)
        self.dept.click()
        self.dept.enter_text(user.dept)

    def click_submit(self):
        self.submit.click()
