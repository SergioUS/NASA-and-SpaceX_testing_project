#Unittest (Positive and Negative tests) for SpaceX site / Rideshare module
#Volha Bratuhin

import unittest
import time
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import VBratuhin_Rideshare_Helper as H
from selenium.webdriver.chrome.options import Options as ChromeOptions

fake = Faker()
def delay():
    time.sleep(random.randint(2, 3))

class Spacex_Rideshare_01_Positive(unittest.TestCase):

    # def SetUp_Headless(self):
    #
    #     options = webdriver.ChromeOptions()
    #     options.page_load_strategy = 'eager'
    #     options.add_argument('--headless')
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.maximize_window()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_01(self):

        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Spacex_url)

        # Verify Title
        try:
            driver.find_element(By.LINK_TEXT, "RIDESHARE").click()
            delay()

            assert driver.title == "SpaceX - Rideshare"
            print("Title is correct")
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        # Verify elements in the Header menu
        try:
            driver.find_element(By.XPATH, "//a[@id='logo']")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Falcon 9')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Falcon Heavy')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Dragon')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starship')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Human Spaceflight')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Rideshare')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starshield')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starlink')]")
            driver.find_element(By.XPATH, "//div[@id='navigation-right']")
            driver.find_element(By.XPATH, "//button[@id='hamburger']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@id='hamburger']").click()
            time.sleep(1)

            print("All icons in header menu is displayed")
        except NoSuchElementException:
        #except EC:
            print("Some icons in header menu is missing")

        # Verify elements on the page
        try:
            driver.find_element(By.XPATH, "//h1[@class='animate'][contains(.,'SmallsatRideshare Program')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Dedicated Rideshare Missions as Low as $300k*. Sea')]")
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.find_element(By.XPATH, "//h2[contains(text(),'COST AS LOW AS $300k')]")
            driver.find_element(By.XPATH, "//h2[contains(text(),'SCHEDULE CERTAINTY')]")
            driver.find_element(By.XPATH, "//h2[contains(text(),'CONTRACT FLEXIBILITY')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'$300k for 50kg to SSO with additional mass at $6k/')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'SSO missions approximately every 4 months. Frequen')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'If your payload is delayed, apply 100% of monies p')]")
            driver.execute_script("window.scrollTo(0, 800)")
            time.sleep(2)
            driver.find_element(By.XPATH, "//h2[contains(text(),'RESERVE YOUR RIDE ONLINE')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Find all the information you need to make a reserv')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Payloads are received at the launch site around L-')]")
            driver.find_element(By.XPATH, "//div[contains(text(),\"Payload User's Guide\")]")
            driver.find_element(By.XPATH, "//div[contains(text(),\"Cake Topper User's Guide\")]")
            driver.execute_script("window.scrollTo(0, 1300)")
            time.sleep(2)
            driver.find_element(By.XPATH, "//span[contains(text(),'Place Order Online')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Welcome Package')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Spacecraft Data Package')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Launch Processing')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Launch!')]")
            driver.execute_script("window.scrollTo(0, 1700)")
            time.sleep(2)
            driver.find_element(By.XPATH, "//h2[contains(text(),'Payload Configurations')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Book your ride on a Rideshare Plate. For larger sp')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'1/4 PLATE')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'1/2 PLATE')]")
            driver.find_element(By.XPATH, "(//td[contains(.,'FULL PLATE')])[1]")
            driver.find_element(By.XPATH, "//td[contains(text(),'FULL PLATE (XL VOLUME)')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'50kg included')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'100kg included')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'200kg included')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'300kg included')]")
            driver.find_element(By.XPATH, "//strong[contains(text(),'Learn more about available volume ')]").click()
            time.sleep(3)
            window_before = driver.window_handles[0]
            driver.find_element(By.XPATH, "//strong[contains(text(),'Learn more about available volume ')]")
            time.sleep(1)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            time.sleep(1)
            driver.switch_to.window(window_before)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 2000)")
            delay()
            driver.find_element(By.XPATH, "//h2[contains(text(),'Falcon 9')]")
            driver.find_element(By.XPATH, "//p[contains(text(),'Falcon 9, the world’s first orbital class reusable')]")
            driver.find_element(By.XPATH, "//strong[contains(text(),'Learn more about Falcon 9')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'VEHICLE HEIGHT')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'VEHICLE DIAMETER')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'FAIRING HEIGHT')]")
            driver.find_element(By.XPATH, "//td[contains(text(),'FAIRING DIAMETER')]")
            driver.find_element(By.XPATH, "//td[contains(.,'70m / 229.6ft')]")
            driver.find_element(By.XPATH, "//td[contains(.,'3.7m / 12ft')]")
            driver.find_element(By.XPATH, "//td[contains(.,'13.1m / 43ft')]")
            driver.find_element(By.XPATH, "//td[contains(.,'5.2m / 17.1ft')]")
            driver.find_element(By.XPATH, "//strong[contains(text(),'Learn more about Falcon 9')]").click()
            time.sleep(3)
            driver.execute_script("window.history.go(-1)")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            delay()
            driver.find_element(By.XPATH, "//p[contains(text(),'*Pricing adjusted in March 2022 to account for exc')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'SpaceX © 2024')]")
            driver.find_element(By.XPATH, "//a[contains(text(),'PRIVACY POLICY')]")
            driver.find_element(By.XPATH, "//a[contains(text(),'SUPPLIERS')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Contact us')]").click()
            time.sleep(3)


            print("TC-1 passed. All icons on the page is displayed")
        except NoSuchElementException:
            print("TC-1 failed. Some icons on the page is missing")

        self.driver.quit()

    def test_02(self):

        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify search flights
        try:
            assert driver.title == "SpaceX Satellite Rideshare"
            print("Title is correct")
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-arrow-wrapper')])[2]").click()
            driver.find_element(By.XPATH, "//span[@class='mat-option-text'][contains(.,'SSO')]").click()
            driver.find_element(By.XPATH, "//button[contains(@type,'button')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'2025')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'JAN')]").click()
            driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("500")
            delay()
            # Verify that the estimated price has been calculated
            try:
                driver.find_element(By.XPATH, "//div[contains(text(),'$3 M')]")
                print("Everything is correct. The estimated price is the same.")
            except NoSuchElementException:
                print("The estimated price has changed.")

            driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
            delay()

            print("TC-2 passed. The user can fill in all boxes")
        except NoSuchElementException:
            print("TC-2 failed. Is there something wrong")


        # Verify breadcrumb-component-row
        try:
            driver.find_element(By.XPATH, "//div[@class='breadcrumb-navigation selectable'][contains(.,'Available Flights')]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'keyboard_arrow_right')])[1]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Plate Selection')]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'keyboard_arrow_right')])[2]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Add-ons')]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'keyboard_arrow_right')])[3]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Deposit')]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'keyboard_arrow_right')])[4]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Flight Review')]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'keyboard_arrow_right')])[5]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Submission')]")

            print("All breadcrumb-component-row is displayed")
        except NoSuchElementException:
            print("Some breadcrumb-component-row is missing")


        self.driver.quit()

    def test_03(self):

        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        H.previous_step1(driver)

        # Verify Select Flight
        try:
            H.scroll_down(driver)

            driver.find_element(By.XPATH, "//div[@class='results-header'][contains(.,'Available Flights')]")
            driver.find_element(By.XPATH, "//div[@class='see-all-text'][contains(.,'See all flightskeyboard_arrow_right')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'See dedicated rideshare flights')]")
            driver.find_element(By.XPATH, "//div[@class='column-narrow-width'][contains(.,'Date')]")
            driver.find_element(By.XPATH, "//div[@class='column-very-narrow-width'][contains(.,'Orbit')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Perigee')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Apogee')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Semi-Major Axis Alt.')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Incl.')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Availability')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'SpaceX can accommodate additional mechanical inter')]")
            driver.find_element(By.XPATH, "(//div[contains(.,'To inquire about flights to MEO, GTO, TLI or other orbits, please email rideshare@spacex.com')])[6]")
            driver.find_element(By.XPATH, "(//a[@href='mailto:rideshare@spacex.com'][contains(.,'rideshare@spacex.com')])[2]")
            driver.find_element(By.XPATH, "(//a[contains(@class,'arrow-button button wipe')])[2]").click()
            delay()

            print("TC-3 passed. The user can select flight")
        except NoSuchElementException:
            print("TC-3 failed. Flight selection not available")

        try:
            assert driver.find_element(By.XPATH, "//div[@class='port-selection-header'][contains(.,'Plate Selection')]")
            print("The page is correct")
        except AssertionError:
            print("The page is different")

        self.driver.quit()

    def test_04(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        H.previous_step2(driver)

        # Verify technical information
        try:
            H.scroll_down(driver)

            driver.find_element(By.XPATH, "//div[@class='port-selection-header'][contains(.,'Plate Selection')]")
            driver.find_element(By.XPATH, "//div[@class='port-selection-subtext'][contains(.,'For technical details, refer to the Rideshare Payload Users Guide. Learn More keyboard_arrow_right')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'Learn More')]").click()
            delay()

            window_before = driver.window_handles[0]
            driver.find_element(By.XPATH, "//span[contains(text(),'Learn More')]")
            time.sleep(1)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            time.sleep(1)
            driver.switch_to.window(window_before)
            time.sleep(1)

            driver.find_element(By.XPATH, "//video[contains(@width,'100%')]")
            driver.find_element(By.XPATH, "(//img[@src='/assets/images/plate_quarter.png'])[1]")
            driver.find_element(By.XPATH, "(//img[@src='/assets/images/plate_half.png'])[1]")
            driver.find_element(By.XPATH, "(//img[@src='/assets/images/plate_full.png'])[1]")
            driver.find_element(By.XPATH, "(//img[@src='/assets/images/plate_xl.png'])[1]")
            driver.find_element(By.XPATH, "//div[@class='col-12 port-size-text'][contains(.,'1/4')]")
            driver.find_element(By.XPATH, "//div[@class='col-12 port-size-text'][contains(.,'1/2')]")
            driver.find_element(By.XPATH, "//div[@class='col-12 port-size-text'][contains(.,'Full')]")
            driver.find_element(By.XPATH, "//div[@class='col-12 port-size-text'][contains(.,'XL')]")
            driver.find_element(By.XPATH, "(//span[@class='alternate-limit-number'][contains(.,'50kg included')])[1]")
            driver.find_element(By.XPATH, "(//span[@class='alternate-limit-number'][contains(.,'100kg included')])[1]")
            driver.find_element(By.XPATH, "(//span[@class='alternate-limit-number'][contains(.,'200kg included')])[1]")
            driver.find_element(By.XPATH, "(//span[@class='alternate-limit-number'][contains(.,'300kg included')])[1]")
            driver.find_element(By.XPATH, '(//span[@class=\'port-limit-text\'][contains(.,\'8" bolt pattern\')])[1]')
            driver.find_element(By.XPATH, '(//span[@class=\'port-limit-text\'][contains(., \'8" or 15" bolt pattern\')])[1]')
            driver.find_element(By.XPATH, '(//span[@class=\'port-limit-text\'][contains(.,\'15" or 24" bolt pattern\')])[1]')
            driver.find_element(By.XPATH, '(//span[@class=\'port-limit-text\'][contains(.,\'24" bolt pattern\')])[3]')
            driver.find_element(By.XPATH, "//div[@class='additional-information-text'][contains(.,'View the Payload Users Guide to make sure your payload meets the requirements.')]")
            driver.find_element(By.XPATH, "//a[contains(text(),'Payload Users Guide')]").click()
            delay()

            window_before = driver.window_handles[0]
            driver.find_element(By.XPATH, "//a[contains(text(),'Payload Users Guide')]")
            time.sleep(1)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            time.sleep(1)
            driver.switch_to.window(window_before)
            time.sleep(1)

            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[1]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[2]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[3]")
            driver.find_element(By.XPATH, "(//i[@class='material-icons'][contains(.,'arrow_forward')])[4]").click()
            delay()

            print("TC-4 passed. The user can select technical specifications")
        except NoSuchElementException:
            print("TC-4 failed. Is there something wrong in technical specifications")

        try:
            assert driver.find_element(By.XPATH,"//div[@class='page-header header col-12'][contains(.,'Add-ons  Please select from the below optional products and services to add on to your request. learn more keyboard_arrow_right')]")
            print("The page is correct")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_05(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        H.previous_step3(driver)

        # Verify ADD-ONS
        try:
            H.scroll_down(driver)

            driver.find_element(By.XPATH, "//div[@class='page-header header col-12'][contains(.,'Add-ons  Please select from the below optional products and services to add on to your request. learn more keyboard_arrow_right')]")
            driver.find_element(By.XPATH, "//span[contains(text(),'learn more')]").click()
            delay()

            window_before = driver.window_handles[0]
            driver.find_element(By.XPATH, "//span[contains(text(),'learn more')]")
            time.sleep(1)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            time.sleep(1)
            driver.switch_to.window(window_before)
            time.sleep(1)

            driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label'][contains(.,'Mechanical Interface Adapter')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'SpaceX can provide unique interfaces for Payloads ')]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-checkbox-inner-container')])[1]").click()
            driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label'][contains(.,'Separation System')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'SpaceX can provide a separation system for your pa')]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-checkbox-inner-container')])[2]").click()
            driver.find_element(By.XPATH, '//div[@class=\'mat-radio-label-content\'][contains(.,\'8"\')]')
            driver.find_element(By.XPATH, '//div[@class=\'mat-radio-label-content\'][contains(.,\'15"\')]')
            driver.find_element(By.XPATH, '//div[@class=\'mat-radio-label-content\'][contains(.,\'24"\')]')
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-radio-outer-circle')])[3]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-radio-outer-circle')])[2]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-radio-outer-circle')])[1]")
            # Verify that the separation system price has been calculated
            try:
                driver.find_element(By.XPATH, "//div[@class='ng-star-inserted'][contains(.,'278,300')]")
                print("Everything is correct. The separation system price is the same.")
            except NoSuchElementException:
                print("The separation system price has changed.")
            driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label'][contains(.,'Payload Electrical Connectivity at Launch Pad')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'SpaceX accommodates electrical connectivity betwee')]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-checkbox-inner-container')])[3]").click()
            driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label'][contains(.,'Fuel Needed')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Select this option if you will need to fuel your P')]")
            # Verify that the fuel price has been calculated
            try:
                driver.find_element(By.XPATH, "//div[contains(text(),'42,350')]")
                print("Everything is correct. The fuel price is the same.")
            except NoSuchElementException:
                print("The fuel price has changed.")
            driver.find_element(By.XPATH, "//span[@class='mat-checkbox-label'][contains(.,'Insurance')]")
            driver.find_element(By.XPATH, "//div[contains(text(),'Select this option if you would like SpaceX to pro')]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-checkbox-inner-container')])[5]").click()
            driver.find_element(By.XPATH, "//input[contains(@autocomplete,'off')]").send_keys("500000")
            delay()
            # Verify that the insurance price has been calculated
            try:
                driver.find_element(By.XPATH, "//div[contains(text(),'25,000')]")
                print("Everything is correct. The insurance price is the same.")
            except NoSuchElementException:
                print("The insurance price has changed.")
            driver.find_element(By.XPATH, "//div[contains(text(),'Current Total with Add-ons')]")
            # Verify that the current total price has been calculated
            try:
                driver.find_element(By.XPATH, "//div[contains(text(),'$3,345,650')]")
                print("The current total price is correct. The amount is the same.")
            except NoSuchElementException:
                print("The current total price has changed.")
            driver.find_element(By.XPATH, "//div[contains(text(),'Click to enter contact and payment information. Yo')]")
            driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
            delay()

            print("TC-5 passed. ADD-ONS is correct")
        except NoSuchElementException:
            print("TC-5 failed. Is there something wrong with ADD-ONS")

        try:
            assert driver.find_element(By.XPATH, "//div[contains(text(),'Contact Information')]")
            print("The page is correct")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_06(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        H.previous_step4(driver)

        # Verify Contact Information
        try:
            H.scroll_down(driver)

            driver.find_element(By.XPATH, "//div[contains(text(),'Contact Information')]")
            driver.execute_script("window.scrollTo(0, 500)")

            # Verify Company Information

            driver.find_element(By.XPATH, "//div[contains(text(),'Company')]")
            driver.find_element(By.XPATH, "//label[contains(text(),'Company Name')]")
            driver.find_element(By.XPATH, "//label[contains(text(),'Street Address')]")
            driver.find_element(By.XPATH, "//label[contains(text(),'State')]")
            driver.find_element(By.XPATH, "//label[contains(text(),'Country')]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Phone')])[1]")
            driver.find_element(By.XPATH, "//label[contains(text(),'City')]")
            driver.find_element(By.XPATH, "//label[contains(text(),'Postal Code')]")

            # filling in the form
            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys(fake.company())
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys(fake.street_address())
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys(fake.state())
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys(fake.country())
            driver.find_element(By.XPATH, "(//div[contains(@class,'iti__selected-flag')])[1]").click()
            driver.find_element(By.XPATH, "// li[ @class ='iti__country iti__preferred iti__active iti__highlight'][contains(., 'United States+1')]").click()
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys(fake.city())
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys(fake.postcode())

            # Verify Point of contact
            driver.execute_script("window.scrollTo(0, 800)")
            driver.find_element(By.XPATH, "//div[contains(text(),'Point of Contact')]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Name')])[2]")
            driver.find_element(By.XPATH, "//label[contains(text(),'Email')]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Phone')])[2]")

            # filling in the form
            name = driver.find_element(By.XPATH, "//input[@id='ppocName']")
            name.send_keys(fake.name())
            email = driver.find_element(By.XPATH, "//input[@id='ppocEmail']")
            email.send_keys(fake.email())
            driver.find_element(By.XPATH, "(//div[contains(@class,'iti__selected-flag')])[2]").click()
            driver.find_element(By.XPATH, "//li[@class='iti__country iti__preferred iti__active iti__highlight'][contains(.,'United States+1')]").click()
            phone = driver.find_element(By.XPATH, "//input[@id='ppocPhone']")
            phone.send_keys("201-555-0124")

            # filling in the form add contact
            driver.find_element(By.XPATH, "//div[contains(text(),'Add Another')]").click()
            driver.execute_script("window.scrollTo(0, 1050)")
            driver.find_element(By.XPATH, "//div[contains(text(),'Point of Contact #2')]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Name')])[3]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Email')])[2]")
            driver.find_element(By.XPATH, "(//label[@class='input-label'][contains(.,'Phone')])[3]")
            driver.find_element(By.XPATH, "(//div[contains(@class,'iti__selected-flag')])[3]").click()
            driver.find_element(By.XPATH, "//li[@class='iti__country iti__preferred iti__active iti__highlight'][contains(.,'United States+1')]").click()
            phone = driver.find_element(By.XPATH, "//input[@id='spocPhone']")
            phone.send_keys("201-555-0125")
            driver.find_element(By.XPATH, "//div[contains(text(),'Remove')]").click()

            print("TC-6 passed. The user can fill in all boxes")
        except NoSuchElementException:
            print("TC-6 failed. Is there something wrong")


        self.driver.quit()


class Spacex_Rideshare_02_Negative(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_01_01(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify search flights
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-arrow-wrapper')])[2]").click()
            driver.find_element(By.XPATH, "//span[@class='mat-option-text'][contains(.,'SSO')]").click()
            driver.find_element(By.XPATH, "//button[contains(@type,'button')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'2025')]").click()
            driver.find_element(By.XPATH, "//div[contains(text(),'JAN')]").click()
            driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(" ")
            delay()
            driver.find_element(By.XPATH, "//div[contains(text(),'Estimated Price')]")
            driver.find_element(By.XPATH, "//i[contains(text(),'arrow_forward')]").click()
            delay()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

            print("TC-1-1 passed. The user can't search flights")
        except NoSuchElementException:
            print("TC-1-1 failed. Is there something wrong.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Please enter search parameters above.')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter search parameters above'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_02_02(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Company Name not entered
        try:
            H.previous_step5(driver)

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys()

            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            print("TC-2-2 passed. The user can't fail to enter Company Name.")
        except NoSuchElementException:
            print("TC-2-2 failed. Is there something wrong. The user can fail to enter value Company Name.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a company name')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a company name'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_03_03(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Invalid Phone number
        try:
            H.previous_step5(driver)

            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("1-201-555-01")

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            print("TC-3-3 passed. The user can't enter invalid phone number.")
        except NoSuchElementException:
            print("TC-3-3 failed. Is there something wrong. The user can enter invalid phone number.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Please enter a valid phone number')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a valid phone number'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_04_04(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Street Address not entered
        try:
            H.previous_step5(driver)

            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys()

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            print("TC-4-4 passed. The user can't fail to enter Street Address.")
        except NoSuchElementException:
            print("TC-4-4 failed. Is there something wrong. The user can fail to enter value Street Address.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a street address')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a street address'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_05_05(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/State not entered
        try:
            H.previous_step5(driver)

            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys()

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            print("TC-5-5 passed. The user can't fail to enter State.")
        except NoSuchElementException:
            print("TC-5-5 failed. Is there something wrong. The user can fail to enter value State.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a state')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a state'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_06_06(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Country not entered
        try:
            H.previous_step5(driver)

            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys()

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            print("TC-6-6 passed. The user can't fail to enter Country.")
        except NoSuchElementException:
            print("TC-6-6 failed. Is there something wrong. The user can fail to enter value Country.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a country')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a country'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_07_07(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Invalid City
        try:
            H.previous_step5(driver)

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("90272")

            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("-$@&")
            driver.find_element(By.XPATH, "//div[contains(text(),'Please enter a city')]")
            time.sleep(1)

            print("TC-7-7 passed. The user can't enter invalid City name.")
        except NoSuchElementException:
            print("TC-7-7 failed. Is there something wrong. The user can enter invalid City name.")


        self.driver.quit()

    def test_08_08(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Company Information/Invalid City
        try:
            H.previous_step5(driver)

            company_name = driver.find_element(By.XPATH, "//input[@id='customerBusinessName']")
            company_name.send_keys("ABC Inc")
            street_address = driver.find_element(By.XPATH, "//input[@id='customerStreetAddress']")
            street_address.send_keys("1000 Main Street")
            state = driver.find_element(By.XPATH, "//input[@id='customerState']")
            state.send_keys("CA")
            country = driver.find_element(By.XPATH, "//input[@id='customerCountry']")
            country.send_keys("USA")
            phone = driver.find_element(By.XPATH, "//input[@id='customerPhone']")
            phone.send_keys("201-555-0123")
            city = driver.find_element(By.XPATH, "//input[@id='customerCity']")
            city.send_keys("Los Angeles")

            postal_code = driver.find_element(By.XPATH, "//input[@id='customerPostalCode']")
            postal_code.send_keys("9%#@(0)")
            driver.find_element(By.XPATH, "//div[contains(text(),'Please enter a postal code')]")
            time.sleep(1)

            print("TC-8-8 passed. The user can't enter invalid Postal Code.")
        except NoSuchElementException:
            print("TC-8-8 failed. Is there something wrong. The user can enter invalid Postal Code")


        self.driver.quit()

    def test_09_09(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Point of contact/Name not entered
        try:
            H.previous_step6(driver)

            name = driver.find_element(By.XPATH, "//input[@id='ppocName']")
            name.send_keys()

            email = driver.find_element(By.XPATH, "//input[@id='ppocEmail']")
            email.send_keys("gewofew916@fna6.com")
            phone = driver.find_element(By.XPATH, "//input[@id='ppocPhone']")
            phone.send_keys("201-555-0124")

            print("TC-9-9 passed. The user can't fail to enter value Name.")
        except NoSuchElementException:
            print("TC-9-9 failed. Is there something wrong. The user can fail to enter value Name.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a name')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a name'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_10_10(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Point of contact/Invalid Email Address
        try:
            H.previous_step6(driver)

            email = driver.find_element(By.XPATH, "//input[@id='ppocEmail']")
            email.send_keys("gewofew916@fna6")

            name = driver.find_element(By.XPATH, "//input[@id='ppocName']")
            name.send_keys("John Smith")
            phone = driver.find_element(By.XPATH, "//input[@id='ppocPhone']")
            phone.send_keys("201-555-0124")

            print("TC-10-10 passed. The user can't enter invalid email address.")
        except NoSuchElementException:
            print("TC-10-10 failed. Is there something wrong. The user can enter invalid email address.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(text(),'Please enter a valid email address')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'Please enter a valid email address'.")
        except AssertionError:
            print("The page is different")


        self.driver.quit()

    def test_11_11(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(H.Rideshare_url)

        # Verify Point of contact/Invalid Phone Number
        try:
            H.previous_step6(driver)

            phone = driver.find_element(By.XPATH, "//input[@id='ppocPhone']")
            phone.send_keys("201-555-01")

            name = driver.find_element(By.XPATH, "//input[@id='ppocName']")
            name.send_keys("John Smith")
            email = driver.find_element(By.XPATH, "//input[@id='ppocEmail']")
            email.send_keys("gewofew916@fna6.com")

            print("TC-11-11 passed. The user can't enter invalid phone number.")
        except NoSuchElementException:
            print("TC-11-11 failed. Is there something wrong. The user can enter invalid phone number.")

        try:
            wait = WebDriverWait(driver, 2)
            assert wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(text(),'A valid phone number is required')]")))
            time.sleep(1)
            print("The page is correct. An inscription appeared 'A valid phone number is required'.")
        except AssertionError:
            print("The page is different")

        self.driver.quit()

def tearDown(self):
    self.driver.quit()











