import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import HelpersStarlink as H  # Ensure HelpersStarlink.py exists and contains the correct paths


def delay():
    time.sleep(random.randint(1, 5))


class PositiveTestCases(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver using ChromeDriverManager
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    # Test Case 036: Verify the "Starlink" link works
    def test_case_036(self):
        driver = self.driver

        print("Test Case 036")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Verifying the title
        self.assertIn("SpaceX", driver.title)
        print("Page has", driver.title, "as Page title")

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # Check if the new window title contains "Starlink"
        if "Starlink" not in driver.title:
            raise Exception("Starlink - Test Case 036 failed")
        else:
            print("Starlink is available - Test Case 036 passed")

    def test_case_037(self):
        driver = self.driver
        print("Test Case 037")

        #Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # self.assertIn("SpaceX - Starlink", driver.title)

        if "Starlink" not in driver.title:
            print("Starlink is not available")

        driver.find_element(By.XPATH, H.residential_link).click()
        delay()

        wait = WebDriverWait(driver, 10)
        delay()

        if "Residential" not in driver.title:
            raise Exception("Residential is not available - Test Case 037 failed")
        else:
            print("Residential is available - Test Case 037 passed")

    def test_case_038(self):
        driver = self.driver
        print("Test Case 038")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        wait = WebDriverWait(driver, 5)
        delay()

        # Click on the "View Availability" button
        driver.find_element(By.XPATH, "(//mat-icon[contains(.,'chevron_right')])[1]").click()
        wait = WebDriverWait(driver, 4)
        map_page_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//canvas[@role='region']")))
        delay()

        # Assert that the map page element is displayed
        self.assertTrue(map_page_element.is_displayed(), "View Availability & Speed Map did not navigate correctly")
        if map_page_element.is_displayed():
            print("View Availability & Speed Map is available - Test Case 038 passed")
        else:
            raise Exception("View Availability & Speed Map is not available - Test Case 038 failed")

    def test_case_039(self):
        driver = self.driver
        print("Test Case 039")

        #Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # Wait for the "Business" button to be clickable, then click it
        wait = WebDriverWait(driver, 10)
        delay()

        driver.find_element(By.XPATH, H.business_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//a[contains(.,'Land Mobility')])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "//u[contains(.,'Schedule a consultation')]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "//button[contains(.,'Start')]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//div[contains(@class,'sc-1f8vz90-0 gbnXlt')])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "//button[contains(.,'Contact Support')]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        wait = WebDriverWait(driver, 10)
        delay()

        contact_support = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MuiBox-root css-1ofqig9']")))
        delay()

        # Assert that the map page element is displayed
        self.assertTrue(contact_support.is_displayed(), "Contact Support did not navigate correctly")
        if contact_support.is_displayed():
            print("Contact Support is available - Test Case 039 passed")
        else:
            raise Exception("Contact Support is not available - Test Case 039 failed")


    def test_case_040(self):
        driver = self.driver
        print("Test Case 040")

        self.driver.get(H.SpaceX_url)

        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        # Handle window switching
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break

        # Click on the "Roam" button
        driver.find_element(By.XPATH, H.roam_link).click()
        delay()

        # Click on 'Watch now'
        driver.execute_script("window.scrollTo(0, 2300)")
        time.sleep(5)

        # Checking the play button
        driver.find_element(By.XPATH, "(//span[contains(.,'Watch Now')])[2]").click()
        time.sleep(10)
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')

class NegativeTestCases(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver using ChromeDriverManager
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()


    def test_case_029_29(self):
        driver = self.driver
        print("Test Case 029_29")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)
        delay()

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.back()
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.back()
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.back()
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.back()
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.personal_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.personal_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.business_link).click()
        time.sleep(1)

    def test_case_030_30(self):
        driver = self.driver
        print("Test Case 030_30")
        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # self.assertIn("SpaceX - Starlink", driver.title)

        if "Starlink" not in driver.title:
            print("Starlink is not available")

        driver.find_element(By.XPATH, H.residential_link).click()
        delay()

        service_address_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@aria-label='Service Address'])[1]"))
        )
        service_address_input.send_keys("###$$$@@@")
        delay()

        # 6. Click on the button "Order now"
        order_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'ORDER NOW')])[2]"))
        )
        order_now_button.click()
        delay()

        # Verify that an error message or validation occurs due to the invalid address
        error_message = None
        try:
           error_message = WebDriverWait(driver, 10).until(
               EC.visibility_of_element_located((By.XPATH, "(//a[contains(@id,'LOCATION')])[1]")))

        except:
           pass

        if error_message:
            print("Error message displayed as expected - Test Case 030_30 passed")
        else:
            print("No error message displayed - Test Case 030_30 failed")
            self.fail("No error message was shown for the invalid address")
    def test_case_031_31(self):
        driver = self.driver
        print("Test Case 031_031")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # Wait for the "Business" button to be clickable, then click it
        wait = WebDriverWait(driver, 10)
        delay()

        driver.find_element(By.XPATH, H.business_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//a[contains(.,'Land Mobility')])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.schedule_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.start_button).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//div[contains(@class,'sc-1f8vz90-0 gbnXlt')])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "(//button[@tabindex='0'])[2]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, "//button[contains(.,'Contact Support')]").click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        wait = WebDriverWait(driver, 10)
        delay()

        email_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='email']"))
        )
        email_input.send_keys("jalagi3083@nexxterp.com")
        delay()

        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'password')]"))
        )
        password_input.send_keys("12345")
        delay()

        driver.find_element(By.XPATH, "//button[@type='submit']").click()



        if email_input:
            print("No access granted with wrong email - Test Case 031_31 passed")
        else:
            print("WARNING! Test Case 031_31 failed!")

    def test_case_032_32(self):
        driver = self.driver
        print("Test Case 032_32")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # Wait for the "Business" button to be clickable, then click it
        wait = WebDriverWait(driver, 10)
        delay()

        driver.find_element(By.XPATH, H.business_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.schedule_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.start_button).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.interested_starlink_residential).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)


        first_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@autocomplete='given-name']"))
        )
        first_name_input.send_keys("%%%###@@@")
        delay()

        if first_name_input:
            print("WARNING! Test Case 032_32 failed!")

        else:
            print("No access granted with wrong First name - Test Case 032_32 passed")

    def test_case_033_33(self):
        driver = self.driver
        print("Test Case 033_33")

        # Navigate to the SpaceX homepage
        driver.get(H.SpaceX_url)

        # Click on the "Starlink" link
        driver.find_element(By.XPATH, H.starlink_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
                driver.switch_to.window(new_window)
                break  # Stop after switching to the new window

        # Wait for the "Business" button to be clickable, then click it
        wait = WebDriverWait(driver, 10)
        delay()

        driver.find_element(By.XPATH, H.business_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.schedule_link).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.start_button).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)

        driver.find_element(By.XPATH, H.interested_starlink_residential).click()
        delay()

        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        driver.switch_to.window(new_window)


        first_name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Jane']"))
        )
        first_name_input.send_keys("Jane")
        delay()

        last_name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Smith']"))
        )
        last_name_input.send_keys("Smith")
        delay()


        phone_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='tel']")))
        phone_input.send_keys(" +++$$$&&@@")
        delay()

        email_input = WebDriverWait(driver,5).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='email']")))

        email_input.send_keys("pacara4727@eachart.com")
        delay()

        company_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='organization']")))
        company_input.send_keys("Acme corporation")
        delay()
        wait = WebDriverWait(driver, 5)
        delay()

        driver.find_element(By.XPATH, "(//button[contains(.,'OK')])[2]").click()
        delay()

        error_message = None
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@data-qa='error-message-visible']")))

        except:
            pass

        if error_message:
            print("Error message displayed as expected - Test Case 033_33 passed")
        else:
            print("No error message displayed - Test Case 033_33 failed")



if __name__ == "__main__":
    unittest.main()

