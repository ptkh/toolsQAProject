from selenium.webdriver.common.by import By
from framework.base.elements import Button
from toolsQAProject.pages.forms.linksForm import LinksForm


class LinksPage:
    """RegistrationForm for working with links page"""
    @property
    def homeLink(self):
        return Button(By.ID, 'simpleLink', "'Home' link")

    @property
    def linksForm(self):
        return LinksForm(self)
