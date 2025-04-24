from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://facebook.com")
sleep(40000)