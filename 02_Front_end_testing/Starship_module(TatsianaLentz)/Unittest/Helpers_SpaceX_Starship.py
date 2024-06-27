# Helpers for tatsianaL_starship_unittest.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests


def delay():
    time.sleep(random.randint(1, 4))

# ------------------------------Helpers for SpaceX site-------------------------------


# SpaceX site URL
SpaceX_url = "https://www.spacex.com/"


# Homepage API check
def check_api(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("----API check: Url has ", requests.get(driver.current_url).status_code, " as Status Code")
        print("----API response code is OK")
    else:
        print("ATTENTION! API response code is not 200", "Current code is:", code)


# Homepage title check
def assert_title(driver, title):
    wait = WebDriverWait(driver, 6)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("----Title check: Page has, " + driver.title + " as Page title")
    if title not in driver.title:
        print("ATTENTION! Page " + title + " has wrong Title!")
        driver.get_screenshot_as_file('Wrong title.png')


# Verify homepage logo
homepage_logo = '//*[@class="header-inner"]'


# Verify and Validate Starship link
starship_link = "(//a[contains(.,'Starship')])[1]"


# Starship page title check
def starship_title_check(driver):
    if "Starship" not in driver.title:
        raise Exception("ATTENTION! Title is different on Spacex-Starship page!")
    else:
        print("----Title check: Page has", driver.title + " as page title")

# ------------------------ Helpers for OFFICIAL SPACEX STORE ----------------------------------


# SpaceX shop URL
shop_url = "https://shop.spacex.com/"

# Shop homepage logo
shop_homepage_logo = "(//img[@alt='SpaceX Store'])[1]"


# Shop API check
def shop_api_check(driver):
    print("----API check: Url has", requests.get("https://shop.spacex.com/").status_code, "as status Code")
    code = requests.get("https://shop.spacex.com/").status_code
    if code == 200:
        print("----API response code is OK")
    else:
        print("ATTENTION! API response code is not 200", "Current code is:", code)


# Shop title check
def shop_title_check(driver):
    try:
        assert driver.title == "Official SpaceX Store"
        print("----Title check: Page has, " + driver.title + " as Page title")
    except AssertionError:
        print("ATTENTION! Title is different. Current Title is:", driver.title)


# Account link
shop_account_link = "(//a[contains(.,'Account')])[2]"