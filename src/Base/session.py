import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Session(unittest.TestCase):
    @staticmethod
    def start_web_driver_session():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(30)
        return driver
