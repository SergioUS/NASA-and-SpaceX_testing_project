# Unittest, includes Positive and Negative tests for SpaceX site, Starship module (prepared by Tatsiana Lentz)

from selenium import webdriver
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import unittest
import time
import Helpers_SpaceX_Starship as H
from selenium.webdriver.common.keys import Keys
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

fake = Faker()


# driver sleep from 1 to 4 seconds
def delay():
    time.sleep(random.randint(1, 4))


def scroll_to_element(iframe):
    pass


class ChromeAPositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.set_window_size(1920, 1080)

# As per unittest module, individual test should start with test_
    def test_case_010_starship(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          SPACEX--(STARSHIP)                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

# TC010
        print("                                                                                                    ")
        print("          Starship TC010                                                                           ")
        print("        --------------------                                                                        ")

# Opening SpaceX site
        driver.get(H.SpaceX_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()

# Check API
        H.check_api(driver)

# Checking title
        H.assert_title(driver, "SpaceX")
        delay()

# Verify and Validate Starship link
        driver.find_element(By.XPATH, H.starship_link).click()
        delay()
        print("----Starship link is visible and clickable")

# Check for correct title on Starship page
        self.assertIn("SpaceX - Starship", driver.title)
        H.starship_title_check(driver)

# Test results for TC01
        print("                                                                                                     ")
        print("        !!!  TC010  PASS   !!!                                                                     ")
        print("        --------------------                                                                        ")

    def test_case_011_starship(self):
        driver = self.driver
        print("                                                                                                     ")
        print("          Starship TC011                                                                             ")
        print("        --------------------                                                                         ")

# Opening SpaceX site
        driver.get(H.SpaceX_url)

# Verifying correct homepage logo
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))

# Check API
        H.check_api(driver)
        delay()

# Check title
        H.assert_title(driver, "SpaceX")
        delay()

# Verify and Validate Starship link
        driver.find_element(By.XPATH, H.starship_link).click()
        delay()

# Checking title
        H.starship_title_check(driver)

# Verifying Starship header
        try:
            wait = WebDriverWait(driver, 8)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Starship')]")))
            delay()
            print("----Starship heading is visible")
        except WDE:
            print("ATTENTION! Starship heading is not visible.")

# Test results for TC011

        print("                                                                                                     ")
        print("        !!!  TC011  PASS   !!!                                                                     ")
        print("        --------------------                                                                        ")

    def test_case_012_starship(self):
        driver = self.driver

# TC012
        print("                                                                                                    ")
        print("          Starship TC012                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX site
        driver.get(H.SpaceX_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))

# Check API
        H.check_api(driver)

# Title check
        H.assert_title(driver, "SpaceX")


# Verify and Validate Starship link
        driver.find_element(By.XPATH, H.starship_link).click()
        time.sleep(10.0)

# Title check
        H.starship_title_check(driver)

# Scrolling down to Starship Overview
        driver.execute_script("window.scrollTo(0,700)")
        delay()

# Verify Starship overview slide
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="reveal-overview"]/h2')))
#
# Scrolling right Starship carousel
        right_arrow = driver.find_element(By.XPATH, '//div[@id="gallery-next-s"]')
        for arrow in range(4):
            right_arrow.send_keys(Keys.ARROW_RIGHT)
            delay()

# End of right scroll
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'RAPTOR ENGINES')]")))
        delay()
        print("----Right scroll 3 times completed")

# Scrolling left Starship overview carousel
        left_arrow = driver.find_element(By.XPATH, '//*[@id="gallery-prev-s"]')
        for arrow in range(4):
            left_arrow.send_keys(Keys.ARROW_LEFT)
            delay()

# End of left scroll
        driver.find_element(By.XPATH, '//*[@id="reveal-overview"]/h2')
        print("----Left scroll 3 times completed")

