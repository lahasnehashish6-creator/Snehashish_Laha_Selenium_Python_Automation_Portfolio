from selenium.webdriver.common.by import By


class CartPage:

    CART_LINK = (By.CSS_SELECTOR, "#cart-total")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()