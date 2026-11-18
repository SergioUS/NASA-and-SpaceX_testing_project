#Unittest scripts for Positive and Negative TC for Starlink website

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import random
import time
import Starlink_B_Helpers_Volha_Antsipenka as H
from faker import Faker


fake= Faker()

def delay():
    time.sleep(random.randint(2,5))



class ChromePositiveTC(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy= 'eager'
        options.add_argument('--headless')
        options.add_argument("--lang=en-US")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

    print("\nStarlink\n--------\nChrome Browser testing\n\nPositive test cases:")

    def test_case_P_011(self):
        driver = self.driver
        print("\n\nTC_P_011")
        #TC_P_011 Checks service availability on main page with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        print("\nTC_P_011 - PASS")


    def test_case_P_012(self):
        driver = self.driver
        print("\nTC_P_012")
        #TC_P_012 Checks service availability on coverage map with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Hover over 'Learn' button and click on 'Availability map' button from dropdown menu
        H.hover_over(driver, H.learn_button)
        H.wait_and_click(driver, H.map_button)
        print("\nOpened availability map")
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Click 'Get started' button and verify order page loaded and displays availability and pricing
        H.wait_and_click(driver, H.map_getstarted_button)
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        print("\nTC_P_012 - PASS")


    def test_case_P_013(self):
        driver = self.driver
        print("\n\nTC_P_013")
        #TC_P_013 Checks possibility to proceed from 'Get started' to 'Checkout' with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        print("\nTC_P_013 - PASS")


    def test_case_P_014(self):
        driver = self.driver
        print("\nTC_P_014")
        #TC_P_014 Verifies that checkout page accepts valid input data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        #Enter valid personal information and proceed to payment
        H.fill_input_field(driver, H.email_input_field, fake.email())
        H.fill_input_field(driver, H.first_name_input_field, fake.first_name())
        H.fill_input_field(driver, H.last_name_input_field, fake.last_name())
        H.fill_input_field(driver, H.phone_input_field, fake.basic_phone_number())
        H.fill_input_field(driver, H.cardholder_name_input_field, fake.name())
        H.fill_iframe_input_field(driver, H.iframe_card_number, H.card_number_input_field, fake.credit_card_number())
        H.fill_iframe_input_field(driver, H.iframe_mm_yy, H.mm_yy_input_field, fake.credit_card_expire())
        H.fill_iframe_input_field(driver, H.iframe_cvc, H.cvc_input_field, fake.credit_card_security_code())
        print("\nEntered all personal information")

        H.verify_no_error_message(driver, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_card_number, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_cvc, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_mm_yy, H.error_message)

        print("\nTC_P_014 - PASS")


    def test_case_P_015(self):
        driver = self.driver
        print("\nTC_P_015")
        #TC_P_015 Verifies that you can't sign in into unregistered account

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Go to user account, enter valid unregistered email and verify that website does not let you in
        H.wait_and_click(driver, H.user_account_icon)
        H.fill_input_field(driver, H.account_email_input_field, fake.email())
        print("\nEntered valid unregistered email address")

        H.wait_and_click(driver, H.next_button)
        H.fill_input_field(driver, H.password_input, fake.password())
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        H.verify_error_message(driver, H.email_not_found_error_message)

        print("\nTC_P_015 - PASS")


    def tearDown(self):
        self.driver.quit()



class ChromeNegativeTC(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        options.add_argument("--lang=en-US")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

    print("\nStarlink\n--------\nChrome Browser testing\n\nNegative test cases:")

    def test_case_N_011(self):
        driver = self.driver
        print("\n\nTC_N_011")
        #TC_N_011 Checks service availability on main page with invalid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)

        print("\nTC_N_011 - PASS")


    def test_case_N_012(self):
        driver = self.driver
        print("\nTC_N_012")
        #TC_N_012 Checks service availability on coverage map with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Hover over 'Learn' button and click on 'Availability map' button from dropdown menu
        H.hover_over(driver, H.learn_button)
        H.wait_and_click(driver, H.map_button)
        print("\nOpened availability map")
        delay()

        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)

        print("\nTC_N_012 - PASS")


    def test_case_N_013(self):
        driver = self.driver
        print("\n\nTC_N_013")
        #TC_N_013 Checks possibility to proceed from 'Get started' to 'Checkout' with invalid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)
        print("\nWebsite does not let you to checkout with invalid address")

        print("\nTC_N_013 - PASS")


    def test_case_N_014(self):
        driver = self.driver
        print("\nTC_N_014")
        #TC_N_014 Verifies that checkout page does not accept invalid input data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        #Enter invalid personal information and click Enter
        H.fill_input_field(driver, H.email_input_field, H.invalid_test_email)
        H.fill_input_field(driver, H.first_name_input_field, fake.first_name())
        H.fill_input_field(driver, H.last_name_input_field, fake.last_name())
        H.fill_input_field(driver, H.phone_input_field, fake.phone_number())
        H.fill_input_field(driver, H.cardholder_name_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_card_number, H.card_number_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_mm_yy, H.mm_yy_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_cvc, H.cvc_input_field, H.invalid_test_input)
        print("\nEntered invalid personal information")
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        delay()

        #Verify that service shows error message for invalid data input
        H.verify_error_message(driver, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_card_number, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_cvc, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_mm_yy, H.error_message)

        print("\nTC_N_014 - PASS")


    def test_case_N_015(self):
        driver = self.driver
        print("\nTC_N_015")
        #TC_N_015 Verifies that you can't sign in into account with invalid data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Go to user account, enter invalid email and verify that website does not let you in
        H.wait_and_click(driver, H.user_account_icon)
        H.fill_input_field(driver, H.account_email_input_field, H.invalid_test_email)
        print(f"\nEntered invalid email address: {H.invalid_test_email}")

        H.wait_and_click(driver, H.next_button)
        H.verify_error_message(driver, H.invalid_data_error_message)

        print("\nTC_N_015 - PASS")


    def tearDown(self):
        self.driver.quit()



class EdgePositiveTC(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.page_load_strategy= 'eager'
        options.add_argument('--headless')
        options.add_argument("--lang=en-US")
        self.driver = webdriver.Edge(options=options)
        self.driver.set_window_size(1920, 1080)

    print("\nStarlink\n--------\nEdge Browser testing\n\nPositive test cases:")

    def test_case_P_011(self):
        driver = self.driver
        print("\n\nTC_P_011")
        #TC_P_011 Checks service availability on main page with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        print("\nTC_P_011 - PASS")


    def test_case_P_012(self):
        driver = self.driver
        print("\nTC_P_012")
        #TC_P_012 Checks service availability on coverage map with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Hover over 'Learn' button and click on 'Availability map' button from dropdown menu
        H.hover_over(driver, H.learn_button)
        H.wait_and_click(driver, H.map_button)
        print("\nOpened availability map")
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Click 'Get started' button and verify order page loaded and displays availability and pricing
        H.wait_and_click(driver, H.map_getstarted_button)
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        print("\nTC_P_012 - PASS")


    def test_case_P_013(self):
        driver = self.driver
        print("\n\nTC_P_013")
        #TC_P_013 Checks possibility to proceed from 'Get started' to 'Checkout' with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        print("\nTC_P_013 - PASS")


    def test_case_P_014(self):
        driver = self.driver
        print("\nTC_P_014")
        #TC_P_014 Verifies that checkout page accepts valid input data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        #Enter valid personal information and proceed to payment
        H.fill_input_field(driver, H.email_input_field, fake.email())
        H.fill_input_field(driver, H.first_name_input_field, fake.first_name())
        H.fill_input_field(driver, H.last_name_input_field, fake.last_name())
        H.fill_input_field(driver, H.phone_input_field, fake.basic_phone_number())
        H.fill_input_field(driver, H.cardholder_name_input_field, fake.name())
        H.fill_iframe_input_field(driver, H.iframe_card_number, H.card_number_input_field, fake.credit_card_number())
        H.fill_iframe_input_field(driver, H.iframe_mm_yy, H.mm_yy_input_field, fake.credit_card_expire())
        H.fill_iframe_input_field(driver, H.iframe_cvc, H.cvc_input_field, fake.credit_card_security_code())
        print("\nEntered all personal information")

        H.verify_no_error_message(driver, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_card_number, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_cvc, H.error_message)
        H.verify_no_error_message_iframe(driver, H.iframe_mm_yy, H.error_message)

        print("\nTC_P_014 - PASS")


    def test_case_P_015(self):
        driver = self.driver
        print("\nTC_P_015")
        #TC_P_015 Verifies that you can't sign in into unregistered account

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Go to user account, enter valid unregistered email and verify that website does not let you in
        H.wait_and_click(driver, H.user_account_icon)
        H.fill_input_field(driver, H.account_email_input_field, fake.email())
        print("\nEntered valid unregistered email address")

        H.wait_and_click(driver, H.next_button)
        H.fill_input_field(driver, H.password_input, fake.password())
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        H.verify_error_message(driver, H.email_not_found_error_message)

        print("\nTC_P_015 - PASS")


    def tearDown(self):
        self.driver.quit()



class EdgeNegativeTC(unittest.TestCase):
    def setUp(self):
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        options.add_argument("--lang=en-US")
        self.driver = webdriver.Edge(options=options)
        self.driver.set_window_size(1920, 1080)

    print("\nStarlink\n--------\nEdge Browser testing\n\nNegative test cases:")

    def test_case_N_011(self):
        driver = self.driver
        print("\n\nTC_N_011")
        #TC_N_011 Checks service availability on main page with invalid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()


        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)

        print("\nTC_N_011 - PASS")


    def test_case_N_012(self):
        driver = self.driver
        print("\nTC_N_012")
        #TC_N_012 Checks service availability on coverage map with valid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Hover over 'Learn' button and click on 'Availability map' button from dropdown menu
        H.hover_over(driver, H.learn_button)
        H.wait_and_click(driver, H.map_button)
        print("\nOpened availability map")
        delay()

        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)

        print("\nTC_N_012 - PASS")


    def test_case_N_013(self):
        driver = self.driver
        print("\n\nTC_N_013")
        #TC_N_013 Checks possibility to proceed from 'Get started' to 'Checkout' with invalid address

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter invalid address and click Enter
        H.fill_input_field(driver, H.address_input_field, H.invalid_test_address)
        print(f"\nEntered invalid address {H.invalid_test_address}")
        ActionChains(driver).send_keys(Keys.ENTER).perform()

        #Verify that service shows error message 'Please select an address from the suggestions'
        H.verify_error_message(driver, H.invalid_address_error)
        print("\nWebsite does not let you to checkout with invalid address")

        print("\nTC_N_013 - PASS")


    def test_case_N_014(self):
        driver = self.driver
        print("\nTC_N_014")
        #TC_N_014 Verifies that checkout page does not accept invalid input data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Enter address and select it from dropdown list
        H.enter_address(driver, H.address_input_field, H.address_dropdown, H.test_address)
        print(f"\nEntered address {H.test_address} and selected it from dropdown list")

        #Verify order page loaded and displays availability and pricing
        H.verify_availability_and_pricing(driver, H.order_page_locator)

        #Click 'Checkout' button and verify checkout page loaded successfully
        H.wait_and_click(driver, H.checkout_button)
        H.verify_checkout_page(driver, H.checkout_page_locator)

        #Enter invalid personal information and click Enter
        H.fill_input_field(driver, H.email_input_field, H.invalid_test_email)
        H.fill_input_field(driver, H.first_name_input_field, fake.first_name())
        H.fill_input_field(driver, H.last_name_input_field, fake.last_name())
        H.fill_input_field(driver, H.phone_input_field, fake.phone_number())
        H.fill_input_field(driver, H.cardholder_name_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_card_number, H.card_number_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_mm_yy, H.mm_yy_input_field, H.invalid_test_input)
        H.fill_iframe_input_field(driver, H.iframe_cvc, H.cvc_input_field, H.invalid_test_input)
        print("\nEntered invalid personal information")
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        delay()

        #Verify that service shows error message for invalid data input
        H.verify_error_message(driver, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_card_number, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_cvc, H.error_message)
        H.verify_error_message_iframe(driver, H.iframe_mm_yy, H.error_message)

        print("\nTC_N_014 - PASS")


    def test_case_N_015(self):
        driver = self.driver
        print("\nTC_N_015")
        #TC_N_015 Verifies that you can't sign in into account with invalid data

        #Open Starlink website and verify title and logo
        driver.get(H.Starlink_url)

        H.assert_title(driver, "Starlink")
        delay()

        H.assert_logo(driver, H.homepage_logo)
        delay()

        #Go to user account, enter invalid email and verify that website does not let you in
        H.wait_and_click(driver, H.user_account_icon)
        H.fill_input_field(driver, H.account_email_input_field, H.invalid_test_email)
        print(f"\nEntered invalid email address: {H.invalid_test_email}")

        H.wait_and_click(driver, H.next_button)
        H.verify_error_message(driver, H.invalid_data_error_message)

        print("\nTC_N_015 - PASS")


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