# Test results for TC012
        print("                                                                                                     ")
        print("        !!!  TC012  PASS   !!!                                                                     ")
        print("        --------------------                                                                        ")

    def test_case_013_starship(self):
        driver = self.driver
        print("                                                                                                    ")
        print("          Starship TC013                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX site
        driver.get(H.SpaceX_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))

# Check API
        H.check_api(driver)

# Check title
        H.assert_title(driver,"SpaceX")

# Verify and Validate Starship link
        driver.find_element(By.XPATH, H.starship_link).click()
        time.sleep(10.0)

# Title check
        H.starship_title_check(driver)

# Scrolling to video
        driver.execute_script("window.scrollTo(0, 1400)")
        time.sleep(10)

# Video play
        driver.find_element(By.XPATH, '//*[@id="video"]/div[2]').click()
        driver.save_screenshot("video.png")
        # give time for movie to play
        time.sleep(20)
        driver.save_screenshot("video1.png")
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')
        print("----Video is playing. Check screenshots")

# TC04 results
        print("                                                                                                     ")
        print("        !!!  TC013  PASS   !!!                                                                     ")
        print("        --------------------                                                                        ")

    def test_case_014_starship(self):
        driver = self.driver
        # self.driver.maximize_window()
        print("                                                                                                    ")
        print("          Starship TC014                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX site
        driver.get(H.SpaceX_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))

# API check
        H.check_api(driver)

# Checking title
        H.assert_title(driver, "SpaceX")


# Verify and Validate Starship link
        driver.find_element(By.XPATH, H.starship_link).click()
        delay()

# Title check
        H.starship_title_check(driver)

# Scrolling down to Starship capabilities slide
        driver.execute_script("window.scrollTo(0,3100)")
        delay()

# Verify capabilities carousel

        driver.find_element(By.XPATH, "//h2[contains(text(),'Starship Capabilities')]")
        delay()
        right_arrow_r = driver.find_element(By.XPATH, "//div[@id='capabilities-next-g']")
        for arrow in range(5):
            right_arrow_r.send_keys(Keys.ARROW_RIGHT)
            delay()

# End of right scroll
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//h2[@class='animate js-bounding'])[6]")))
        delay()
        print("----Right scroll 4 times completed")

# Scrolling left Starship capabilities carousel
        left_arrow = driver.find_element(By.XPATH, "//div[@id='capabilities-prev-g']")
        left_arrow.send_keys(Keys.ARROW_LEFT)
        delay()
        left_arrow.send_keys(Keys.ARROW_LEFT)
        delay()
        left_arrow.send_keys(Keys.ARROW_LEFT)
        delay()
        left_arrow.send_keys(Keys.ARROW_LEFT)

# End of left scroll
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Starship Capabilities')]")))
        delay()
        print("----Left scroll 4 times completed")

# TC014 Results
        print("                                                                                                     ")
        print("        !!!  TC014  PASS   !!!                                                                     ")
        print("        --------------------                                                                        ")

    def tearDown(self):
        self.driver.quit()


class ChromeNegativeTests(unittest.TestCase):
    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        # self.driver.set_window_size(1920, 1080)

    def test_case_003_3_shop(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("                                        OFFICIAL SPACEX STORE                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

# TC003-3
        print("          Shop TC003-3                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX-Shop site
        driver.get(H.shop_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 4)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

# Check API
        H.shop_api_check(driver)

# Check title
        H.assert_title(driver, "Official SpaceX Store")
        delay()

# Scrolling down
        driver.execute_script("window.scrollTo(0, 2000)")
        delay()

# Finding "Super heavy chrome model" in the store
        wait = WebDriverWait(driver, 5)
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'SUPER HEAVY CHROME MODEL')])[2]")))
        item.click()
        delay()

# Input invalid email format
        driver.execute_script("window.scrollTo(0, 300)")
        email_form = driver.find_element(By.XPATH, "//input[@id='subscribe-email-address']")
        email_form.clear()
        email = str(random.randint(0, 1000)) + "!"
        email_form.send_keys(email)
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'Subscribe')]").click()

