from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
import logging
import os


class Logger:
    root = os.path.abspath(os.path.dirname(__file__)).split('task3.1')[0]

    def __new__(cls, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        f_handler = logging.FileHandler('../log/report.log')
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        f_handler.setFormatter(formatter)
        logger.addHandler(f_handler)
        return logger


class EventLogger(AbstractEventListener):
    """Event listener class working with logger"""

    def __init__(self):
        self.logger = Logger()

    def before_navigate_to(self, page, driver):
        self.logger.info("Opening %s" % page)

    def after_navigate_to(self, page, driver):
        self.logger.info("%s opened" % page)

    def before_find(self, by, value, driver):
        self.logger.info("About to find element by - %s - %s" % (by, value))

    def after_find(self, by, value, driver):
        self.logger.info("Found element by - %s - %s" % (by, value))

    def before_click(self, element, driver):
        self.logger.info("About to click element - %s" % element)

    def after_click(self, element, driver):
        self.logger.info("Clicked element - %s " % element)

    def before_change_value_of(self, element, driver):
        self.logger.info("About to change value of element - %s" % element)

    def after_change_value_of(self, element, driver):
        self.logger.info("Changed value of element - %s" % element)

    def before_switch_tab(self, tab, driver):
        self.logger.info("About to switch to tab %d " % tab)

    def after_switch_tab(self, tab, driver):
        self.logger.info("Switched to tab %d " % tab)

    def before_close_current_tab(self, driver):
        self.logger.info("About to close current tab - %s" % driver)

    def after_close_current_tab(self, driver):
        self.logger.info("Closed current tab - %s" % driver)

    def before_quit(self, driver):
        self.logger.info("About to quit driver - %s" % driver)

    def after_quit(self, driver):
        self.logger.info("Quit driver - %s" % driver)

    def on_exception(self, exception, driver):
        self.logger.info("Exception has been raised - %s \n %s" % (driver, exception))
