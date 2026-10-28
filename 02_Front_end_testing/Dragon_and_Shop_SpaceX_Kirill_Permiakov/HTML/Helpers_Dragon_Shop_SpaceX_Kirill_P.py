import inspect
import unittest
from datetime import datetime
import os
import random
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE, TimeoutException, WebDriverException

# Color codes
red = "\033[31m" # red
gre = "\033[32m" # green
dft = "\033[0m" # default/white

item_quantity = "1"
negative_search_str = "!@#$%^&()"
#negative_search_str = "!@#$%^&()-_/777"

SpaceX_url = "https://www.spacex.com/"
Dragon_url = "https://www.spacex.com/vehicles/dragon"
Shop_SpaceX_url = "https://shop.spacex.com/"
Cart_url = "https://shop.spacex.com/cart"

vehicles_link = "//*[normalize-space()='Vehicles']"
dragon_link = "//a[normalize-space()='Dragon']"
starship_link = "//a[normalize-space()='Starship']"
falcon_9_link = "//a[normalize-space()='Falcon 9']"
falcon_h_link = "//a[normalize-space()='Falcon Heavy']"
shop_link = "//*[text()='Shop']"
shop_spacex_link = '//*[@href="https://shop.spacex.com"]'

superdraco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-1']"
superdraco_img_link = '//img[contains(@src , "SuperDraco")]'
draco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-0']"
draco_img_link = '//img[contains(@src , "/Draco")]'
shop_item2_link = "//img[@alt='Starship Milestone First Orbital Flight Mission Patch']"
shop_item3_link = '//img[@data-image-id="44600129650767"]'
dec_quantity = "//span[@data-action='decrease-quantity']"
inc_quantity = "//span[@data-action='increase-quantity']"
quantity_link = "//input[@name='quantity']"
add_to_cart_link = "//button[@type='submit']"
cart_quantity_link = "//tr[@class='CartItem']//div[@class='QuantitySelector']//input[contains(@name,'updates[')]"
dragon_video_link = "//picture[@class='responsive-image']//*[@class='play-arrow']//*[name()='svg']//*[name()='path' and contains(@d,'M400-280v-')]"
swbutt_next_link = '//*[@class="swiper-controls bottom-swiper-controls"]//*[@class="swiper-button swiper-next"]'
swbutt_prev_link = '//*[@class="swiper-controls bottom-swiper-controls"]//*[@class="swiper-button swiper-previous"]'
#search_btn_link = "//button[normalize-space()='Search']"
search_btn_link = '//button[text()="Search"]'
#search_btn_link = "//button[@class='Header__Icon Icon-Wrapper Icon-Wrapper--clickable hidden-desk is-expanded']"
#search_btn_link = """//button[@class='Header__Icon Icon-Wrapper Icon-Wrapper--clickable hidden-desk' and @aria-label="Open search bar"]"""


search_input_link = '//input[@id="search-input"]'
search_res_link = f"""//*[contains(text(), 'results for "{negative_search_str}"')]"""
search_res_1_item_link = "//main[@id='main']//li[1]"

# Verify homepage logo
homepage_logo = '//*[@class="section-inner feature"]'
dragon_homepage_logo = "//div[@class='inner-center']//h1[@id='header']"
shop_spacex_logo = '//*[@class="Slideshow__Image hide-no-js lazyautosizes Image--lazyLoaded"]'
cart_header = '//*[text() = "Cart"]'

home_title = "SpaceX"
dragon_title = "SpaceX - Dragon"
shop_spacex_title = "Official SpaceX Store"
cart_title = "Your Shopping Cart – SpaceX Store"

# Take a Screenshot
def take_screenshot(driver):

    # Get helper function name
    helper_name = inspect.stack()[1].function

    # Get current unittest test name
    test_name = "Unknown_Test"

    for frame in inspect.stack():
        test_self = frame.frame.f_locals.get("self")

        if isinstance(test_self, unittest.TestCase):
            test_name = test_self._testMethodName
            break

    # Screenshots folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(current_dir, "Screenshots")
    os.makedirs(folder, exist_ok=True)

    # Current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Screenshot filename
    filename = f"{test_name}_{helper_name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # Save screenshot
    saved = driver.save_screenshot(filepath)

    if saved:
        print("----Screenshot saved:", filepath)
    else:
        raise AssertionError("Screenshot NOT saved!")

def delay():
    time.sleep(random.randint(1, 4))

# Homepage API check
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200 or code == 429:
        print("----API check: Url has ", code, " as Status Code")
        print("----API response code is OK")
    else:
        take_screenshot(driver)
        print(red,"ATTENTION! API response code is not 200 or 429", "Current code is:", code,dft)
        raise AssertionError(f"API check FAILED! Status Code: {code}")
        #assert False, f"API check FAILED! Status Code: {code}"