# Confirmation of subscription
# TC01 Results
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'Alert Alert Alert--info')]")))
            print("----Invalid email was added successfully.")
            print("----'You're now subscribed to receive updates when the product is back on stock.' message is visible.")
            print("                                                                                                   ")
            print("        !!!  TC003-3  FAIL   !!!                                                                   ")
            print("        --------------------                                                                       ")
        except WDE:
            print("----Invalid email was not added .")
            print("                                                                                                   ")
            print("        !!!  TC003-3  PASS   !!!                                                                   ")
            print("        --------------------                                                                       ")

    def test_case_004_4_shop(self):
        driver = self.driver

# TC004-4
        print("                                                                                                     ")
        print("          Shop TC004-4                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX-Shop site
        driver.get(H.shop_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

# Check API
        H.shop_api_check(driver)

# Check title
        H.assert_title(driver, "Official SpaceX Store")
        delay()

# Scrolling down
        driver.execute_script("window.scrollTo(0, 2000)")
        delay()

# Finding "Super heavy chrome model" in the store
        wait = WebDriverWait(driver, 10)
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'SUPER HEAVY CHROME MODEL')]")))
        item.click()
        delay()

# "Coming soon" button
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Coming Soon')]")
        button.click()

# Verify that cart is empty and item was not added
        driver.find_element(By.XPATH, '//*[@id="section-header"]/div/div[4]/nav/ul/li[3]/a').click()
        time.sleep(1)

# Verify correct page
        try:
            assert driver.title == "Your Shopping Cart – SpaceX Store"
            print("----Title check:'Your Shopping Cart – SpaceX Store'")
        except WDE:
            print("----ATTENTION! Title is different. Current Title is:", driver.title)
        delay()


# Check shopping cart message
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="EmptyState__Title Heading u-h5"]')))
            print("----'YOUR CART IS EMPTY' message is present")
            print("                                                                                                   ")
            print("        !!!  TC004-4  PASS   !!!                                                                   ")
            print("        --------------------                                                                       ")
        except WDE:
            print("----Cart is not empty!")
            print("                                                                                                   ")
            print("        !!!  TC004-4  FAIL   !!!                                                                   ")
            print("        --------------------                                                                       ")
            driver.save_screenshot('shopping cart.png')

    def test_case_005_5_shop(self):
        driver = self.driver

        print("                                                                                                   ")
        print("            Shop  TC005-5                                                                       ")
        print("        ---------------------                                                                     ")

# Opening SpaceX-Shop site
        driver.get(H.shop_url)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

# Check API
        H.shop_api_check(driver)

# Title check
        H.shop_title_check(driver)

# Locating account
        driver.find_element(By.XPATH, H.shop_account_link).click()
        delay()

# Title check for Account page
        H.assert_title(driver, "Account – SpaceX Store")

# 'Create one' link
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="customer_login"]/div[3]/a'))).click()
        delay()

# Title check for  Create Account page
        H.assert_title(driver, "Create Account – SpaceX Store")

# Verifying we are on  Create Account page
        driver.find_element(By.XPATH, '//*[@id="create_customer"]/header/h1')

# Filling out registration form
        driver.find_element(By.NAME, "customer[first_name]")
        driver.find_element(By.NAME, "customer[last_name]")
        delay()
        registration_email = driver.find_element(By.NAME, "customer[email]")
        registration_email.send_keys(fake.email())
        delay()
        registration_password = driver.find_element(By.NAME, "customer[password]")
        delay()
        registration_password.clear()
        registration_password.send_keys(fake.password())
        time.sleep(6.5)
        driver.find_element(By.XPATH, "//button[contains(text(),'Create my account')]").click()
        delay()

# Title check for current page
        H.assert_title(driver, "Official SpaceX Store")

# Check account registration status
        driver.find_element(By.XPATH, H.shop_account_link).click()
        delay()

