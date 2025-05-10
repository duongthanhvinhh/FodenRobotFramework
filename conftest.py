import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
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
        chrome_prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  # <==== Important one added
        }
        options = ChromeOptions()
        options.add_experimental_option("prefs", chrome_prefs)

        driver = webdriver.Chrome(service=service_obj, options=options)

    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("signon.rememberSignons", False)
        profile.set_preference("signon.autofillForms", False)
        options = FirefoxOptions()
        options.profile = profile

        driver = webdriver.Firefox(service=service_obj, options=options)

    else:
        # Default to Chrome
        chrome_prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options = ChromeOptions()
        options.add_experimental_option("prefs", chrome_prefs)

        driver = webdriver.Chrome(service=service_obj, options=options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    yield driver

    try:
        driver.quit()
    except Exception as e:
        print(f"Error during driver quit: {e}")