from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import unittest
import time
import AllureReports
from selenium.webdriver.chrome.service import Service as ChromeService


def delay():
    time.sleep(random.randint(1, 5))


class ChromeNegativeTests(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=ChromeService())
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    # Verify correct URL
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
        time.sleep(2)

        # Verify Mens button is clickable
        driver.find_element(By.XPATH, "(//button[contains(.,'Mens')])[2]").click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Mens')])[2]"))).click()
        print("Mens button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Mens')])[2]")))
        print("Mens button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Mens')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        driver.find_element(By.XPATH, "(//button[contains(.,'Mens')])[2]").click()

        # Verify Outwear button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/outerwear'])[2]")))
        print("Outwear button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/outerwear'])[2]")))
        print("Outwear button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/collections/outerwear'])[2]").click()
        driver.find_element(By.XPATH, "(//a[@href='/collections/outerwear'])[2]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "(//a[@href='/collections/outerwear'])[2]").send_keys('0.5')
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
        assert "https://shop.spacex.com/collections/outerwear" in driver.current_url
        print("URL is OK")

        # Verify Unisex Dragon Sweater button is clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'UNISEX DRAGON SWEATER')])[2]")))
        print("Unisex Dragon Sweater button is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'UNISEX DRAGON SWEATER')])[2]")))
        print("Unisex Dragon Sweater button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'UNISEX DRAGON SWEATER')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify Size XS button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[@type='button'])[3]")))
        print("Size XS button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@type='button'])[3]")))
        print("Size XS button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[@type='button'])[3]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify S button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'S')])[6]")))
        print("Size S button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'S')])[6]")))
        print("Size S button is clickable")
        time.sleep(1)
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'S')])[6]").click()
        time.sleep(2)

        # Verify Item added to cart
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//span[contains(@class,'Button Link Link--secondary')])[2]")))
        print("Quantity button is visible")

        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='quantity']")))
        quantity_input.send_keys("0.5")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'Product__InfoWrapper')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'Product__InfoWrapper')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(.,'Add to cart')]").click()
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

        # Verify Unisex Dragon Sweater added to cart
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//img[contains(@class,'CartItem__Image')])[1]")))
        print("Image Unisex Dragon Sweater added to cart")
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

    def test_added_item1_to_cart_chrome(self):
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
        time.sleep(2)

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
        time.sleep(2)

        # Verify Shirts button is clickable
        driver.find_element(By.XPATH, "(//button[contains(.,'Womens')])[2]").click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[contains(.,'Shirts')])[5]")))
        print("Shirts button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(.,'Shirts')])[5]")))
        print("Shirts button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'Shirts')])[5]").click()
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

        # Verify Unisex Starship Flight 3 T-Shirt button is clickable
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//a[contains(.,'Unisex Starship Flight 3 T-Shirt')])[2]")))
        print("Unisex Starship Flight 3 T-Shirt button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(.,'Unisex Starship Flight 3 T-Shirt')])[2]")))
        print("Unisex Starship Flight 3 T-Shirt button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'Unisex Starship Flight 3 T-Shirt')])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        # Verify color button
        driver.find_element(By.XPATH, "//label[@title='Black']")
        delay()
        print("Find color Black")
        time.sleep(2)

        # Verify Size button is clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@type='button'])[3]")))
        print("Size button is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[3]")))
        print("Size button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[@type='button'])[3]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'S')])[5]")))
        print("Size S button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'S')])[5]")))
        print("Size S button is clickable")
        time.sleep(1)
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'S')])[5]").click()
        time.sleep(2)

        # Quantity added to cart
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//span[contains(@class,'Button Link Link--secondary')])[2]")))
        print("Quantity button is visible")

        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@value,'1')])[1]")))
        quantity_input.send_keys("0.2")
        time.sleep(1)

        # Verify Add to cart button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'InfoWrapper')]")))
        print("Add to cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'InfoWrapper')]")))
        print("Add to cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(.,'Add to cart')]").click()
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
            (By.XPATH, "(//img[contains(@class,'CartItem__Image')])[1]")))
        print("Image Unisex Starship Flight 3 T-Shirt added to cart")
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

    def test_check_search_line_chrome(self):
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
        time.sleep(1)

        # Verify Search button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[@data-action='toggle-search'])[1]")))
        print("Search button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@data-action='toggle-search'])[1]")))
        print("Search button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[@data-action='toggle-search'])[1]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Search Line added keys
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='search']")))
        print("Search Line is visible")
        driver.get("https://shop.spacex.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("12345")
        time.sleep(5)

        # Verify No results could be found
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'No results could be found')]")))
        print("No results could be found")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

        # Verify correct URL

    def test_added_item2_to_cart_chrome(self):
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
        time.sleep(1)

        # Verify Kids button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Kids')])[2]")))
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
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Kids')])[2]").click()
        time.sleep(2)

        # Verify Outwear button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/kids-outerwear'])[2]")))
        print("Outwear button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/kids-outerwear'])[2]")))
        print("Outwear button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[@href='/collections/kids-outerwear'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Kids SpaceX Spacesuit Onesie button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[@href='/collections/kids-outerwear/products/spacex-spacesuit-onesie'])[2]")))
        print("Kids SpaceX Spacesuit Onesie button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[@href='/collections/kids-outerwear/products/spacex-spacesuit-onesie'])[2]")))
        print("Kids SpaceX Spacesuit Onesie button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "(//a[@href='/collections/kids-outerwear/products/spacex-spacesuit-onesie'])[2]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[contains(.,'White')]")))
        print("Kids SpaceX Spacesuit Onesie button is visible")

        # Verify quantity added
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//input[contains(@value,'1')])[1]")))
        print("Quantity button is visible")

        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@value,'1')])[1]")))
        quantity_input.send_keys("!")
        time.sleep(1)

        # Verify Add to Cart button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'InfoWrapper')]")))
        print("Add to Cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'InfoWrapper')]")))
        print("Add to Cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(.,'Add to cart')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify correct URL
        assert "https://shop.spacex.com/cart" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    # Verify correct URL
    def test_added_item3_to_cart_chrome(self):
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
        time.sleep(1)

        # Verify Accessories button is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[contains(.,'Accessories')])[2]")))
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
        time.sleep(1)
        driver.find_element(By.XPATH, "(//button[contains(.,'Accessories')])[2]").click()
        time.sleep(2)

        # Verify View All button is clickable
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//a[contains(.,'View All')])[8]")))
        print("View All button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//a[contains(.,'View All')])[8]")))
        print("View All button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "(//a[contains(.,'View All')])[8]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify Starship Torch button is clickable
        wait = WebDriverWait(driver, 2)
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
        time.sleep(1)

        # Verify quantity added
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//span[@class='QuantitySelector__Button Link Link--secondary'])[2]")))
        print("Quantity button is visible")

        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@value,'1')])[2]")))
        quantity_input.send_keys("---")
        time.sleep(1)

        # Verify Add to Cart is clickable
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'Product__Info  ')]")))
        print("Add to Cart button is visible")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'Product__Info  ')]")))
        print("Add to Cart button is clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(.,'Add to cart')]").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        all_windows = driver.window_handles
        for window in all_windows:
            if window != first_window:
                new_window = window
        driver.switch_to.window(first_window)
        # assert driver.title == "The Internet", "title should be The Internet"
        driver.switch_to.window(new_window)
        time.sleep(1)

        # Verify correct URL
        assert "https://shop.spacex.com/cart" in driver.current_url
        print("URL is OK")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(AllureReports)