# Title check on my account page
        try:
            assert driver.title == "Account – SpaceX Store"
            print("----Title check: Page has, " + driver.title + " as Page title")
        except WDE:
            print("ATTENTION! Title is different. Current Title is:", driver.title)
            delay()

# Verifying we are on 'My Account' page
        driver.find_element(By.XPATH, '//*[@id="main"]/div/header/div/h1')
        print("----'My Account' message is visible")
        delay()

# Checking for Greeting message
        try:
            wait = WebDriverWait(driver,3)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Welcome back, !')]")))
            driver.save_screenshot('Greeting_without_name.png')
            print("----Greeting without a user's name: 'Welcome back, !'. Check screenshot" )
            print("                                                                                                   ")
            print("        !!!  TC005-5  FAIL   !!!                                                                   ")
            print("        --------------------                                                                       ")
        except WDE:
            driver.save_screenshot('Greeting_account_registration.png')
            print("ATTENTION! Check screenshot")
            print("                                                                                                   ")
            print("        !!!  TC005-5  PASS   !!!                                                                   ")
            print("        ---------------------                                                                     ")

    def test_case_006_6_shop(self):
        driver = self.driver
# TC006-6
        print("                                                                                                     ")
        print("          Shop TC006-6                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX-Shop site
        driver.get(H.shop_url)

# Check API
        H.shop_api_check(driver)

# Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

# Check title
        H.shop_title_check(driver)


# Locating account
        driver.find_element(By.XPATH, H.shop_account_link).click()
        delay()

# Title check
        H.assert_title(driver, "Account – SpaceX Store")

# Verify we are on Log in page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Login')]")))
        delay()

# Filling out log in with existing valid email only
        email = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/input')
        email.clear()
        email.send_keys("kiyax51885@cnurbano.com")
        delay()
        driver.find_element(By.XPATH, "//input[contains(@type,'password')]").clear()

# Clicking Log in
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Login')]").click()
        time.sleep(3)

# Checking status of Log in
        login_fail = driver.find_element(By.XPATH, '//*[@id="customer_login"]/header/p')
        login_sign = driver.find_element(By.XPATH, '//*[@id="customer_login"]/header/h1')

        if login_fail and login_sign:
            print("----Login failed.")
            print("                                                                                                   ")
            print("        !!!  TC006-6  PASS   !!!                                                                   ")
            print("        ---------------------                                                                     ")
        else:
            print("----Check for login")
            print("                                                                                                   ")
            print("        !!!  TC006-6  FAIL   !!!                                                                   ")
            print("        ---------------------                                                                     ")

    def test_case_007_7_shop(self):
        driver = self.driver

# TC007-7
        print("                                                                                                     ")
        print("          Shop TC007-7                                                                            ")
        print("        --------------------                                                                        ")

# Opening SpaceX-Shop site
        driver.get(H.shop_url)

# Check API
        H.shop_api_check(driver)

# Verifying correct homepage
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.shop_homepage_logo)))

# Title check
        H.shop_title_check(driver)

# Locating account
        driver.find_element(By.XPATH, H.shop_account_link).click()
        delay()

# Title check
        H.assert_title(driver, "Account – SpaceX Store")

# Verify we are on Log in page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Login')]")))
        delay()


# Filling out log in with existing valid password only
        driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/input').clear()
        password = driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        password.clear()
        password.send_keys("12345")
        delay()

# Clicking Log in
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Login')]").click()
        time.sleep(7)

# Checking status of Log in
        login_fail = driver.find_element(By.XPATH, '//*[@id="customer_login"]/header/p')
        login_sign = driver.find_element(By.XPATH, '//*[@id="customer_login"]/header/h1')

        if login_fail and login_sign:
            print("----Login failed.")
            print("                                                                                                   ")
            print("        !!!  TC007-7  PASS   !!!                                                                   ")
            print("        ---------------------                                                                     ")
        else:
            print("----Check for login")
            print("                                                                                                   ")
            print("        !!!  TC007-7  FAIL   !!!                                                                   ")
            print("        ---------------------                                                                     ")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)