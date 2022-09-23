from selenium.webdriver.common.by import By
from framework.base.baseForm import BaseForm
from framework.base.elements import Button
from toolsQAProject.pages.linksPage import LinksPage
from toolsQAProject.pages.webTablesPage import WebTablesPage


class ElementsMenu(BaseForm):
    """RegistrationForm for working with elements"""
    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(@class, 'main-header')][text()='Elements']", "Elements header"))

    @property
    def tablesPage(self):
        return WebTablesPage()

    @property
    def linksPage(self):
        return LinksPage()

    @property
    def webTablesButton(self):
        return Button(By.XPATH, "//span[text()='Web Tables']", "'Web Tables' button")

    @property
    def linksButton(self):
        return Button(By.XPATH, "//span[text()='Links']", "'Links' button")

    def click_links_button(self) -> None:
        self.linksButton.click()

    def click_web_tables_button(self) -> None:
        self.webTablesButton.click()

