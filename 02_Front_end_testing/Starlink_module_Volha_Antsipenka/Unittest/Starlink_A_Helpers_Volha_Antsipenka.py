#Helpers file for Starlink_A_unittest_Volha_Antsipenka.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import random
import time
import requests

def delay():
    time.sleep(random.randint(2,5))


Starlink_url = "https://starlink.com/"

test_address = "13036 SD-244, Keystone, SD 57751"

# test_email =
# test_phone =
# test_name =

#Starlink homepage logo XPath
homepage_logo = '//img[@class="MuiBox-root mui-iu1euh"]'

#Starlink 'Get Started' button XPath
getstarted_button = '//div[@class="MuiBox-root mui-1hbure9"]//button[@type="button"][normalize-space()="Get Started"]'

#Starlink address input field XPath
address_input_field = '//input[contains(@placeholder,"Address") or @id="_r_1v_"]'

#Starlink address dropdown list XPath
address_dropdown = "//div[contains(@class,'pac-item') or contains(@class,'suggestion') or @role='option'] | //div[contains(@class,'pac-container')]//div")


#Starlink Homepage title check
def assert_title(driver, title):
    wait= WebDriverWait(driver, 5)
    try:
        wait.until(EC.title_is(title))
        print(f"\nTitle check PASS: Page has title '{driver.title}'")
    except WDE:
        print(f"\nTitle check FAIL: Page has wrong title '{driver.title}'")
        driver.get_screenshot_as_file('Wrong_Title.png')
        assert False, f"Wrong page title. Expected '{driver.title}' to be '{title}'"


#Starlink Homepage logo check
def assert_logo(driver, locator):
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        print("\nLogo check PASS: Page has correct logo")
    except WDE:
        print("\nLogo check FAIL: Page has wrong logo")
        driver.get_screenshot_as_file('Wrong_logo.png')
        assert False, "Wrong page logo"


#Waits for element to be clickable and clicks
def wait_and_click(driver, locator):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    time.sleep(0.5)
    element.click()
    return element


#Enters address and selects it from dropdown menu
def enter_address(driver, input_locator, dropdown_locator, address):
    wait = WebDriverWait(driver, 5)
    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, input_locator)))
    address_input.clear()
    address_input.send_keys(address)

    # Waits for Google Places dropdown and clicks
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_locator)))
    time.sleep(0.5)
    dropdown.click()


def verify_availability_and_pricing(driver, timeout=15):
    """Verifies that after address selection we get availability + pricing page"""
    wait = WebDriverWait(driver, timeout)
    # After selecting address, Starlink redirects to /residential or shows Order page with $55/$85/$130
    # Wait for any pricing element or Order summary
    pricing_locator = (By.XPATH, "//*[contains(text(),'$55') or contains(text(),'$85') or contains(text(),'$130') or contains(text(),'Availability') or contains(text(),'Order Summary')]")
    try:
        element = wait.until(EC.visibility_of_element_located(pricing_locator))
        print(f"\nPASS: Availability page loaded. Found: {element.text[:100]}")
        return True
    except TimeoutException:
        driver.save_screenshot('TC01_Availability_Fail.png')
        print("\nFAIL: No pricing/availability found after address selection")
        return False