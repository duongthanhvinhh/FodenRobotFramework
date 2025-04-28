from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.shop_page import ShopPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")
        # By username1 = By.XPATH("")

    def login(self,username, password):
        self.set_text_to_element(*self.username_input, username, 10)
        # self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        return ShopPage(self.driver)