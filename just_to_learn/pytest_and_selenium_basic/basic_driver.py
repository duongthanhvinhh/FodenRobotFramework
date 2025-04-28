from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

# We can pass service object when initializing the browser like below
# service_obj = Service("#path_to_chrome_driver_on_you_local_machine")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
# driver.maximize_window()
driver.get("https://facebook.com")

# Javascript Executor
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# Get screenshot as file
driver.get_screenshot_as_file("screenshot.png")

# Actions in python
action = ActionChains(driver)
action.double_click(driver.find_element(By.XPATH, "//button[@type='submit']"))

print(driver.title)
print(driver.current_url)

driver.close()