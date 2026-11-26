from pathlib import Path
from datetime import datetime
from playwright.sync_api import Page, FrameLocator, expect
from playwright.sync_api import Page

# Color codes
red = "\033[31m" # red
gre = "\033[32m" # green
dft = "\033[0m" # default/white

SPACEX = 'https://www.spacex.com/'
DRAGON = 'https://www.spacex.com/vehicles/dragon'
SHOP = 'https://shop.spacex.com/'
CART = 'https://shop.spacex.com/cart'
ITEM_QUANTITY = '1'
NEGATIVE_SEARCH = '!@#$%^&()'

# Original Selenium XPath locators (Playwright supports XPath directly).
#vehicles_link = "//*[normalize-space()='Vehicles']"
vehicles_link = "//span[text() = 'Vehicles']"
dragon_link = "//a[normalize-space()='Dragon']"
starship_link = "//a[normalize-space()='Starship']"
falcon_9_link = "//a[normalize-space()='Falcon 9']"
falcon_h_link = "//a[normalize-space()='Falcon Heavy']"
shop_link = "//*[text()='Shop']"
shop_spacex_link = '//*[@href="https://shop.spacex.com"]'
superdraco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-1']"
superdraco_img_link = '//img[contains(@src , "SuperDraco")]'
draco_link = "//div[@class='inner-left-top']//button[@id='section-tab-button-0']"
draco_img_link = '//img[contains(@src , "/Draco") ]'
shop_item2_link = "//img[@alt='Starship Milestone First Orbital Flight Mission Patch']"
shop_item3_link = '//img[@data-image-id="44600129650767"]'
#dec_quantity = "//span[@data-action='decrease-quantity']"
dec_quantity = "//button[@aria-label='Decrease quantity']"
#inc_quantity = "//span[@data-action='increase-quantity']"
inc_quantity = "//button[@aria-label='Increase quantity']"
quantity_link = "//input[@name='quantity']"
add_to_cart_link = "//button[@type='submit']"
cart_quantity_link = "//tr[@class='CartItem']//div[@class='QuantitySelector']//input[contains(@name,'updates[')]"
dragon_video_link = "//picture[@class='responsive-image']//*[@class='play-arrow']//*[name()='svg']//*[name()='path' and contains(@d,'M400-280v-')]"
swbutt_next_link = '//*[@class="swiper-controls bottom-swiper-controls"]//*[@class="swiper-button swiper-next"]'
swbutt_prev_link = '//*[@class="swiper-controls bottom-swiper-controls"]//*[@class="swiper-button swiper-previous"]'

pagination_next_link = "//a[@title='Next page']"
search_items_link = "//ul[contains(@class,'ProductList')]/li"
search_btn_link = '//button[text()="Search"]'
search_input_link = '//input[@id="search-input"]'
search_res_link = f'''//*[contains(text(), 'results for "{NEGATIVE_SEARCH}"')]'''
search_res_1_item_link = "//main[@id='main']//li[1]"
search_res_title = "Search result – SpaceX Store"
#homepage_logo = '//*[@class="section-inner feature"]'
homepage_logo = "//*[name()='path' and contains(@d,'M33.4556 7')]"
dragon_homepage_logo = "//div[@class='inner-center']//h1[@id='header']"
shop_spacex_logo = '//*[@class="Slideshow__Image hide-no-js lazyautosizes Image--lazyLoaded"]'
cart_header = '//*[text() = "Cart"]'
home_title = 'SpaceX'
dragon_title = 'SpaceX - Dragon'
shop_spacex_title = 'Official SpaceX Store'
cart_title = 'Your Shopping Cart – SpaceX Store'
botbanner = "//swiper-slide[@aria-label='1 / 5']//div[@class='section-inner']"

def check_element(page: Page, xpath: str):
    el = page.locator(xpath).first
    expect(el).to_be_visible(timeout=10000)
    print('----Element visible:', xpath)
    return el


def check_clickable_element(page: Page, xpath: str):
    el = check_element(page, xpath)
    expect(el).to_be_enabled()
    #el.click()
    print('----Clickable element checked:', xpath)
    return el


def check_url(page: Page, url: str):
    expect(page).to_have_url(url, timeout=15000)
    print('----URL OK:', page.url)


def check_title(page: Page, title: str):
    expect(page).to_have_title(title, timeout=15000)
    print('----Title OK:', page.title())