# Homepage title check
def assert_title(driver, title):
    print("----assert_title")
    wait = WebDriverWait(driver, 6)
    try:
        wait.until(EC.title_is(title))
    except WDE:
        take_screenshot(driver)
        print(red,"ATTENTION! Page " + title + " has wrong Title Wait Time!(WDE) - ", driver.title, dft)
        driver.get_screenshot_as_file('Wrong_Title_Wait.png')
        raise AssertionError("ATTENTION! Page " + title + " has wrong Title Wait Time!(WDE) - ", driver.title)
    try:
        assert title in driver.title
        print("----Title check: Page has, " + "'" + driver.title + "'" + " title as Page title")
    except AssertionError:
        take_screenshot(driver)
        print(red,"ATTENTION! Page " + title + " has wrong Title!(AssertionError) - ", driver.title,dft)
        driver.get_screenshot_as_file('Wrong_Title.png')
        raise AssertionError("ATTENTION! Page " + title + " has wrong Title!(AssertionError) - ", driver.title)
    except WDE:
        take_screenshot(driver)
        print(red,"ATTENTION! Page " + title + " has wrong Title!(WDE) - ", driver.title,dft)
        driver.get_screenshot_as_file('Wrong_Title.png')
        raise AssertionError("ATTENTION! Page " + title + " has wrong Title!(WDE) - ", driver.title)


# Dragon page title check
def dragon_title_check(driver, title = "Dragon"):
    print("----dragon_title_check")
    if "Dragon" not in driver.title:
        take_screenshot(driver)
        print(red,"ATTENTION! Page " + title + " has wrong Title!",dft)
        raise AssertionError("ATTENTION! Page " + title + " has wrong Title!")
    else:
        print("----Title check: Page has", driver.title + " as page title")

# URL check
def check_URL(driver, c_url):
    cur_url = driver.current_url
    chk_url = c_url
    if cur_url == chk_url:
        print("----Current URL: " + driver.current_url + " is OK")
    else:
        take_screenshot(driver)
        print(red,"ATTENTION! Current URL is not " + chk_url + " Current url is:", cur_url,dft)
        raise AssertionError("ATTENTION! Current URL is not " + chk_url + " Current url is:", cur_url)

# Element check and Click
def check_clickable_element (driver, locator):
    element = driver.find_element(By.XPATH, locator)
    print("----check_clickable_element " + element.text)
    if element.is_displayed():
        print("----Element " + element.text + " is displayed OK")
    else:
        take_screenshot(driver)
        print(red,"ATTENTION! Element " + element.text + " is NOT displayed OK",dft)
        raise AssertionError("ATTENTION! Element " + element.text + " is NOT displayed OK")
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(element)).click()
        print("----Element " + element.text + " is clickable OK")
        print("----Element " + element.text + " is Clicked OK")
    except WDE:
        take_screenshot(driver)
        print(red,"ATTENTION! Element " + element.text + " is NOT clickable!",dft)
        raise AssertionError("ATTENTION! Element " + element.text + " is NOT clickable!")

# Element check
def check_element (driver, locator):
    try:
        element = driver.find_element(By.XPATH, locator)
        print("----check_element " + element.text)
    except WDE:
        take_screenshot(driver)
        print(red, "----NO such element " + element.text, dft)
        raise AssertionError("----NO such element " + element.text)
    if element.is_displayed():
        print("----Element " + element.text + " is displayed OK")
    else:
        take_screenshot(driver)
        print(red,"ATTENTION! Element " + element.text + " is NOT displayed OK",dft)
        raise AssertionError("ATTENTION! Element " + element.text + " is NOT displayed OK")
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, locator)))
        print("----Element " + element.text + " presence_of_element_located is OK")
    except WDE:
        take_screenshot(driver)
        print(red,"ATTENTION! Element " + element.text + " is NOT presence_of_element_located!",dft)
        raise AssertionError("ATTENTION! Element " + element.text + " is NOT presence_of_element_located!")


 # -----------------------------------Negative functions-----------------------------------

# Video playing check
def check_video_playing(driver):
    print("----check_video_playing")
    try:
        pause_locator = "//button[contains(@class,'player-control-play-pause-icon') and @aria-label='Pause video']"
        timer_locator = "//span[contains(@class,'ytwPlayerTimeDisplayTimeElapsed')]/span[@aria-hidden='true']"

        pause_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, pause_locator)))
        print("----YouTube button:", pause_button.get_attribute("aria-label"))

        timer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, timer_locator)))
        start_time = timer.get_attribute("textContent").strip()
        print("----Video start time:", start_time)

        time.sleep(3)

        timer = driver.find_element(By.XPATH, timer_locator)
        current_time = timer.get_attribute("textContent").strip()
        print("----Video current time:", current_time)

        pause_button = driver.find_element(By.XPATH, pause_locator)

        if start_time != current_time and pause_button.get_attribute("aria-label") == "Pause video":
            print("----Video is playing OK")
            return True

        print("----ATTENTION! Video is NOT playing!")
        # return False
        take_screenshot(driver)
        raise AssertionError("----ATTENTION! Video is NOT playing!")

    except TimeoutException:
        take_screenshot(driver)
        print("----ATTENTION! YouTube controls NOT found!")
        #return False
        raise AssertionError("----ATTENTION! YouTube controls NOT found!")

# show URL
def show_URL(driver):
    cur_url = driver.current_url
    print("----Current URL: " + cur_url + " is OK")
