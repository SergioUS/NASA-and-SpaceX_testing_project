import random
import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE

# Color codes
red = "\033[31m" # red
gre = "\033[32m" # green
dft = "\033[0m" # default/white

SpaceX_url = "https://www.spacex.com/"
Dragon_url = "https://www.spacex.com/vehicles/dragon"
Shop_SpaceX_url = "https://shop.spacex.com/"

vehicles_link = "//*[normalize-space()='Vehicles']"
dragon_link = "//a[normalize-space()='Dragon']"
starship_link = "//a[normalize-space()='Starship']"
falcon_9_link = "//a[normalize-space()='Falcon 9']"
falcon_h_link = "//a[normalize-space()='Falcon Heavy']"
shop_link = "//*[text()='Shop']"
shop_spacex_link = '//*[@href="https://shop.spacex.com"]'

superdraco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-1']"
draco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-0']"

# Verify homepage logo
homepage_logo = '//*[@class="section-inner feature"]'
dragon_homepage_logo = "//div[@class='inner-center']//h1[@id='header']"
shop_spacex_logo = '//*[@class="Slideshow__Image hide-no-js lazyautosizes Image--lazyLoaded"]'
#shop_spacex_logo = "//img[contains(@class, 'Slideshow__Image')]"

home_title = "SpaceX"
dragon_title = "SpaceX - Dragon"
shop_spacex_title = "Official SpaceX Store"


def delay():
    time.sleep(random.randint(1, 4))

# Homepage API check
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("----API check: Url has ", requests.get(driver.current_url).status_code, " as Status Code")
        print("----API response code is OK")
    else:
        print(red,"ATTENTION! API response code is not 200", "Current code is:", code,dft)

# Homepage title check
def assert_title(driver, title):
    print("----assert_title")
    wait = WebDriverWait(driver, 6)
    try:
        wait.until(EC.title_is(title))
    except WDE:
        print(red,"ATTENTION! Page " + title + " has wrong Title Wait Time!(WDE)",dft)
        driver.get_screenshot_as_file('Wrong_Title_Wait.png')
    try:
        assert title in driver.title
        print("----Title check: Page has, " + "'" + driver.title + "'" + " title as Page title")
    except AssertionError:
        print(red,"ATTENTION! Page " + title + " has wrong Title!(AssertionError)",dft)
        driver.get_screenshot_as_file('Wrong_Title.png')
    except WDE:
        print(red,"ATTENTION! Page " + title + " has wrong Title!(WDE)",dft)
        driver.get_screenshot_as_file('Wrong_Title.png')


# Dragon page title check
def dragon_title_check(driver, title = "Dragon"):
    print("----dragon_title_check")
    if "Dragon" not in driver.title:
        #raise Exception("ATTENTION! Title is different on Spacex-Dragon page!")
        print(red,"ATTENTION! Page " + title + " has wrong Title!",dft)
    else:
        print("----Title check: Page has", driver.title + " as page title")

# URL check
def check_URL(driver, c_url):
    cur_url = driver.current_url
    chk_url = c_url
    if cur_url == chk_url:
        print("----Current URL: " + driver.current_url + " is OK")
    else:
        print(red,"ATTENTION! Current URL is not " + chk_url + " Current url is:", cur_url,dft)

# Element check
def check_clickable_element (driver, locator):
    element = driver.find_element(By.XPATH, locator)
    print("----check_clickable_element " + element.text)
    if element.is_displayed():
        print("----Element " + element.text + " is displayed OK")
    else:
        print(red,"ATTENTION! Element " + element.text + " is NOT displayed OK",dft)
    try:
        #element = driver.find_element(By.XPATH, el)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(element)).click()
        print("----Element " + element.text + " is clickable OK")
        print("----Element " + element.text + " is Clicked OK")
    except WDE:
        print(red,"ATTENTION! Element " + element.text + " is NOT clickable!",dft)


