from selenium.webdriver.common.by import By


class HomePageLocators:
    search_box = (By.XPATH, "//input[@name='k']")
    search_button = (By.XPATH, "//button[@data-cy='search-find-button']")
    cookie_close_button = (By.XPATH, "//span[text()='Kapat']")

class SearchResultPageLocators:
    card_item = (By.XPATH, "//article[@data-cy='product-card-item']/div[2]/a")
    second_pagination_item = (By.XPATH, "//a[@title='2. sayfa']")


class ItemDetailPageLocators:
    item_price = (By.ID, "sp-price-lowPrice")
    item_title = (By.ID, "sp-title")
    add_to_basket = (By.ID, "add-to-basket")
    basket = (By.XPATH, "//a[@class='dIB']")# "//div[@class='basket-container robot-header-iconContainer-cart']")


class BasketPageLocators:
    item_price = (By.XPATH, "//p[@class='new-price']")
    item_amount = (By.XPATH, "//select[@class='amount']")
    delete_item = (By.XPATH, "//a[@title='Sil']")
    empty_basket = (By.XPATH, "//div[@class='clearfix']//h2")