def check_api(page: Page):
    # Similar to requests.get(current_url), but uses Playwright's API client.
    response = page.request.get(page.url, timeout=20000)
    assert response.status in (200, 429), f'HTTP status {response.status}: {page.url}'
    print('----API status:', response.status)

def open_checked(page: Page, url: str, logo: str, title: str):
    check_url(page, url)
    check_title(page, title)
    check_element(page, logo)
    check_api(page)


def check_video_playing0(frame: FrameLocator):
    player = frame.locator("#movie_player")
    video = frame.locator("video.html5-main-video")
  # Wait for player
    expect(player).to_be_attached(timeout=15000)
  # Start video
    player.evaluate("(el) => el.playVideo()")
  # Verify video is playing
    expect(video).to_have_js_property("paused", False, timeout=15000)
  # Verify video data is loaded
    expect(video).to_have_js_property("readyState", 4, timeout=15000)
  # Verify playback progress
    expect(video).not_to_have_js_property("currentTime", 0, timeout=15000)
    print("----YouTube video is playing: OK")


def screenshot_on_failure(page: Page, test_name: str):
    folder = Path(__file__).parent / 'Screenshots'
    folder.mkdir(exist_ok=True)
    path = folder / f'{test_name}_{datetime.now():%Y%m%d_%H%M%S_%f}.png'
    page.screenshot(path=str(path), full_page=True, timeout=10000)
    print('----Screenshot:', path)

def check_quantity (page: Page, quantity_val1, quantity_cart_val1):
    quantity_val = quantity_val1
    quantity_cart_val = quantity_cart_val1

    if quantity_val == quantity_cart_val:
        print("----Quantity Cart = " + str(quantity_cart_val) + " = Quantity = ", str(quantity_val))
    else:
        print(red, "----Quantity Cart = " + str(quantity_cart_val) + " != Quantity = ", str(quantity_val), dft)
        raise AssertionError("----Quantity Cart = " + str(quantity_cart_val) + " != Quantity = ", str(quantity_val))

def check_video_playing(page: Page, expected_video_id: str):
    """
    Verify YouTube video:
    1. Correct iframe URL
    2. Video is playing
    3. Playback time is increasing
    """
    # 1. Expected YouTube URL
    expected_url = f"https://www.youtube.com/embed/{expected_video_id}"
    # 2. Find YouTube iframe
    iframe = page.locator(f"iframe[src*='{expected_video_id}']")
    expect(iframe).to_be_attached(timeout=15000)
    # 3. Verify URL
    actual_url = iframe.get_attribute("src")
    assert actual_url is not None, "YouTube iframe URL is missing"

    actual_url_clean = actual_url.split("?")[0]

    assert actual_url_clean == expected_url, (f"YouTube URL mismatch! "
        f"Expected: {expected_url}, Actual: {actual_url_clean}")

    print(f"----YouTube URL OK: {actual_url_clean}")

    # 4. Find video inside iframe
    frame = iframe.content_frame
    video = frame.locator("video.html5-main-video")

    expect(video).to_be_attached(timeout=15000)

    # 5. Verify video is playing
    expect(video).to_have_js_property("paused", False, timeout=15000)

    print("----YouTube video is playing: OK")

    # 6. Get playback time
    start_time = video.evaluate("(v) => v.currentTime")

    page.wait_for_timeout(3000)

    end_time = video.evaluate("(v) => v.currentTime")

    # 7. Verify playback time is increasing
    assert end_time > start_time, (f"YouTube video is not progressing! "
        f"Start: {start_time:.2f}s, End: {end_time:.2f}s")

    # 8. Format playback time
    def format_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    print(f"----YouTube playback time: " f"{start_time:.2f}s -> {end_time:.2f}s "
        f"(progress: {end_time - start_time:.2f}s) OK")

