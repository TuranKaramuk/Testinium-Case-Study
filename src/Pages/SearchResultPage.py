

from src.Pages.BasePage import BasePage
from src.Pages.Cons.Locators import SearchResultPageLocators
from selenium.webdriver.support import expected_conditions as EC

from src.utils.utils import get_logger

second_page_url = "https://www.gittigidiyor.com/arama?k=bilgisayar&sf=2"


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.log = get_logger('SearchResultPage')

    def go_to_second_page(self):
        self.log.info('Going to second page')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(*SearchResultPageLocators.second_pagination_item)
        self.web_driver_wait.until(EC.url_to_be('https://www.gittigidiyor.com/arama?k=Bilgisayar&sf=2'))

    def verify_navigated_to_second_page(self):
        self.log.info('Asserting url')
        assert "https://www.gittigidiyor.com/arama?k=Bilgisayar&sf=2" == self.driver.current_url

    def open_item(self):
        self.click(*SearchResultPageLocators.card_item)
