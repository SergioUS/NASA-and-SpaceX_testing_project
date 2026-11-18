#Unittest scripts for Positive and Negative TC for Starlink website

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import random
import time
import Starlink_A_Helpers_Volha_Antsipenka as H
# import AllureReports
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service

fake= Faker()

def delay():
    time.sleep(random.randint(2,5))

# def scroll_to_element(iframe):
#     pass



class ChromePositiveTC(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy= 'eager'
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.set_window_size(1920, 1080)

    def test_case_011(self):
        driver = self.driver
        print("\nStarlink\n--------\nChrome Browser testing\n\nPositive test cases:\n\nTC_011")

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Click "Get Started"
        H.wait_and_click(driver, H.getstarted_button)

        #Enter address and select it from dropdown menu
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address: {H.test_address} and selected from dropdown")


        # 5.Verify availability and pricing
        is_available = verify_availability_and_pricing(driver, timeout=15)
        self.assertTrue(is_available, "Availability and pricing not displayed for valid address")





    def test_case_012(self):
        driver = self.driver
        print("\nTC_012")



    def test_case_013(self):
        driver = self.driver
        print("\nTC_013")



    def test_case_014(self):
        driver = self.driver
        print("\nTC_014")



    def test_case_015(self):
        driver = self.driver
        print("\nTC_015")




class ChromeNegativeTC(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here





# if __name__ == '__main__':
#     unittest.main()
