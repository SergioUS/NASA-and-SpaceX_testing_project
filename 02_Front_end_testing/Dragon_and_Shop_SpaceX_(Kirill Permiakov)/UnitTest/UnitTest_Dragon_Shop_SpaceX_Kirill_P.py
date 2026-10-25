import time
from selenium import webdriver
import unittest
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
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
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.set_window_size(1920, 1080)
        #self.driver.execute_script('Chrome.settingsPrivate.setDefaultZoom(0.8);
# As per unittest module, each individual test name should start with test_
    def test_case_006_Dragon_Positive (self):
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

    def test_case_007_Dragon_Positive (self):
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

    def test_case_008_Dragon_Positive (self):
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
        h.check_clickable_element(driver, h.superdraco_link) # Check link SuperDraco
        h.check_element(driver,h.superdraco_img_link) # Check img SuperDraco
        h.check_clickable_element(driver, h.draco_link) # Check link Draco
        h.check_element(driver, h.draco_img_link) # Check img Draco

    # Test results for TC008
        print("   ")
        print("        !!!  DRAGON TC008  PASS   !!!        ")
        print("        --------------------      ")

    def test_case_009_shop_spacex_Positive (self):
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

    def test_case_010_shop_spacex_Positive (self):
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
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_case_006_Dragon_Negative (self):
        driver = self.driver
    # TC006
        print("        ")
        print("        DRAGON TC006 NEGATIVE      ")
        print("        ---------------------    ")

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
    # 3. Changing Element: Draco -> SuperDraco
        h.check_clickable_element(driver, h.superdraco_link) # Check link SuperDraco
        h.check_element(driver,h.superdraco_img_link) # Check img SuperDraco
        print("----Changing Element: Draco -> SuperDraco is OK")
    # 4. Click Restore Down (middle window button - make window smaller)
        #driver.set_window_rect(width=1200, height=800)
        driver.set_window_size(600, 600)
        print("----Click Restore Down Browser Window is OK")
        h.delay()
    # 5. Check content display in restored window
        h.check_element(driver, h.superdraco_img_link)  # Check img SuperDraco
        print("----Check content display in restored down window (SuperDraco) is OK")
        h.check_clickable_element(driver, h.draco_link)  # Check link Draco
        h.check_element(driver, h.draco_img_link)  # Check img Draco
        print("----Changing Element: SuperDraco -> Draco is OK")
    # 6. Click Maximize (fullscreen)
        driver.maximize_window()
        print("----Maximize window is OK")
        h.delay()
    # 7. Check content display
        h.check_element(driver, h.draco_img_link) # Check img Draco
        print("----Check content display Draco is OK")
    # Test results for TC006
        print("   ")
        print("        !!!  DRAGON TC006 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_007_Dragon_Negative (self):
        driver = self.driver
    # TC007
        print("        ")
        print("        DRAGON TC007 NEGATIVE      ")
        print("        ---------------------    ")

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

    # 1. Find the Element by XPath
        dragon_video = driver.find_element(By.XPATH, h.dragon_video_link)
        print("----Find the Element by XPath " + dragon_video.text + " is OK")

    # 2. Scrolling to the Element
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",dragon_video)
        print("----Scrolling to Element "+ dragon_video.text + " is OK")
        h.delay()

    # 3. Click on image / Play icon to run video
        h.check_clickable_element(driver, h.dragon_video_link)  # Check link Video
        print("----Click on image / Play icon to run video is OK")

    # 4. Verify video starts playing
        driver.switch_to.default_content()

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='ulVZds71CZQ']")))
        driver.switch_to.frame(iframe)
        try:
            print("----Current iframe URL:", driver.execute_script("return window.location.href;"))

            self.assertTrue(h.check_video_playing(driver), "Dragon video is NOT playing!")
        finally:
            driver.switch_to.default_content()

    # 5. Click Minimize (minimize browser to taskbar)
        driver.minimize_window()
        print("----Click Minimize (minimize browser to taskbar) is OK")
        h.delay()

    # 6. Click Maximize (fullscreen)
        driver.maximize_window()
        print("----Maximize window is OK")
        h.delay()

    # 7. Check content display
        h.check_element(driver, h.dragon_video_link) # Check Video locator
        print("----Check content display Draco is OK")

    # Test results for TC007
        print("   ")
        print("        !!!  DRAGON TC007 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_008_Dragon_Negative (self):
        driver = self.driver
    # TC008
        print("        ")
        print("        DRAGON TC008 NEGATIVE      ")
        print("        ---------------------    ")

    # 1.  Opening SpaceX - Dragon site
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

    # 2. Scroll to bottom banner / carousel / slider
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("----Scroll to bottom banner is OK")

    # Find the Element by XPath
        swbutt_next = driver.find_element(By.XPATH, h.swbutt_next_link)
        print("----Find the Element by XPath swbutt_next is OK")
        h.check_clickable_element(driver, h.swbutt_next_link)

        swbutt_prev = driver.find_element(By.XPATH, h.swbutt_prev_link)
        print("----Find the Element by XPath swbutt_prev is OK")
        h.check_clickable_element(driver, h.swbutt_prev_link)

# 3. Click 10 times in a row on Next / forward arrow
        for i in range(10):
            swbutt_next.click()
        print("----Swbutt_next.click 10 times is OK")

#. 4. Click Minimize and then Maximize browser window
        driver.minimize_window()
        print("----Minimize_window is OK")
        h.delay()
        driver.maximize_window()
        print("----Maximize_window is OK")

# 5. Click 10 times in a row on Back / Previous / backward arrow
        for i in range(10):
            swbutt_prev.click()
        print("----Swbutt_prev.click 10 times is OK")
        h.delay()

    # Test results for TC008
        print("   ")
        print("        !!!  DRAGON TC008 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_009_shop_spacex_Negative(self):
        driver = self.driver
    # TC009
        print("        ")
        print("        SHOP SPACEX TC009 NEGATIVE      ")
        print("        --------------------------    ")

    # 1. Opening Shop SpaceX site
        driver.get(h.Shop_SpaceX_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.shop_spacex_logo)))
        print("----Homepage_logo Shop SpaceX is OK")
        #h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.shop_spacex_title)
        #h.delay()

    # Check URL
        h.check_URL(driver, h.Shop_SpaceX_url)

    # 2. Find Search Button Element by XPATH and Click
        search_btn = driver.find_element(By.XPATH, h.search_btn_link)
        #search_btn = wait.until(EC.invisibility_of_element_located((By.XPATH, h.search_btn_link)))
        print("----Find Element by XPATH Search Button is OK")
        h.check_element(driver, h.search_btn_link)
        print("----Search_btn_link Element checked is OK")
        search_btn.click()
        print("----Click on Search Button is OK")

    # Find Search field Element by XPATH
        search_input = driver.find_element(By.XPATH, h.search_input_link)
        print("----Find Element by XPATH Search Input is OK")
        h.check_element(driver, h.search_input_link)
        print("----Search_input_link Element checked is OK")

    # 3. Type special symbols "!@#$%^&()" into search field
        search_input.send_keys(h.negative_search_str)
        print("----Type special symbols ", h.negative_search_str, " into search field is OK")
        h.delay()

    # 4. Send key Enter
        search_input.send_keys(Keys.ENTER)
        print("----Send key Enter is OK")
        #h.delay()

    # 5. Check result
    # Show URL
        h.show_URL(driver)

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, "Search result – SpaceX Store")

    # Check result output Title
        h.check_element(driver, h.search_res_link)
        print("----Search result text checked is OK")
    # Check result output 1 item
        h.check_element(driver, h.search_res_1_item_link)
        print("----Search result 1 item checked is OK")

    # Test results for TC009
        print("   ")
        print("        !!!  SHOP SPACEX TC009 NEGATIVE PASS   !!!        ")
        print("        ------------------------------------------      ")

    def test_case_010_shop_spacex_Negative(self):
        driver = self.driver
    # TC010
        print("        ")
        print("        SHOP SPACEX TC010 NEGATIVE      ")
        print("        --------------------------    ")

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

    # 2. Select 3rd item in-stock item and open its PDP (Product Display Page)
        scroll = str(500)
        self.driver.execute_script("document.body.style.zoom='50%'")
        print("----Shop SpaceX page ZOOM 50% is OK")
        driver.execute_script("window.scrollTo(0, " + scroll + ")")
        print("----Shop SpaceX page scrolled to " + scroll + " is OK")
        h.delay()
        h.check_clickable_element(driver, h.shop_item3_link)
        print("----Shop SpaceX item 3 Click is OK")
        h.delay()

    # 3. Find Quantity: field
        quantity = wait.until(EC.element_to_be_clickable((By.XPATH, h.quantity_link)))
        addToCart = wait.until(EC.element_to_be_clickable((By.XPATH, h.add_to_cart_link)))
        quantity.clear() # not work here
        quantity.send_keys("qwerty")
        print("----Shop SpaceX item 3 Quantity quantity.send_keys('qwerty') is OK")
        quantity.send_keys(Keys.TAB)

    # Getting a value from a field Quantity
        quantity_val = str(quantity.get_attribute("value"))

        h.check_element(driver, h.add_to_cart_link)
        addToCart.click()
        print("----Shop SpaceX item 3 addToCart.click() is OK")
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
        quantity_cart_val = str(quantity_cart.get_attribute("value"))

        if quantity_val == quantity_cart_val:
            print("----Quantity Cart = " + str(quantity_val) + " is OK")
        else:
            print(h.red, "----Quantity Cart = " + str(quantity_val) + " is NOT OK", h.dft)

    # Test results for TC010
        print("   ")
        print("        !!!  SHOP SPACEX TC010 NEGATIVE PASS   !!!        ")
        print("        ------------------------------------------      ")


    def tearDown(self) -> None:
        self.driver.quit()

