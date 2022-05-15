import os
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from src.utils.utils import get_logger, setup_logger

APP_DIR = os.path.dirname(os.path.abspath(__file__))
setup_logger(output_file=os.path.join(APP_DIR, 'Logs', 'test.log'))


class BasePage:
    def __init__(self, driver) -> None:
        self.web_driver_wait = WebDriverWait(driver, 30)
        self.driver = driver
        self.log = get_logger('BasePage')

    def find_element(self, *locator) -> WebElement:
        return self.driver.find_element(*locator)

    def click(self, *locator) -> None:
        element = self.find_element(*locator)
        self.web_driver_wait.until(EC.element_to_be_clickable(element))
        element.click()
        time.sleep(3)

    def input(self, *locator, text: str) -> None:
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def select(self, *locator) -> Select:
        return Select(self.find_element(*locator))

