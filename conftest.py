import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.chrome.options import Options as chromOptions
from selenium.webdriver.ie.service import Service

# To control the option you send along with the command to execute test in terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def handle_browser(request):
    browser_name = request.config.getoption("--browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        options = chromOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("signon.rememberSignons", False)
        profile.set_preference("signon.autofillForms", False)
        options = firefoxOptions()
        options.profile = profile
        driver = webdriver.Firefox(options=options, service=service_obj)
        # driver = webdriver.Firefox(service=service_obj)
    else:
        options = chromOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=service_obj, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver #To send driver back to class test which call this fixture
    print("Add some actions needed to run after method")
    driver.close()