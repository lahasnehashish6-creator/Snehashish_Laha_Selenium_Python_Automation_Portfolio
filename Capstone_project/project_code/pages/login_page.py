from selenium.webdriver.common.by import By


class LoginPage:

    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_warning(self):
        return self.driver.find_element(*self.WARNING).text

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()