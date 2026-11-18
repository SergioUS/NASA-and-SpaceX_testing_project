#Helpers file for Starlink_B_unittest_Volha_Antsipenka.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime
import random
import time

def delay():
    time.sleep(random.randint(2,5))


Starlink_url = "https://starlink.com/"

#Starlink test data
test_address = "13036 SD-244, Keystone, SD 57751"
invalid_test_address = "Ab 1-_,!@#<>"
invalid_test_email = "dA*(#-=_@gmai.co"
invalid_test_input = "Ab 1-_,!@#<>"

#Starlink homepage logo XPath
homepage_logo = '//img[@class="MuiBox-root mui-iu1euh"]'

#Starlink 'Get Started' button XPath
map_getstarted_button = "//button[contains(.,'Get Started')] | //button[@type='submit']"

#Starlink address input field XPath
address_input_field = '//input[contains(@placeholder,"Search address...")]'

#Starlink address dropdown list XPath
address_dropdown = "//div[contains(@class,'MuiAutocomplete-popper')] | //li[contains(@role,'option')]"

#Starlink order page XPath
order_page_locator= "//h6[contains(text(),'available')] | //button[@aria-label='checkout'] | //h1[contains(text(),'Order')]"

#Starlink 'Checkout' button XPath
checkout_button = "//button[@aria-label='checkout'] | //div[contains(@class,'MuiButtonBase-root')]"

#Starlink checkout page XPath
checkout_page_locator= "//h3[contains(text(),'Order Summary')] | //button[@aria-label='order'] | //h1[contains(text(),'Checkout')]"

#Starlink 'Place order' button
place_order = "//button[@aria-label='order'] | //button[contains(.,'Place Order')]"

#Starlink 'Learn' button XPath
learn_button = "//button[.//p[text()='Learn']]"

#Starlink 'Availability map' button XPath
map_button = "//p[contains(.,'Availability Map')]"

#Starlink error messages XPaths
error_message = "//*[contains(@class,'error')]"
invalid_address_error = "//p[contains(.,'Please select an address from the suggestions')]"
invalid_data_error_message = "//span[contains(.,'Invalid email address')] | //p[@id='_r_3_-helper-text']"
email_not_found_error_message = "//div[@role='alert'] | //div[contains(.,'Email not found')]"

#Starlink user account XPaths
user_account_icon = "//a[@aria-label='Sign In']"
account_email_input_field = "//input[@type='email'] | //input[@id='_r_3_']"
next_button = "//button[@type='submit'] | //button[contains(.,'Next')]"
password_input = "//input[@type='password']"

#Starlink credentials input fields XPaths
email_input_field = "//input[@type='email'] | //input[@id='_r_9_']"
first_name_input_field = "//input[contains(@name,'firstName')] | //input[@id='_r_a_']"
last_name_input_field = "//input[contains(@name,'lastName')] | //input[@id='_r_b_']"
phone_input_field = "//input[contains(@name,'phone')] | //input[@id='_r_c_']"
cardholder_name_input_field = "//input[contains(@name,'cardholderName')] | //input[@id='_r_1a_']"
card_number_input_field = "//input[@aria-label='Card Number'] | //input[@id='adyen-checkout-encryptedCardNumber-1792965535397'] | //input[contains(@placeholder,'4444 3333 2222 1111')]"
mm_yy_input_field = "//input[@aria-label='MM/YY'] | //input[@id='adyen-checkout-encryptedExpiryDate-1792965535398']"
cvc_input_field = "//input[@aria-label='CVC'] | //input[@id='adyen-checkout-encryptedSecurityCode-1792965535399']"
iframe_card_number = "//iframe[contains(@title,'Iframe for card number')]"
iframe_mm_yy = "//iframe[contains(@title,'Iframe for expiry date')]"
iframe_cvc = "//iframe[contains(@title,'Iframe for security code')]"



#Screenshots function
def screenshot(driver, name="error"):
    folder = "C:/Users/olya0/PycharmProjects/NASA-and-SpaceX_testing_project/02_Front_end_testing/Starlink_module_Volha_Antsipenka/Screenshots"
    dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #date+time
    path = f"{folder}/{name}_{dt}.png"
    driver.save_screenshot(path)
    return path


#Starlink Homepage title check
def assert_title(driver, title):
    wait= WebDriverWait(driver, 5)
    try:
        wait.until(EC.title_is(title))
        print(f"\nTitle check PASS: Page has title '{driver.title}'")
    except WDE:
        print(f"\nTitle check FAIL: Page has wrong title '{driver.title}'")
        screenshot(driver, "Wrong_Title")
        assert False, f"Wrong page title. Expected '{driver.title}' to be '{title}'"


#Starlink Homepage logo check
def assert_logo(driver, locator):
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        print("\nLogo check PASS: Page has correct logo")
    except WDE:
        print("\nLogo check FAIL: Page has wrong logo")
        screenshot(driver, "Wrong_Logo")
        assert False, "Wrong page logo"


