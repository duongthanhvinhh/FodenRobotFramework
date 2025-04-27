import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login_page import LoginPage
from page_objects.shop_page import ShopPage


# @pytest.mark.usefixtures("handle_browser")
# class TestEndToEnd:
def test_e2e(handle_browser):
    driver = handle_browser
    login_page = LoginPage(driver)
    shop_page = login_page.login("rahulshettyacademy", "learning")
    shop_page.go_to_shop()
    shop_page.add_product_to_cart("Blackberry")
    cart_page = shop_page.go_to_cart()


    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 7)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    success_text = driver.find_element(By.CLASS_NAME, "alert-success").text

    assert "Success! Thank you!" in success_text
    driver.get_screenshot_as_file("screen.png")


