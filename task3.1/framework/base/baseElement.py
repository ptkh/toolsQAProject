from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as ec
from framework.utilities.driverUtil import DriverUtil
from framework.utilities.loggingUtil import EventLogger


class BaseElement:
    """Base class for webelements"""

    def __init__(self, by: str, value: str, name=''):
        self.driver = DriverUtil.get_driver()
        self.event_listener = EventLogger()
        self.by = by
        self.value = value
        self.name = name
        self.locator = (self.by, self.value)

    @property
    def element(self):
        try:
            self.event_listener.before_find(*self.locator, self.driver)
            DriverUtil.wait_until(ec.visibility_of_element_located(self.locator))
            element = self.driver.find_element(*self.locator)
            self.event_listener.after_find(*self.locator, self.driver)
            return element
        except NoSuchElementException as e:
            self.event_listener.on_exception(e, self.driver)
            raise NoSuchElementException("Could not find element - %s" % self.name)

    @property
    def text(self):
        return self.element.text

    def is_displayed(self) -> bool:
        return self.element.is_displayed()

    def click(self) -> None:
        try:
            self.event_listener.before_click(self.name, self.driver)
            self.element.click()
            self.event_listener.after_click(self.name, self.driver)
        except ElementClickInterceptedException as e:
            self.event_listener.on_exception(e, self.driver)
            self.scroll_click()
        except ElementNotInteractableException as e:
            self.event_listener.on_exception(e, self.driver)
            self.scroll_click()

    def scroll_click(self) -> None:
        try:
            self.event_listener.before_click(self.name, self.driver)
            DriverUtil.wait_until(ec.element_to_be_clickable(self.element))
            self.element.click()
            self.event_listener.after_click(self.name, self.driver)
        except ElementClickInterceptedException as e:
            self.event_listener.on_exception(e, self.driver)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DOWN * 3).perform()
            self.scroll_click()
        except ElementNotInteractableException as e:
            self.event_listener.on_exception(e, self.driver)
            self.scroll_click()