#Waits for element to be clickable and clicks
def wait_and_click(driver, locator):
    wait = WebDriverWait(driver, 7)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    time.sleep(1)
    element.click()
    return element


#Hovers over element
def hover_over(driver, locator):
    wait = WebDriverWait(driver, 7)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    ActionChains(driver).move_to_element(element).perform()
    return element


#Enters address and selects it from dropdown menu
def enter_address(driver, input_locator, dropdown_locator, address):
    wait = WebDriverWait(driver, 7)
    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, input_locator)))
    address_input.clear()
    address_input.send_keys(address)

    #Waits for Google Places dropdown and clicks
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_locator)))
    time.sleep(1)
    dropdown.click()


#Fills input field with provided value
def fill_input_field(driver, locator, value):
    wait = WebDriverWait(driver, 7)
    input_field = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    input_field.click()
    input_field.clear()
    input_field.send_keys(value)
    return input_field


#Fills input field inside iframe (for payment information)
def fill_iframe_input_field(driver, iframe_locator, input_field_locator, value):
    wait = WebDriverWait(driver, 7)
    iframe = wait.until(EC.element_to_be_clickable((By.XPATH, iframe_locator)))
    driver.switch_to.frame(iframe)
    input_field = wait.until(EC.element_to_be_clickable((By.XPATH, input_field_locator)))
    input_field.click()
    input_field.clear()
    input_field.send_keys(value)
    driver.switch_to.default_content()


#Verifies that after selecting address Starlink redirects to Order page with displayed availability and pricing
def verify_availability_and_pricing(driver, locator):
    wait = WebDriverWait(driver, 7)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        print("\nOrder page loaded successfully")
    except WDE:
        screenshot(driver, "Order_page_redirect_Fail")
        print("\nFAIL: No pricing/availability found after address selection")
        assert False, "Order page ERROR. No pricing/availability found after address selection"


#Verifies that after clicking 'Checkout' button Starlink redirects to the checkout page
def verify_checkout_page(driver, locator):
    wait = WebDriverWait(driver, 7)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        print("\nCheckout page loaded successfully")
    except WDE:
        screenshot(driver, "Checkout_page_redirect_Fail")
        print("\nFAIL: Checkout page load unsuccessful")
        assert False, "Checkout page ERROR. Checkout page load unsuccessful"


#Verifies that for invalid input data Starlink displays error message
def verify_error_message(driver, locator):
    wait = WebDriverWait(driver, 7)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        print("\nWebsite shows error message for invalid data input")
    except WDE:
        screenshot(driver, "Error_message_display_Fail")
        print("\nFAIL: No error message was displayed after invalid data input")
        assert False, "ERROR. No error message was displayed after invalid data input"


#Verifies that for valid input data Starlink does not display error message
def verify_no_error_message(driver, locator):
    wait = WebDriverWait(driver, 7)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        screenshot(driver, "Unexpected_error_message")
        print("\nFAIL: Error message was displayed after valid data input")
        assert False, "ERROR. Error message was displayed after valid data input"
    except WDE:
        print("\nWebsite does not show error message for valid data input")


#Verifies that for valid input data Starlink does not display error message in iframe
def verify_no_error_message_iframe(driver, iframe_locator, error_locator):
    wait = WebDriverWait(driver, 7)
    try:
        iframe = driver.find_element(By.XPATH, iframe_locator)
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, error_locator)
        driver.switch_to.default_content()
        screenshot(driver, "Unexpected_error_message")
        print("\nFAIL: Error message was displayed after valid data input")
        assert False, "ERROR. Error message was displayed after valid data input"
    except WDE:
        driver.switch_to.default_content()
        print("\nWebsite does not show error message for valid data input")


#Verifies that for invalid input data Starlink displays error message in iframe
def verify_error_message_iframe(driver, iframe_locator, error_locator):
    wait = WebDriverWait(driver, 7)
    try:
        iframe = driver.find_element(By.XPATH, iframe_locator)
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, error_locator)
        driver.switch_to.default_content()
        print("\nPASS: Error message was displayed after invalid data input")
        return True
    except WDE:
        driver.switch_to.default_content()
        screenshot(driver, "Error_message_display_Fail")
        assert False, "ERROR. Error message was not displayed after invalid data input"


# # Verifies that Starlink shows availability after selecting address on map
# def verify_map_availability(driver, locator):
#     wait = WebDriverWait(driver, 7)
#     try:
#         wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
#         print("\nMap shows availability coverage for selected address")
#     except WDE:
#         driver.get_screenshot_as_file('Map_availability_load_Fail.png')
#         print("\nFAIL: No availability coverage on map displayed after address selection")
#         assert False, "Map availability page ERROR. No availability coverage on map displayed after address selection"
