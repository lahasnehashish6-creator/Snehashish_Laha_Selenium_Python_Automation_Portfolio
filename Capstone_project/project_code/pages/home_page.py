from selenium.webdriver.common.by import By


class HomePage:

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product)
        self.driver.find_element(*self.SEARCH_BUTTON).click()