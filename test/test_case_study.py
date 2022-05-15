import time
import unittest

import pytest

from src.Pages import HomePage
from src.Base.session import Session
from src.Pages.BasketPage import BasketPage
from src.Pages.HomePage import HomePage
from src.Pages.ItemDetailPage import ItemDetailPage
from src.Pages.SearchResultPage import SearchResultPage



class Test_case_study(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Session.start_web_driver_session()
        cls.driver.maximize_window()
        cls.home_page = HomePage(cls.driver)
        cls.search_result_page = SearchResultPage(cls.driver)
        cls.item_detail_page = ItemDetailPage(cls.driver)
        cls.basket_page = BasketPage(cls.driver)
        cls.driver.get(HomePage.get_base_url())

    @pytest.mark.order(1)
    def test_search_item(self) -> None:
        time.sleep(3)
        self.home_page.search_item('Bilgisayar')
        self.search_result_page.go_to_second_page()
        self.search_result_page.verify_navigated_to_second_page()
        self.search_result_page.open_item()

    @pytest.mark.order(2)
    def test_open_item_detail(self):
        global item_price
        self.item_detail_page.get_item_title()
        item_price = self.item_detail_page.get_item_price()

    @pytest.mark.order(3)
    def test_add_item_to_basket(self):
        global basket_price
        self.item_detail_page.add_to_basket()
        self.item_detail_page.go_to_basket()
        basket_price = self.basket_page.get_item_price()
        assert basket_price == item_price

    @pytest.mark.order(4)
    def test_increase_item_amount(self):
        self.basket_page.increase_item_amount()
        item_amount = self.basket_page.get_item_amount()
        assert item_amount == '2'


    @pytest.mark.order(5)
    def test_delete_item(self):
        self.basket_page.delete_item()
        assert self.basket_page.basket_is_empty()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.close()
            cls.driver.quit()
