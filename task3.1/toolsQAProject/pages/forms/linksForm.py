from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm


class LinksForm(BaseForm):
    """RegistrationForm for working with links page"""
    def __init__(self, page):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Links']", "Links header"))
        self.linksPage = page

    def click_home_link(self) -> None:
        self.linksPage.homeLink.click()

