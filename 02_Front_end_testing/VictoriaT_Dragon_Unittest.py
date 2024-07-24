import time
import unittest
# import AllureReports
# from selenium.common.exceptions import AssertionError
import HtmlTestRunner
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()


class SpaceX_01_Positive_and_Negative(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    # TC1 Verify SpaceX is open and header menu is visible

    def test_01_positive(self):
        driver = self.driver
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()
        driver.get("https://www.spacex.com/")

        # Verify header menu is visible
        driver.find_element(By.XPATH, "(//a[contains(.,'Dragon')])[1]").click()
        try:
            assert driver.title == "SpaceX - Dragon"
            print("Title is correct", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        # Verify elements in the Header menu
        try:
            WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//li[@class='nav-item'][contains(.,'Dragon')]")))
            driver.find_element(By.XPATH, "//a[@id='logo']")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Dragon')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starship')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Human Spaceflight')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Rideshare')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starshield')]")
            driver.find_element(By.XPATH, "//li[@class='nav-item'][contains(.,'Starlink')]")
            driver.find_element(By.XPATH, "//div[@id='navigation-right']")
            driver.find_element(By.XPATH, "//button[@id='hamburger']").click()
            # delay()
            print("All icons in header menu is displayed")
            print("TC-1 passed. Header menu is visible")
        except NoSuchElementException:
            print("TC-1 failed. header menu is not visible")

    #     #TC2 Verify that header menu is clickable and takes user to correct page
    def test_02_positive(self):
        driver = self.driver
        driver.get("https://www.spacex.com/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        time.sleep(3)
        try:
            assert driver.title == "SpaceX"
            print("Title is Correct. Current Title is:", driver.title)
            print("TC-2 passed. Header menu is visible")
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
            print("TC-2 failed. Header menu is visible")
        #
        time.sleep(2)
        #
        # # Verify and Validate Dragon link
        #
        driver.find_element(By.XPATH, "(//a[@href='/vehicles/dragon/'])[1]").click()
        time.sleep(2)
        try:
            assert driver.title == "SpaceX - Dragon"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

    #
    #
    # #3 Verify user can use Shop menu in header and that clickable and takes user to correct page
    def test_03_positive(self):
        driver = self.driver
        driver.get("https://www.spacex.com/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        time.sleep(7)
        window_before = driver.window_handles[0]
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        window_after = driver.window_handles[1]
        time.sleep(2)
        driver.switch_to.window(window_after)
        try:
            assert driver.title == "Official SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
            print("TC-3 passed. Header menu is visible")
        except AssertionError:
            print("Title is different. Current Title is:"), driver.title
            print("TC-3 failed. Header menu is visible")
        time.sleep(2)

    #
    # 4 Verify the header menu in Shop is present and clickable

    def test_04_positive(self):
        driver = self.driver
        driver.get("https://shop.spacex.com")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        #window_before = driver.window_handles[0]

        # #Navigate on Shop
        #driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        # window_after = driver.window_handles[1]
        time.sleep(1)
        # driver.switch_to.window(window_after)

        #  #Verify Title is correct
        try:
            assert driver.title == "Official SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        #
        #
        kids_menu = driver.find_element(By.XPATH, "//button[@class='Heading u-h6'][contains(.,'Kids')]")
        action = ActionChains(driver)
        action.move_to_element(kids_menu).perform()
        time.sleep(2)
        shirts = driver.find_element(By.XPATH, "(//a[contains(.,'Shirts')])[6]")

        action.click(shirts).perform()
        time.sleep(2)

        # Verify title for kid's shirts page is correct
        try:
            assert driver.title == "Kid's Shirts – SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
            print("TC-4 passed. Header menu is visible")
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
            print("TC-4 failed.")
        time.sleep(2)

    # #5-6 Verify navigate to header menu  in Shop open drop-down
    def test_05_06_positive(self):
        driver = self.driver
        driver.get("https://shop.spacex.com")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        #window_before = driver.window_handles[0]

        #     # Navigate on Shop
        # driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        # window_after = driver.window_handles[1]
        # time.sleep(1)
        # driver.switch_to.window(window_after)

        # #Confirm drop-dawn
        kids_menu = driver.find_element(By.XPATH, "//button[@class='Heading u-h6'][contains(.,'Kids')]")
        actions = ActionChains(driver)
        actions.move_to_element(kids_menu).perform()
        time.sleep(2)
        shirts = driver.find_element(By.XPATH, "(//a[contains(.,'Shirts')])[6]")
        actions.click(shirts).perform()
        time.sleep(3)
        #
        # #Verify Title is correct
        try:
            assert driver.title == "Kid's Starship Flight 4 T-Shirt – SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
            print("TC-5-6 passed. Header menu is visible")
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
            print("TC-5-6 failed. Header menu is visible")
        time.sleep(2)

    #
    #
    # 7 Verify user able to select a product
    def test_07_08_positive(self):
        driver = self.driver
        driver.get("https://www.spacex.com/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        window_before = driver.window_handles[0]
        #
        # # Click on Shop
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        window_after = driver.window_handles[1]
        time.sleep(2)
        driver.switch_to.window(window_after)
        time.sleep(2)

        #
        try:
            assert driver.title == "Official SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        #
        # #Confirm drop-down
        kids_menu = driver.find_element(By.XPATH, "//button[contains(@aria-controls,'kids')]")
        actions = ActionChains(driver)
        actions.move_to_element(kids_menu).perform()
        time.sleep(2)
        shirts = driver.find_element(By.XPATH, "(//a[contains(.,'Shirts')])[6]")
        actions.click(shirts).perform()
        time.sleep(3)
        # #Verify user on right page
        #
        try:
            assert driver.title == "Kid's Shirts – SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        # #Select product
        driver.find_element(By.XPATH,
                            '//*[@id="shopify-section-collection-template"]/section/div/div/div/div/ul/li[1]/div/div/div[2]/span/a').click()
        time.sleep(3)
        try:
            assert driver.title == "Kid's Starship Flight 4 T-Shirt – SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        #
        # #?????#8 Verify user able to click Add to Card button  (Continue for TC 7)
        driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Add to cart')]").click()
        #
        try:
            assert driver.title == "Your Shopping Cart – SpaceX Store"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        #
        #
        # #??? 9 Verify if click on Checkout button user move to right page
        driver.find_element(By.XPATH, "//button[@name='checkout']").click()
        time.sleep(3)
        try:
            assert driver.title == "Information - SpaceX Store - Checkout"
            print("Title is correct.Current Title is :", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        time.sleep(2)
        #
        #
        # #10 Verify User not able to continue shipping with wrong Email format
        #
        # # #type Email
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.clear()
        email.send_keys("test@test")
        time.sleep(3)
        element = driver.find_element(By.XPATH, '//*[@id="Form0"]/div[1]/div/div/div[2]/div/div[2]/div[1]/button')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        element.click()
        time.sleep(3)

        # driver.find_element(By.XPATH, "//button[contains(@fdprocessedid,'e6gjl')]").click()
        #
        try:
            assert driver.title == "Information - SpaceX Store - Checkout"
            print("Title is correct.Current Title is :", driver.title)
        except WDE:
            print("Title is correct.Current Title is :", driver.title)
        driver.find_element(By.XPATH, "//p[@id='error-for-email']")



    #11 Verify user not able to enter 1 letter or special characters of First Name and Last Name fields
    def test_09_negative(self):
        driver = self.driver
        driver.get("https://shop.spacex.com/26126155855/checkouts/d6ec79126848eb8bdcc7907f98290cec")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.minimize_window()

        # input email
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.clear()
        email.send_keys("test@test")
        time.sleep(3)
        # driver.find_element(By.XPATH, "//button[@id='continue_button']").  click()
        # driver.find_element(By.XPATH, "//input[contains(@aria-invalid,')true')]").send_keys("test@test")

        # #input first name and last name
        driver.find_element(By.XPATH, "//input[@id='TextField0']").send_keys("@")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='TextField1']").send_keys("L")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        element.click()
        time.sleep(3)

        try:
            assert driver.title == "Information - SpaceX Store - Checkout"
            print("TC -9 failed, First name and last name accepted and not highlighted in red", driver.title)
        except WDE:
            print("Title is correct.Current Title is :", driver.title)

    #
    #

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))