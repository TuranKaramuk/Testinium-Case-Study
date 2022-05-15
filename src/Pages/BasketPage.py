import time

from src.Pages.BasePage import BasePage
from src.Pages.Cons.Locators import BasketPageLocators
from src.utils.utils import get_logger


class BasketPage(BasePage):
    def __init__(self,driver) -> None:
        super().__init__(driver)
        self.log = get_logger('BasketPage')

    def get_item_price(self) -> str:
        self.log.info('Getting item price in basket.')
        return self.find_element(*BasketPageLocators.item_price).text

    def increase_item_amount(self) -> None:
        self.log.info('Increasing item amount.')
        self.select(*BasketPageLocators.item_amount).select_by_value('2')
        time.sleep(3)

    def get_item_amount(self) -> str:
        return self.find_element(*BasketPageLocators.item_amount).get_attribute('value')

    def delete_item(self) -> None:
        self.log.info('Deleting item.')
        self.click(*BasketPageLocators.delete_item)

    def basket_is_empty(self) -> bool:
        if self.find_element(*BasketPageLocators.empty_basket).text == "Sepetinizde ürün bulunmamaktadır.":
            return True