# Positive tests
class Positive_Firefox (unittest.TestCase):

# SetUP initialization function for class
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        self.driver.set_window_size(1920, 1080)

# As per unittest module, each individual test name should start with test_
    def test_case_006_Dragon_Positive (self):
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

    def test_case_007_Dragon_Positive (self):
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

    def test_case_008_Dragon_Positive (self):
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
        h.check_clickable_element(driver, h.superdraco_link) # Check link SuperDraco
        h.check_element(driver,h.superdraco_img_link) # Check img SuperDraco
        h.check_clickable_element(driver, h.draco_link) # Check link Draco
        h.check_element(driver, h.draco_img_link) # Check img Draco

    # Test results for TC008
        print("   ")
        print("        !!!  DRAGON TC008  PASS   !!!        ")
        print("        --------------------      ")

    def test_case_009_shop_spacex_Positive (self):
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
        h.delay()
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

    def test_case_010_shop_spacex_Positive (self):
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
class Negative_Firefox (unittest.TestCase):

    # SetUP initialization function for class
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        self.driver.set_window_size(1920, 1080)

    def test_case_006_Dragon_Negative (self):
        driver = self.driver
    # TC006
        print("        ")
        print("        DRAGON TC006 NEGATIVE      ")
        print("        ---------------------    ")

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
    # 3. Changing Element: Draco -> SuperDraco
        h.check_clickable_element(driver, h.superdraco_link) # Check link SuperDraco
        h.check_element(driver,h.superdraco_img_link) # Check img SuperDraco
        print("----Changing Element: Draco -> SuperDraco is OK")
    # 4. Click Restore Down (middle window button - make window smaller)
        #driver.set_window_rect(width=1200, height=800)
        driver.set_window_size(600, 600)
        print("----Click Restore Down Browser Window is OK")
        h.delay()
    # 5. Check content display in restored window
        h.check_element(driver, h.superdraco_img_link)  # Check img SuperDraco
        print("----Check content display in restored down window (SuperDraco) is OK")
        h.check_clickable_element(driver, h.draco_link)  # Check link Draco
        h.check_element(driver, h.draco_img_link)  # Check img Draco
        print("----Changing Element: SuperDraco -> Draco is OK")
    # 6. Click Maximize (fullscreen)
        driver.maximize_window()
        print("----Maximize window is OK")
        h.delay()
    # 7. Check content display
        h.check_element(driver, h.draco_img_link) # Check img Draco
        print("----Check content display Draco is OK")
    # Test results for TC006
        print("   ")
        print("        !!!  DRAGON TC006 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_007_Dragon_Negative (self):
        driver = self.driver
    # TC007
        print("        ")
        print("        DRAGON TC007 NEGATIVE      ")
        print("        ---------------------    ")

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

    # 1. Find the Element by XPath
        dragon_video = driver.find_element(By.XPATH, h.dragon_video_link)
        print("----Find the Element by XPath " + dragon_video.text + " is OK")

    # 2. Scrolling to the Element
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",dragon_video)
        print("----Scrolling to Element "+ dragon_video.text + " is OK")
        h.delay()

    # 3. Click on image / Play icon to run video
        h.check_clickable_element(driver, h.dragon_video_link)  # Check link Video
        print("----Click on image / Play icon to run video is OK")

    # 4. Verify video starts playing
        driver.switch_to.default_content()

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='ulVZds71CZQ']")))
        driver.switch_to.frame(iframe)
        try:
            print("----Current iframe URL:", driver.execute_script("return window.location.href;"))

            self.assertTrue(h.check_video_playing(driver), "Dragon video is NOT playing!")
        finally:
            driver.switch_to.default_content()

    # 5. Click Minimize (minimize browser to taskbar)
        driver.minimize_window()
        print("----Click Minimize (minimize browser to taskbar) is OK")
        h.delay()

    # 6. Click Maximize (fullscreen)
        driver.maximize_window()
        print("----Maximize window is OK")
        h.delay()

    # 7. Check content display
        h.check_element(driver, h.dragon_video_link) # Check Video locator
        print("----Check content display Draco is OK")

    # Test results for TC007
        print("   ")
        print("        !!!  DRAGON TC007 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_008_Dragon_Negative (self):
        driver = self.driver
    # TC008
        print("        ")
        print("        DRAGON TC008 NEGATIVE      ")
        print("        ---------------------    ")

    # 1.  Opening SpaceX - Dragon site
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

    # 2. Scroll to bottom banner / carousel / slider
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("----Scroll to bottom banner is OK")

    # Find the Element by XPath
        swbutt_next = driver.find_element(By.XPATH, h.swbutt_next_link)
        print("----Find the Element by XPath swbutt_next is OK")
        h.check_clickable_element(driver, h.swbutt_next_link)

        swbutt_prev = driver.find_element(By.XPATH, h.swbutt_prev_link)
        print("----Find the Element by XPath swbutt_prev is OK")
        h.check_clickable_element(driver, h.swbutt_prev_link)

# 3. Click 10 times in a row on Next / forward arrow
        for i in range(10):
            swbutt_next.click()
        print("----Swbutt_next.click 10 times is OK")

#. 4. Click Minimize and then Maximize browser window
        driver.minimize_window()
        print("----Minimize_window is OK")
        h.delay()
        driver.maximize_window()
        print("----Maximize_window is OK")

# 5. Click 10 times in a row on Back / Previous / backward arrow
        for i in range(10):
            swbutt_prev.click()
        print("----Swbutt_prev.click 10 times is OK")
        h.delay()

    # Test results for TC008
        print("   ")
        print("        !!!  DRAGON TC008 NEGATIVE PASS   !!!        ")
        print("        -------------------------------------      ")

    def test_case_009_shop_spacex_Negative(self):
        driver = self.driver
    # TC009
        print("        ")
        print("        SHOP SPACEX TC009 NEGATIVE      ")
        print("        --------------------------    ")

    # 1. Opening Shop SpaceX site
        driver.get(h.Shop_SpaceX_url)

    # Verifying correct web page
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.shop_spacex_logo)))
        print("----Homepage_logo Shop SpaceX is OK")
        #h.delay()

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, h.shop_spacex_title)
        #h.delay()

    # Check URL
        h.check_URL(driver, h.Shop_SpaceX_url)

    # 2. Find Search Button Element by XPATH and Click
        search_btn = driver.find_element(By.XPATH, h.search_btn_link)
        #search_btn = wait.until(EC.invisibility_of_element_located((By.XPATH, h.search_btn_link)))
        print("----Find Element by XPATH Search Button is OK")
        h.check_element(driver, h.search_btn_link)
        print("----Search_btn_link Element checked is OK")
        search_btn.click()
        print("----Click on Search Button is OK")

    # Find Search field Element by XPATH
        search_input = driver.find_element(By.XPATH, h.search_input_link)
        print("----Find Element by XPATH Search Input is OK")
        h.check_element(driver, h.search_input_link)
        print("----Search_input_link Element checked is OK")

    # 3. Type special symbols "!@#$%^&()" into search field
        search_input.send_keys(h.negative_search_str)
        print("----Type special symbols ", h.negative_search_str, " into search field is OK")
        h.delay()

    # 4. Send key Enter
        search_input.send_keys(Keys.ENTER)
        print("----Send key Enter is OK")
        #h.delay()

    # 5. Check result
    # Show URL
        h.show_URL(driver)

    # Check API
        h.check_API(driver)

    # Checking title
        h.assert_title(driver, "Search result – SpaceX Store")

    # Check result output Title
        h.check_element(driver, h.search_res_link)
        print("----Search result text checked is OK")
    # Check result output 1 item
        h.check_element(driver, h.search_res_1_item_link)
        print("----Search result 1 item checked is OK")

    # Test results for TC009
        print("   ")
        print("        !!!  SHOP SPACEX TC009 NEGATIVE PASS   !!!        ")
        print("        ------------------------------------------      ")

    def test_case_010_shop_spacex_Negative(self):
        driver = self.driver
    # TC010
        print("        ")
        print("        SHOP SPACEX TC010 NEGATIVE      ")
        print("        --------------------------    ")

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

    # 2. Select 3rd item in-stock item and open its PDP (Product Display Page)
        scroll = str(500)
        self.driver.execute_script("document.body.style.zoom='50%'")
        print("----Shop SpaceX page ZOOM 50% is OK")
        driver.execute_script("window.scrollTo(0, " + scroll + ")")
        print("----Shop SpaceX page scrolled to " + scroll + " is OK")
        h.delay()
        h.check_clickable_element(driver, h.shop_item3_link)
        print("----Shop SpaceX item 3 Click is OK")
        h.delay()

    # 3. Find Quantity: field
        quantity = wait.until(EC.element_to_be_clickable((By.XPATH, h.quantity_link)))
        addToCart = wait.until(EC.element_to_be_clickable((By.XPATH, h.add_to_cart_link)))
        quantity.clear() # not work here
        quantity.send_keys("qwerty")
        print("----Shop SpaceX item 3 Quantity quantity.send_keys('qwerty') is OK")
        quantity.send_keys(Keys.TAB)

    # Getting a value from a field Quantity
        quantity_val = str(quantity.get_attribute("value"))

        h.check_element(driver, h.add_to_cart_link)
        addToCart.click()
        print("----Shop SpaceX item 3 addToCart.click() is OK")
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
        quantity_cart_val = str(quantity_cart.get_attribute("value"))

        if quantity_val == quantity_cart_val:
            print("----Quantity Cart = " + str(quantity_val) + " is OK")
        else:
            print(h.red, "----Quantity Cart = " + str(quantity_val) + " is NOT OK", h.dft)

    # Test results for TC010
        print("   ")
        print("        !!!  SHOP SPACEX TC010 NEGATIVE PASS   !!!        ")
        print("        ------------------------------------------      ")


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


