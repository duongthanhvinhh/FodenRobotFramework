import json

import pytest

from pages.login_page import LoginPage

test_data_path = "../data/test_e2e.json"
with open(test_data_path) as data_file:
    test_data = json.load(data_file)
    test_list = test_data["data"]

@pytest.mark.smoke # This is like category in selenium Java and C# => To run by filtering category: pytest -m smoke
@pytest.mark.parametrize("test_list_item",test_list) # test_list_item is defined as an item of the test_list, to get data for each loop when using parametrize
def test_e2e(handle_browser, test_list_item): # the test_list_item in parametrize should be passed as an argument of the test
    driver = handle_browser
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["user_name"], test_list_item["password"])
    shop_page.go_to_shop()
    shop_page.add_product_to_cart(test_list_item["product_name"])
    cart_page = shop_page.go_to_cart()
    cart_page.checkout()
    cart_page.enter_delivery_address(test_list_item["target_country"])
    cart_page.validate_order_successfully("Success! Thank you! Your order will be delivered in next few weeks")


