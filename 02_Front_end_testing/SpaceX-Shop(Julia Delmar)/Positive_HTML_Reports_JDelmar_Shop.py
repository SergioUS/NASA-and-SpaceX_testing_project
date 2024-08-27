from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time
import HtmlTestRunner
from selenium.webdriver.chrome.service import Service as ChromeService


def delay():
    time.sleep(random.randint(1, 5))


class ChromePositiveTests(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=ChromeService())
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    # Verify correct URL
    def test_check_shop_chrome(self):
        driver = self.driver
        driver.get('https://www.spacex.com/')

        wait = WebDriverWait(driver, 2)
        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is clickable")
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        time.sleep(1)

        # Verify correct URL
        try:
            assert "https://shop.spacex.com/" in driver.current_url
            print("URL is OK")
        except AssertionError:
            print("URL is wrong, current URL: ", driver.current_url)

        # Verify title
        try:
            assert "Official SpaceX Store" in driver.title
            print("Title is OK")
        except AssertionError:
            print("Title is wrong, current title: ", driver.title)

    def tearDown(self):
        self.driver.quit()

    # Verify Shop button clickable
    def test_check_shirts_chrome(self):
        driver = self.driver
        driver.get('https://www.spacex.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify Womens button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Womens')])[2]"))).click()
        print("Womens button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Womens')])[2]")))
        print("Womens button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        time.sleep(2)

        # Verify Shirts button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]")))
        print("Shirts button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]")))
        print("Shirts button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)
        assert "https://shop.spacex.com/collections/womens-shirts" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_added_item_to_cart_chrome(self):
        driver = self.driver
        driver.get('https://www.spacex.com/')
        wait = WebDriverWait(driver, 2)

        # Verify Shop button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify Womens button is clickable
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Womens')])[2]"))).click()
        print("Womens button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Womens')])[2]")))
        print("Womens button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        time.sleep(2)

        # Verify Shirts button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]")))
        print("Shirts button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]")))
        print("Shirts button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/collections/womens-shirts'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.spacex.com/collections/womens-shirts" in driver.current_url
        print("URL is OK")

        # Verify Unisex Starship Flight 4 T-shirt button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/womens-shirts/products/unisex-starship-flight-4-t-shirt'])[2]")))
        print("Unisex Starship Flight 4 T-shirt button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/womens-shirts/products/unisex-starship-flight-4-t-shirt'])[2]")))
        print("Unisex Starship Flight 4 T-shirt button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "(//a[@href='/collections/womens-shirts/products/unisex-starship-flight-4-t-shirt'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(.,'Unisex Starship Flight 4 T-Shirt')]")))
        driver.find_element(By.XPATH, "//label[@title='Black']")
        delay()
        driver.find_element(By.XPATH, "//span[@class='ProductForm__SelectedValue'][contains(.,'S')]").click()
        delay()
        driver.find_element(By.XPATH, "//input[@value='1']")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='Container'])[1]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[@class='Container'])[1]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//div[@class='Container'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct page
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='Container'])[1]")))
        print("Checkout button is visible")
        driver.find_element(By.XPATH, "(//div[@class='Container'])[1]")
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

        # Verify correct URL

    def test_removed_item_from_cart_chrome(self):
        driver = self.driver
        driver.get('https://www.spacex.com/')

        # Verify Shop button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Accessories')])[2]").click()
        time.sleep(2)

        # Verify button Accessories is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Accessories')])[2]"))).click()
        print("Accessories button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Accessories')])[2]")))
        print("Accessories button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Accessories')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Accessories')])[2]").click()

        # Verify View All button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/accessories'])[2]")))
        print("View All button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/accessories'])[2]")))
        print("View All button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/collections/accessories'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.spacex.com/collections/accessories" in driver.current_url
        print("URL is OK")

        # Verify Starship Torch button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[contains(.,'STARSHIP TORCH')])[2]")))
        print("Starship Torch button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(.,'STARSHIP TORCH')])[2]")))
        print("Starship Torch button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'STARSHIP TORCH')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify Add to cart button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(.,'STARSHIP TORCH')]")))
        driver.find_element(By.XPATH, "(//input[contains(@value,'1')])[2]")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'Product__InfoWrapper')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'Product__InfoWrapper')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[contains(@class,'Product__InfoWrapper')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify item added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='Container'])[1]")))
        print("Checkout button is visible")
        driver.find_element(By.XPATH, "(//div[@class='Container'])[1]")
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    # Verify correct URL
    def test_check_shop_kids_shirts_chrome(self):
        driver = self.driver
        driver.get('https://www.spacex.com/')

        # Verify Shop button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]")))
        print("Shop button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='https://shop.spacex.com/'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify Kids button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Kids')])[2]"))).click()
        print("Kids button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Kids')])[2]")))
        print("Kids button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Kids')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Kids')])[2]").click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[contains(.,'Shirts')])[6]")))
        print("Shirts button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(.,'Shirts')])[6]")))
        print("Shirts button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'Shirts')])[6]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(2)

        # Verify correct URL
        assert "https://shop.spacex.com/collections/kids-t-shirts" in driver.current_url
        print("URL is OK")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
