from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class CartPage(BasePage):

     def __init__(self, driver):
         super().__init__(driver)
         self.driver = driver
         self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
         self.country_search_input = (By.ID, "country")
         self.target_country = (By.LINK_TEXT, "{}")
         self.term_and_condition =(By.XPATH, "//div[@class='checkbox checkbox-primary']")
         self.purchase_button = (By.CSS_SELECTOR, "[type='submit']")
         self.success_alert = (By.CLASS_NAME, "alert-success")

     def checkout(self):
         self.driver.find_element(*self.checkout_button).click()

     def enter_delivery_address(self, country_name):
         self.driver.find_element(*self.country_search_input).send_keys(country_name)
         wait = WebDriverWait(self.driver, 7)
         dynamic_target_country_xpath = (self.target_country[0], self.target_country[1].format(country_name))
         wait.until(expected_conditions.presence_of_element_located(dynamic_target_country_xpath))
         self.driver.find_element(*dynamic_target_country_xpath).click()
         self.driver.find_element(*self.term_and_condition).click()
         self.driver.find_element(*self.purchase_button).click()

     def validate_order_successfully(self, success_message):
         success_text = self.driver.find_element(*self.success_alert).text
         assert success_message in success_text
         # self.driver.get_screenshot_as_file("screen.png")'×
         # Success! Thank you! Your order will be delivered in next few weeks :-).'