from src.Pages.BasePage import BasePage
from src.Pages.Cons.Locators import HomePageLocators
from src.utils.utils import get_logger

base_url = "https://www.gittigidiyor.com/"


class HomePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.log = get_logger('HomePage')

    def search_item(self, item: str) -> None:
        self.log.info(f'Searching the {item}')
        self.click(*HomePageLocators.cookie_close_button)
        self.input(*HomePageLocators.search_box, text=item)
        self.click(*HomePageLocators.search_button)

    @staticmethod
    def get_base_url() -> str:
        return base_url
