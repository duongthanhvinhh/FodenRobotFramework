from selenium.webdriver.common.by import By

from page_objects.cart_page import CartPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.shop_page = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products_list = (By.XPATH, "//div[@class='card h-100']")
        self.product_name = (By.XPATH, ".//div/h4/a")
        self.add_item_button = (By.XPATH, ".//div/button")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def go_to_shop(self):
        self.driver.find_element(*self.shop_page).click()

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(*self.products_list)
        for product in products:
            product_name = product.find_element(*self.product_name).text
            if product_name == product_name:
                # Add item into cart
                product.find_element(*self.add_item_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        return CartPage(self.driver)
