from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.utilities.config import ConfigManager
from framework.utilities.loggingUtil import EventLogger


class DriverUtil:
    """Singleton class to create webdriver instance with options specified in config.json
    Browser choice depends on provided optional cli argument '--browser' (chrome/firefox)"""
    browser_choice = None
    event_listener = None
    _config_data = None
    _wait_time = None
    url = None
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.event_listener = EventLogger()
            DriverUtil.parse_config()
            if cls.browser_choice == "firefox":
                web_driver = webdriver.Firefox
                service = FirefoxService(GeckoDriverManager().install())
                webdriver_options = webdriver.FirefoxOptions()
            else:
                web_driver = webdriver.Chrome
                service = ChromeService(ChromeDriverManager().install())
                webdriver_options = webdriver.ChromeOptions()

            for option in DriverUtil._config_data['browser_options']:
                webdriver_options.add_argument(option)

            cls.driver = web_driver(service=service, options=webdriver_options)
            if len(cls.windows()) > 1:
                for window in cls.windows()[1:]:
                    cls.driver.switch_to.window(window)
                    cls.driver.close()
            cls.driver.switch_to.window(cls.windows()[0])
        return cls.driver

    @classmethod
    def quit_driver(cls) -> None:
        cls.driver.quit()
        cls.driver = None

    @classmethod
    def parse_config(cls):
        if cls._config_data is None:
            cls._config_data = ConfigManager.load_browser_config()
            cls._wait_time = cls._config_data['wait_time']
            cls.url = cls._config_data['url']

    @classmethod
    def windows(cls):
        return cls.driver.window_handles

    @classmethod
    def wait_until(cls, ec):
        return WebDriverWait(cls.driver, cls._wait_time).until(ec)

    @classmethod
    def close_current_tab(cls) -> None:
        cls.event_listener.before_close_current_tab(cls.driver)
        cls.driver.close()
        cls.event_listener.after_close_current_tab(cls.driver)

    @classmethod
    def switch_to_tab(cls, index) -> None:
        cls.event_listener.before_switch_tab(index, cls.driver)
        cls.driver.switch_to.window(cls.windows()[index])
        cls.event_listener.after_switch_tab(index, cls.driver)

    @classmethod
    def navigate_to(cls, url) -> None:
        cls.driver.get(url)

    @classmethod
    def get_alert(cls):
        return cls.driver.switch_to.alert
