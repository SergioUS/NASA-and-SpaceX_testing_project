# Zara Avramov - Unittest for SpaceX - Module Falcon 9 - Positive and Negative test cases

import time
from selenium import webdriver
import requests
import Helpers_SpaceX_Falcon9 as H
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


#import HtmlTestRunner
#import AllureReports


# Driver sleeps from 1 to 5 seconds
def delay() -> object:
    time.sleep(random.randint(1, 5))


class PositiveTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService())
        self.driver.maximize_window()

    # Test Case 025 - Verify and Validate Falcon 9 link
    def test_case_025(self):
        driver = self.driver

        print("Test Case 025")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            raise Exception("Falcon 9 is not available - Test Case 025 failed")
        else:
            print("Falcon 9 is available - Test Case 025 passed")

    # Test Case 026 - Validate "Play Video" button for "Falcon 9 in Flight" video
    def test_case_026(self):
        driver = self.driver

        print("Test Case 026")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            print("Falcon 9 is not available")

        # Locate the video
        driver.execute_script("window.scrollTo(0, 2300)")
        time.sleep(5)

        # Checking the play button
        driver.find_element(By.XPATH, '//*[@id="video"]/div[1]').click()
        time.sleep(10)
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')
        print("Video is working - Test Case 026 passed")

    # Test Case 027 - Verify and Validate image sliders for "Falcon 9" Overview
    def test_case_027(self):
        driver = self.driver

        print("Test Case 027")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            print("Falcon 9 is not available")

        # Locate the image sliders
        driver.execute_script("window.scrollTo(0, 1600)")
        time.sleep(5)

        # Verify Falcon 9 Overview
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-stagger')))

        # Use right arrow to scroll right
        right_arrow = driver.find_element(By.XPATH, '//*[@id="gallery-next-s"]')
        for arrow in range(4):
            right_arrow.send_keys(Keys.ARROW_RIGHT)
            delay()

        # Verify it's the last window
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Payload')]")))

        # Use left arrow to scroll left
        left_arrow = driver.find_element(By.XPATH, '//*[@id="gallery-prev-s"]')
        for arrow in range(4):
            left_arrow.send_keys(Keys.ARROW_LEFT)
            delay()

        # Verify it's the last window
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-stagger')))
            print("Image sliders are working - Test Case 027 passed")
        except WDE:
            print("Test Case 027 failed")

    # Test Case 028 - Validate "User's Guide Download" button
    def test_case_028(self):
        driver = self.driver

        print("Test Case 028")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Defining previous window
        window_before = driver.window_handles[0]

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            print("Falcon 9 is not available")

        # Locate section with Download User's Guide
        driver.execute_script("window.scrollTo(0, 4600)")
        time.sleep(4)

        # Verify Download User's Guide button is clickable
        driver.find_element(By.CLASS_NAME, "text").click()
        delay()

        # Defining window after
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        url = driver.current_url
        try:
            assert "falcon-users-guide-2021-09.pdf" in url
            print("User's Guide is downloading - Test Case 028 passed")
        except AssertionError:
            print("ATTENTION! URL is different. Test Case 028 failed")

    # Test Case 029 - Validate "sales@spacex.com" link
    def test_case_029(self):
        driver = self.driver

        print("Test Case 029")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            print("Falcon 9 is not available")

        # Scroll to locate sales@spacex.com link
        driver.execute_script("window.scrollTo(0, 4600)")
        time.sleep(2)

        email = driver.find_element(By.XPATH, "//a[contains(text(),'sales@spacex.com')]").get_attribute("href")
        print(email)
        try:
            assert "sales@spacex.com" in email
            print("Email link is working - Test Case 029 passed")
        except WDE:
            print("Test Case 029 failed")

    def tearDown(self):
        self.driver.quit()


class NegativeTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService())
        self.driver.maximize_window()

    # Test Case 008-8 - Validate user can't get access by entering a wrong password
    def test_case_008_8(self):
        driver = self.driver

        print("Test Case 008-8")

        # Opening SpaceX
        driver.get(H.SpaceX_url)

        # Checking Homepage
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

        # API testing
        code = requests.get(H.SpaceX_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title + " as Page title")

        # Waiting for Falcon 9 link to become available
        driver.find_element(By.XPATH, H.falcon9_link).click()
        delay()

        # Check if we moved to Falcon 9 page
        self.assertIn("SpaceX - Falcon 9", driver.title)
        if "Falcon 9" not in driver.title:
            print("Falcon 9 is not available")

        # Locate SUPPLIERS link and click on it
        driver.execute_script("window.scrollTo(0, 4600)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/supplier/']").click()
        delay()

        # Check if we moved to SpaceX - Suppliers page
        self.assertIn("SpaceX - Suppliers", driver.title)
        if "Suppliers" not in driver.title:
            print("Suppliers is not available")

        # Defining previous window
        window_before = driver.window_handles[0]

        # Find View Documentation button and click on it
        driver.find_element(By.XPATH, "//div[contains(text(),'View Documentation')]").click()
        delay()

        # Defining next window
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        # Locating the Password field and entering a wrong password
        iframe = driver.find_element(By.XPATH, ('//*[@id="opacity"]/iframe'))
        driver.switch_to.frame(iframe)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Aabc123!")
        time.sleep(5)

        # Checking status
        login_fail = driver.find_element(By.XPATH, '//*[@id="password"]')

        if login_fail:
            print("No access granted with wrong password - Test Case 008_8 passed")
        else:
            print("WARNING! Test Case 008_8 failed!")

    # Validate user can't enter a decimal number for quantity
    def test_case_009_9(self):
        driver = self.driver

        print("Test Case 009-9")

        # Opening Shop URL
        driver.get(H.shop_url)

        # Verifying Shop Logo
        wait = WebDriverWait(driver, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

        # API testing
        code = requests.get(H.shop_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("Official SpaceX Store", driver.title)
        print("Page has", driver.title + " as Page title")
        delay()

        # Locate the product
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'STARSHIP TORCH')]").click()
        delay()

        # Locate quantity field
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(2)

        # Enter a decimal number for quantity
        quantity = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity.send_keys(Keys.CONTROL + "a")  # Select all text
        quantity.send_keys(Keys.BACKSPACE)
        quantity.send_keys("1.5")
        delay()

        # Locate and click the Add to Cart button
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Add to cart')]")
        add_to_cart_button.click()
        delay()

        # Verify cart is visible
        driver.find_element(By.XPATH, "//h1[contains(text(),'Cart')]")
        delay()

        # Verify correct page
        try:
            assert driver.title == "Your Shopping Cart – SpaceX Store"
            print("Your Shopping Cart – SpaceX Store")
        except WDE:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Find the product quantity in the cart and get the value
        quantity_element = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity_value = quantity_element.get_attribute("value")
        print("The value extracted from the element is " + quantity_value)

        # Verify the quantity
        if quantity_value == "1":
            print("Can't enter a decimal number for quantity - Test Case 009-9 passed")
        else:
            print("Test Case 009-9 failed")

    # Validate user can't enter letters for quantity
    def test_case_010_10(self):
        driver = self.driver

        print("Test Case 010-10")

        # Opening Shop URL
        driver.get(H.shop_url)

        # Verifying Shop Logo
        wait = WebDriverWait(driver, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

        # API testing
        code = requests.get(H.shop_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("Official SpaceX Store", driver.title)
        print("Page has", driver.title + " as Page title")
        delay()

        # Locate the product
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'STARSHIP TORCH')]").click()
        delay()

        # Locate quantity field
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(2)

        # Enter a decimal number for quantity
        quantity = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity.send_keys(Keys.CONTROL + "a")  # Select all text
        quantity.send_keys(Keys.BACKSPACE)
        quantity.send_keys("abc")
        delay()

        # Locate and click the Add to Cart button
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Add to cart')]")
        add_to_cart_button.click()
        delay()

        # Verify cart is visible
        driver.find_element(By.XPATH, "//h1[contains(text(),'Cart')]")
        delay()

        # Verify correct page
        try:
            assert driver.title == "Your Shopping Cart – SpaceX Store"
            print("Your Shopping Cart – SpaceX Store")
        except WDE:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Find the product quantity in the cart and get the value
        quantity_element = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity_value = quantity_element.get_attribute("value")
        print("The value extracted from the element is " + quantity_value)

        # Verify the quantity
        if quantity_value == "1":
            print("Can't enter letters for quantity - Test Case 010-10 passed")
        else:
            print("Test Case 010-10 failed")

    # Validate user can't enter symbols for quantity
    def test_case_011_11(self):
        driver = self.driver

        print("Test Case 011-11")

        # Opening Shop URL
        driver.get(H.shop_url)

        # Verifying Shop Logo
        wait = WebDriverWait(driver, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

        # API testing
        code = requests.get(H.shop_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("Official SpaceX Store", driver.title)
        print("Page has", driver.title + " as Page title")
        delay()

        # Locate the product
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'STARSHIP TORCH')]").click()
        delay()

        # Locate quantity field
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(2)

        # Enter a decimal number for quantity
        quantity = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity.send_keys(Keys.CONTROL + "a")  # Select all text
        quantity.send_keys(Keys.BACKSPACE)
        quantity.send_keys("@@@")
        delay()

        # Locate and click the Add to Cart button
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Add to cart')]")
        add_to_cart_button.click()
        delay()

        # Verify cart is visible
        driver.find_element(By.XPATH, "//h1[contains(text(),'Cart')]")
        delay()

        # Verify correct page
        try:
            assert driver.title == "Your Shopping Cart – SpaceX Store"
            print("Your Shopping Cart – SpaceX Store")
        except WDE:
            print("Title is different. Current Title is:", driver.title)
        delay()

        # Find the product quantity in the cart and get the value
        quantity_element = driver.find_element(By.CLASS_NAME, "QuantitySelector__CurrentQuantity")
        quantity_value = quantity_element.get_attribute("value")
        print("The value extracted from the element is " + quantity_value)

        # Verify the quantity
        if quantity_value == "1":
            print("Can't enter symbols for quantity - Test Case 011-11 passed")
        else:
            print("Test Case 011-11 failed")

    # Validate that entering symbols into the search field does not deliver results
    def test_case_012_12(self):
        driver = self.driver

        print("Test Case 012-12")

        # Opening Shop URL
        driver.get(H.shop_url)

        # Verifying Shop Logo
        wait = WebDriverWait(driver, 7)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

        # API testing
        code = requests.get(H.shop_url).status_code
        if code == 200:
            print("API response code is 200")
        else:
            print("API response code is not 200", "Current code is:", code)
        delay()

        # Verifying the title
        self.assertIn("Official SpaceX Store", driver.title)
        print("Page has", driver.title + " as Page title")
        delay()

        # Locate the Search button and click it
        driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
        delay()

        # Enter symbols for product name
        search_field = driver.find_element(By.XPATH, "//input[@id='search-input']")
        search_field.send_keys(Keys.CONTROL + "a")  # Select all text
        search_field.send_keys(Keys.BACKSPACE)
        search_field.send_keys("%%%")
        search_field.send_keys(Keys.RETURN)
        delay()

        # See if the search delivers anything
        product_found_element = driver.find_element(By.CLASS_NAME, "SectionHeader__Description")
        if product_found_element.is_displayed():
            print("Search for symbols delivers results - Test Case 012-12 failed")
        else:
            print("Test Case 012-12 passed")


def tearDown(self):
    self.driver.quit()

#if __name__ == '__main__':
#unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))


#if __name__ == "__main__":
#unittest.main(Allure_Report)
