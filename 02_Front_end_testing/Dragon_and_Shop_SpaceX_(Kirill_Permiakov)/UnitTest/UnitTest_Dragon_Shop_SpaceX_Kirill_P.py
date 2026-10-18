import time
from selenium import webdriver
import unittest
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from faker import Faker
import UnitTest.Helpers_Dragon_Shop_SpaceX_Kirill_P as h

# Positive tests
class Positive_Chrome (unittest.TestCase):

# SetUP initialization function for class
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.set_window_size(1920, 1080)
        #self.driver.execute_script('Chrome.settingsPrivate.setDefaultZoom(0.8);')

# As per unittest module, each individual test name should start with test_
    def test_case_006_Dragon (self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          SPACEX / DRAGON                                         ")
        print("                                                                                                    ")
        print("----------------------------------- POSITIVE TEST CASES 006 - 010 ---------------------------------")
        print("                                                                                                    ")
    # TC006
        print("        ")
        print("          DRAGON TC006       ")
        print("        --------------------    ")

    # Opening SpaceX site
        driver.get(h.SpaceX_url)

    # Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.homepage_logo)))
        print("----Homepage_logo is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.home_title)

    # Check URL
        h.check_URL(driver, h.SpaceX_url)

        h.delay()

    # Verify, Validate and click on Dragon link
    # 1. Find the Vehicles menu
        vehicles = wait.until(EC.visibility_of_element_located((By.XPATH, h.vehicles_link)))
        print("----Visibility_of_element: Vehicles is OK")
    # 2. Hover the mouse cursor over Vehicles menu
        ActionChains(driver).move_to_element(vehicles).perform()
        print("----Hover the mouse cursor over Vehicles is OK")

    # 3. Verify dropdown appears with items: StarShip, Dragon, Falcon 9, Falcon Heavy, etc
        h.check_clickable_element(driver, h.starship_link)
        h.check_clickable_element(driver, h.falcon_9_link)
        h.check_clickable_element(driver, h.falcon_h_link)
        h.check_clickable_element(driver, h.dragon_link)

        h.delay()

    # Check for correct title on Dragon page
        try:
            print("----Check for correct title on Dragon page")
            dragon_title = "SpaceX - Dragon"
            self.assertIn(dragon_title, driver.title)
            print("----Title check: Page has, " + "'" + driver.title + "'" + " title as Page title")
        except WDE:
            print("ATTENTION! Page " + driver.title + " has wrong Title! (NOT " + dragon_title + ")")

        h.dragon_title_check(driver)
        h.assert_title(driver, "SpaceX - Dragon")

    # Test results for TC006
        print("   ")
        print("        !!!  DRAGON TC006  PASS   !!!                                                                     ")
        print("        --------------------      ")

    def test_case_007_Dragon (self):
        driver = self.driver
    # TC007
        print("        ")
        print("          DRAGON TC007       ")
        print("        --------------------    ")

    # Opening SpaceX - Dragon site
        driver.get(h.Dragon_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.dragon_homepage_logo)))
        print("----Homepage_logo is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.dragon_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.Dragon_url)

    # Refresh page (F5) and verify URL stays the same
        driver.refresh()
        print("----Dragon page was refreshed is OK")
        h.check_URL(driver, h.Dragon_url)

    # Test results for TC007
        print("   ")
        print("        !!!  DRAGON TC007  PASS   !!!        ")
        print("        --------------------      ")

    def test_case_008_Dragon (self):
        driver = self.driver
    # TC008
        print("        ")
        print("          DRAGON TC008       ")
        print("        --------------------    ")

    # Opening SpaceX - Dragon site
        driver.get(h.Dragon_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.dragon_homepage_logo)))
        print("----Homepage_logo is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.dragon_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.Dragon_url)

    # Scrolling down to Starship capabilities slide
        #driver.execute_script("window.scrollTo(0,3100)")

    # 1. Find the Element by XPath
        element_superdraco = driver.find_element(By.XPATH, h.superdraco_link)
        element_draco = driver.find_element(By.XPATH, h.draco_link)
    # 2. Scrolling to the Element
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element_draco)
        print("----Scrolling to Element "+ element_draco.text + " is OK")
        h.delay()
    # 3. Checking Elements
        h.check_clickable_element(driver, h.superdraco_link)
        h.check_clickable_element(driver, h.draco_link)





    # Test results for TC008
        print("   ")
        print("        !!!  DRAGON TC008  PASS   !!!        ")
        print("        --------------------      ")

    def test_case_009_shop_spacex (self):
        driver = self.driver
    # TC009
        print("                             ")
        print("          SHOP SPACEX TC009  ")
        print("        -------------------- ")

    # Opening SpaceX site
        driver.get(h.SpaceX_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.homepage_logo)))
        print("----Homepage_logo is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.home_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.SpaceX_url)

    # Verify, Validate and click on Shop link
    # 1. Find the Shop menu
        shop = wait.until(EC.visibility_of_element_located((By.XPATH, h.shop_link)))
        print("----Visibility_of_element: Shop is OK")
    # 2. Hover the mouse cursor over Shop menu
        ActionChains(driver).move_to_element(shop).perform()
        print("----Hover the mouse cursor over Shop is OK")
    # 3. Verify dropdown appears with item Shop SpaceX and Click
        h.check_clickable_element(driver, h.shop_spacex_link)
    # 4. Switch to new window Shop SpaceX
        driver.switch_to.window(driver.window_handles[-1])
        h.delay()

        print("----Current URL:", driver.current_url)
        print("----Page title:", driver.title)
        print("----Windows:", driver.window_handles)

    # Verifying correct web page Shop SpaceX
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.shop_spacex_logo)))
        print("----Homepage_logo Shop SpaceX is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.shop_spacex_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.Shop_SpaceX_url)

    # Test results for TC009
        print("   ")
        print("  !!!  SHOP SPACEX TC009 PASS   !!!        ")
        print("        --------------------      ")

    def test_case_010_shop_spacex (self):
        driver = self.driver
    # TC010
        print("                             ")
        print("          SHOP SPACEX TC010  ")
        print("        -------------------- ")

    # 1. Opening Shop SpaceX site
        driver.get(h.Shop_SpaceX_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.shop_spacex_logo)))
        print("----Homepage_logo Shop SpaceX is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.shop_spacex_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.Shop_SpaceX_url)

    # 2. Select 2nd item in-stock item and open its PDP (Product Display Page)
        scroll = str(500)
        self.driver.execute_script("document.body.style.zoom='50%'")
        print("----Shop SpaceX page ZOOM 50% is OK")
        driver.execute_script("window.scrollTo(0, " + scroll + ")")
        print("----Shop SpaceX page scrolled to " + scroll + " is OK")
        h.check_clickable_element(driver, h.shop_item2_link)
        print("----Shop SpaceX item 2 Click is OK")
        h.delay()

    # 3. Select size / quantity if required - Quantity: 1
        decrease = wait.until(EC.element_to_be_clickable((By.XPATH, h.dec_quantity)))
        increase = wait.until(EC.element_to_be_clickable((By.XPATH, h.inc_quantity)))
        quantity = wait.until(EC.element_to_be_clickable((By.XPATH, h.quantity_link)))
        addToCart = wait.until(EC.element_to_be_clickable((By.XPATH, h.add_to_cart_link)))
        increase.click()
        print("----Shop SpaceX item 2 Quantity increase.click() is OK")
        decrease.click()
        print("----Shop SpaceX item 2 Quantity decrease.click() is OK")
        quantity.clear()
        print("----Shop SpaceX item 2 Quantity quantity.clear() is NOT OK idk")
        quantity.send_keys("23")
        print("----Shop SpaceX item 2 Quantity quantity.send_keys('23') is OK")
        quantity.send_keys(Keys.BACK_SPACE)
        print("----Shop SpaceX item 2 Quantity quantity.send_keys(Keys.BACK_SPACE) is OK")
        quantity.send_keys(Keys.ARROW_LEFT)
        print("----Shop SpaceX item 2 Quantity quantity.send_keys(Keys.ARROW_LEFT) is OK")
        quantity.send_keys(Keys.DELETE)
        print("----Shop SpaceX item 2 Quantity quantity.send_keys(Keys.DELETE) is OK")
        quantity.send_keys(Keys.BACK_SPACE)
        print("----Shop SpaceX item 2 Quantity quantity.send_keys(Keys.BACK_SPACE) is OK")
        quantity.send_keys(h.item_quantity)
        print("----Shop SpaceX item 2 Quantity quantity.send_keys(h.item_quantity) = " + h.item_quantity + " is OK")
    # Getting a value from a field Quantity
        quantity_val = int(quantity.get_attribute("value"))

        addToCart.click()
        print("----Shop SpaceX item 2 addToCart.click() is OK")
        h.delay()

    # Verifying correct web page Cart
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.cart_header)))
        print("----Homepage_logo Cart is OK")
        h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.cart_title)
        h.delay()

    # Check URL
        h.check_URL(driver, h.Cart_url)

        quantity_cart = wait.until(EC.visibility_of_element_located((By.XPATH, h.cart_quantity_link)))
    # Getting a value from a field Quantity
        quantity_cart_val = int(quantity_cart.get_attribute("value"))

        if quantity_val == quantity_cart_val:
            print("----Quantity Cart = " + str(quantity_val) + " is OK")
        else:
            print(h.red, "----Quantity Cart = " + str(quantity_val) + " is NOT OK", h.dft)


    # Test results for TC010
        print("   ")
        print("  !!!  SHOP SPACEX TC010 PASS   !!!        ")
        print("        --------------------      ")

    def tearDown(self) -> None:
        self.driver.quit()

# Negative tests
class Negative_Chrome (unittest.TestCase):

    # SetUP initialization function for class
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #self.driver.set_window_size(1920, 1080)
        self.driver.execute_script('Chrome.settingsPrivate.setDefaultZoom(0.8);')


    def tearDown(self) -> None:
        self.driver.quit()





if __name__ == '__main__':
    unittest.main()


