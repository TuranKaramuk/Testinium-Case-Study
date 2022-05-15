from src.Pages.BasePage import BasePage
from src.Pages.Cons.Locators import ItemDetailPageLocators
from src.utils.utils import write_file, get_logger


class ItemDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.log = get_logger('ItemDetailPage')

    def get_item_title(self):
        self.log.info('Getting item info')
        item_title = self.find_element(*ItemDetailPageLocators.item_title).text
        write_file('item title: ' + item_title)
        self.log.info('item title: ' + item_title)

    def get_item_price(self):
        self.log.info('Getting item price')
        item_price = self.find_element(*ItemDetailPageLocators.item_price).text
        write_file('item price: ' + item_price)
        self.log.info('item price: ' + item_price)
        return item_price

    def add_to_basket(self):
        self.log.info('Item is adding to basket')
        self.click(*ItemDetailPageLocators.add_to_basket)

    def go_to_basket(self):
        self.log.info('Going to basket')
        self.click(*ItemDetailPageLocators.basket)