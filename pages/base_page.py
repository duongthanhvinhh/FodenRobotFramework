import os
import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions

from constants.framework_constants import DEFAULT_TIMEOUT

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def wait_for_page_load(self, timeout=DEFAULT_TIMEOUT):
        """Wait until document.readyState == 'complete'."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def wait_for_element_present(self, by, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for the element to be present in DOM."""
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((by, locator))
        )

    def wait_for_element_visible(self, by, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for the element to be visible."""
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, locator))
        )

    def wait_for_element_clickable(self, by, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for the element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, locator))
        )

    def wait_for_element_attribute_value(self, by, locator, attribute, expected_value, timeout=DEFAULT_TIMEOUT):
        """Wait for element's attribute to have a specific value."""
        def attribute_value_is(driver):
            try:
                element = driver.find_element(by, locator)
                return element.get_attribute(attribute) == expected_value
            except NoSuchElementException:
                return False

        WebDriverWait(self.driver, timeout).until(attribute_value_is)

    def wait_for_element_disappear(self, by, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located((by, locator))
        )

    def wait_for_text_in_element(self, by, locator, expected_text, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.text_to_be_present_in_element((by, locator), expected_text)
        )

    def click_to_element(self, by, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for the element to be clickable and click it."""
        element = self.wait_for_element_clickable(by, locator, timeout)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Handle cases where another element obscures the click
            self.driver.execute_script("arguments[0].click();", element)

    def set_text_to_element(self, by, locator, text, timeout=DEFAULT_TIMEOUT):
        """Wait for element to be visible, clear any existing text and input the new text."""
        element = self.wait_for_element_visible(by, locator, timeout)
        element.clear()
        element.send_keys(text)

    def hover_over_element(self, by, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_visible(by, locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_element(self, by, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_present(by, locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def double_click_element(self, by, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_visible(by, locator, timeout)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_element(self, by, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_visible(by, locator, timeout)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_by, source_locator, target_by, target_locator, timeout=DEFAULT_TIMEOUT):
        source = self.wait_for_element_visible(source_by, source_locator, timeout)
        target = self.wait_for_element_visible(target_by, target_locator, timeout)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def upload_file(self, by, locator, file_path, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_present(by, locator, timeout)
        element.send_keys(file_path)

    # ========== Browser / Alert / Frames ==========
    def switch_to_frame(self, by, locator, timeout=DEFAULT_TIMEOUT):
        frame = self.wait_for_element_present(by, locator, timeout)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_name=None, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        if window_name:
            self.driver.switch_to.window(window_name)
        else:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def refresh_page(self):
        self.driver.refresh()

    def accept_alert(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def get_element_text(self, by, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_visible(by, locator, timeout)
        return element.text

    def get_element_attribute(self, by, locator, attribute, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_element_present(by, locator, timeout)
        return element.get_attribute(attribute)

    def execute_js_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def highlight_element(self, by, locator, effect_time=2, color="yellow", border="2px solid red"):
        element = self.wait_for_element_present(by, locator)
        original_style = element.get_attribute('style')
        self.driver.execute_script(f"arguments[0].setAttribute('style', arguments[1]);", element, f"border: {border}; background-color: {color};")
        time.sleep(effect_time)
        self.driver.execute_script(f"arguments[0].setAttribute('style', arguments[1]);", element, original_style)

    def take_screenshot(self, filename='screenshot.png', folder='screenshots'):
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, filename)
        self.driver.save_screenshot(path)

    # ========== Assertion Helpers ==========
    def assert_element_text_equals(self, by, locator, expected_text, timeout=DEFAULT_TIMEOUT):
        actual_text = self.get_element_text(by, locator, timeout)
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'."

    def assert_element_attribute_contains(self, by, locator, attribute, expected_value, timeout=DEFAULT_TIMEOUT):
        actual_value = self.get_element_attribute(by, locator, attribute, timeout)
        assert expected_value in actual_value, f"Expected '{expected_value}' to be in attribute value '{actual_value}'."
