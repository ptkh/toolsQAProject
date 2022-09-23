from framework.base.baseElement import BaseElement
from framework.utilities.driverUtil import DriverUtil
from framework.utilities.loggingUtil import EventLogger


class BaseForm:
    """Base class for providing access to webdriver and logger"""

    def __init__(self, unique_locator: tuple[str, str, str]):
        self.driver = DriverUtil.get_driver()
        self.unique_locator = unique_locator
        self.event_listener = EventLogger()

    @property
    def uniqueElement(self):
        return BaseElement(*self.unique_locator)

    def is_open(self) -> bool:
        return self.uniqueElement.is_displayed()
