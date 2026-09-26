from selenium.webdriver.common.by import By


class ProductPage:

    MACBOOK = (By.LINK_TEXT, "MacBook")
    ADD_TO_CART = (By.ID, "button-cart")

    def __init__(self, driver):
        self.driver = driver

    def open_macbook(self):
        self.driver.find_element(*self.MACBOOK).click()

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()