def resize_browser_window(page: Page, width: int, height: int):
    cdp = page.context.new_cdp_session(page)
    try:
        window_id = cdp.send("Browser.getWindowForTarget")["windowId"]
        # Restore Chrome window
        cdp.send("Browser.setWindowBounds",
                 {"windowId": window_id, "bounds": {"windowState": "normal"}})
        page.wait_for_timeout(500)
        # Resize Chrome window
        cdp.send("Browser.setWindowBounds",
                 {"windowId": window_id, "bounds": {"width": width, "height": height}})
        page.wait_for_timeout(500)
        # Get actual window size
        bounds = cdp.send("Browser.getWindowBounds",
                          {"windowId": window_id})["bounds"]
        actual_width = bounds["width"]
        actual_height = bounds["height"]
        print(f"----Requested window size: {width}x{height}")
        print(f"----Actual window size: {actual_width}x{actual_height}")
        # Verify dimensions with 2px tolerance
        assert abs(actual_width - width) <= 2, (
            f"Chrome width mismatch: {width} != {actual_width}")
        assert abs(actual_height - height) <= 2, (
            f"Chrome height mismatch: {height} != {actual_height}")
        print("----Chrome window resize: OK")

    finally:
        cdp.detach()

def maximize_browser_window(page: Page):
    cdp = page.context.new_cdp_session(page)
    try:
        window_id = cdp.send("Browser.getWindowForTarget")["windowId"]
        # Restore window to normal state
        cdp.send("Browser.setWindowBounds",
                 {"windowId": window_id, "bounds": {"windowState": "normal"}})
        # Maximize Chrome window
        cdp.send("Browser.setWindowBounds",
                 {"windowId": window_id, "bounds": {"windowState": "maximized"}})
        # Verify window state
        bounds = cdp.send("Browser.getWindowBounds",
                          {"windowId": window_id})["bounds"]
        assert bounds["windowState"] == "maximized"
        print("----Chrome window maximized: OK")
    finally:
        cdp.detach()

def minimize_browser_window(page: Page):
    cdp = page.context.new_cdp_session(page)
    try:
        window_id = cdp.send("Browser.getWindowForTarget")["windowId"]
        # Minimize Chrome window to taskbar
        cdp.send("Browser.setWindowBounds",
                 {"windowId": window_id, "bounds": {"windowState": "minimized"}})
        # Verify window state
        bounds = cdp.send ("Browser.getWindowBounds",
                           {"windowId": window_id})["bounds"]
        assert bounds["windowState"] == "minimized"
        print("----Chrome window minimized: OK")
    finally:
        cdp.detach()

def search_items_count1 (page: Page):
    total_count = 0
    page_number = 1

    while True:
        page.wait_for_load_state("domcontentloaded")

        products = page.locator(search_items_link)

        count = products.count()
        total_count += count

        print(f"----Page {page_number}: {count} products")

        next_page = page.locator(pagination_next_link)

        if not next_page.is_visible():
            break

        # Get the URL of the next page
        next_url = next_page.get_attribute("href")

        # Click Next and wait for navigation
        next_page.click()
        page.wait_for_url(f"**{next_url}")
        page.wait_for_load_state("domcontentloaded")

        page_number += 1

    print(f"----Total pages: {page_number}")
    print(f"----Total products found: {total_count}")

    return total_count


def search_items_count(page: Page):

    # Get expected products count from the title
    result_title = page.locator(search_res_link)
    expect(result_title).to_be_visible()

    expected_count = int(result_title.inner_text().split()[0])

    print(f"----Expected products count: {expected_count}")

    total_count = 0
    page_number = 1

    while True:
        page.wait_for_load_state("domcontentloaded")

        products = page.locator(search_items_link)

        count = products.count()
        total_count += count

        print(f"----Page {page_number}: {count} products")

        next_page = page.locator(pagination_next_link)

        if not next_page.is_visible():
            break

        next_url = next_page.get_attribute("href")

        next_page.click()
        page.wait_for_url(f"**{next_url}")
        page.wait_for_load_state("domcontentloaded")

        page_number += 1

    print(f"----Total pages: {page_number}")
    print(f"----Products count in header: {expected_count}")
    print(f"----Actual products found: {total_count}")

    if expected_count == total_count:
        print("----Products count verification: PASSED")
    else:
        print("----Products count verification: FAILED")

    assert expected_count == total_count, (
        f"Products count mismatch: "
        f"Expected {expected_count}, Actual {total_count}"
    )

    return total_count




#################################################################################
"""
How to show print() in terminal
Add flag -s:

pytest test_playwright_Dragon_Positive.py -v -s

- -s — shows output print() in real time.
- -v — shows detailed name of the tests.
"""
#################################################################################
"""
How to do that print() will be shown all the time
Create in folder Playwright file pytest.ini:

[pytest]
addopts = -v -s

Now you can run tests like this:
pytest test_playwright_Dragon_Positive.py
"""
#################################################################################