from playwright.sync_api import Page, expect
import helpers as h
import time

def test_case_006_Dragon_Negative (page: Page):
    print("\n")
# 1. Open https://www.spacex.com/vehicles/dragon/
    page.goto(h.DRAGON)
    # Checking page
    h.open_checked(page, h.DRAGON, h.dragon_homepage_logo,h.dragon_title)
# 2. Scroll to ENGINES section and click SuperDraco / Draco link to switch engines
    # Checking h.draco_link
    expect(page.locator(h.draco_link)).to_be_visible()
    # Scroll to ENGINES section
    page.locator(h.draco_link).scroll_into_view_if_needed()
    print("----Scroll to Draco: Done")

    draco = page.locator(h.draco_link)
    print("----Find Draco: Done")
    expect(draco).to_be_visible()
    print("----Draco is visible: OK")
    superdraco = page.locator(h.superdraco_link)
    print("----Find SuperDraco: Done")
    expect(superdraco).to_be_visible()
    print("----SuperDraco is visible: OK")
    superdraco.click()
    print("----SuperDraco clicked: OK")
# 3. Verify section content changes
    expect(page.locator(h.superdraco_img_link)).to_be_visible()
    print("----SuperDraco img is visible: OK")
# 4. Click Restore Down (middle window button - make window smaller)
    page.set_viewport_size({"width": 600, "height": 600})
    print("----Page size 600x600 : OK")
# 5. Check content display in restored down window
    expect(page.locator(h.superdraco_img_link)).to_be_visible()
    print("----SuperDraco img is visible: OK")

    draco.click()
    expect(page.locator(h.draco_img_link)).to_be_visible()
    print("----Draco img is visible: OK")
# 6. Click Maximize (fullscreen)
    page.set_viewport_size({"width": 1920, "height": 1080})
# 7. Check content display
    expect(page.locator(h.draco_img_link)).to_be_visible()
    print("----Draco img is visible: OK")

def test_case_007_Dragon_Negative (page: Page):
    print("\n")
# 1. Open https://www.spacex.com/vehicles/dragon/
    page.goto(h.DRAGON)
    # Checking page
    h.open_checked(page, h.DRAGON, h.dragon_homepage_logo, h.dragon_title)
# 2. Find block / image with Dragon parachute system video
    video = page.locator(h.dragon_video_link)
    expect(page.locator(h.dragon_video_link)).to_be_visible()
    print("----Dragon parachute system video is visible: OK")
    video.scroll_into_view_if_needed()
    print("----Scroll to Dragon parachute system video: OK")
    page.wait_for_timeout(1000)
# 3. Click on Dragon parachute video
    print("Clicked element:", video.evaluate("(el) => el.outerHTML"))
    # Verify element is inside viewport
    expect(video).to_be_in_viewport()
    print("----Video is in viewport: OK")
    video.click()
    print("----Video.click: OK")
# 4. Verify video playback
    frame = page.frame_locator("iframe[src*='ulVZds71CZQ']")
    #h.check_video_playing(frame)
    h.check_video_playing(page, "ulVZds71CZQ")
# 5. Click Minimize (minimize browser to taskbar)
    page.wait_for_timeout(2000)
    h.resize_browser_window(page,522,522)
    page.wait_for_timeout(2000)
# 6. Restore browser and click Maximize
    h.maximize_browser_window(page)
    page.wait_for_timeout(2000)


def test_case_008_Dragon_Negative (page: Page):
    print("\n")
    print("test_case_008_Dragon_Negative")
# 1. Open https://www.spacex.com/vehicles/dragon/
    page.goto(h.DRAGON)
    # Checking page
    h.open_checked(page, h.DRAGON, h.dragon_homepage_logo, h.dragon_title)
# 2. Scroll to bottom banner / carousel / slider
    expect(page.locator(h.botbanner)).to_be_visible()
    banner = page.locator(h.botbanner)
    banner.scroll_into_view_if_needed()
    print("Scroll to bottom banner: Done")
# 3. Click 10 times in a row on Next / forward arrow
    expect(page.locator(h.swbutt_next_link)).to_be_visible()
    print("----Expect(page.locator(h.swbutt_next_link)).to_be_visible(): Done")
    nextt = page.locator(h.swbutt_next_link)
    countn=0
    for i in range(1,11):
        if nextt.is_enabled():
            nextt.click()
            countn += 1
            print("----Next Click: Ok ", i)
        else:
            print(f"----Can't click next ({i})")
    print(f"----Next.click() {countn} times: Done")
# 4. Click Minimize and then Maximize browser window
    h.minimize_browser_window(page)
    print("----Мinimize_browser_window: Done")
    time.sleep(2)
    h.maximize_browser_window(page)
    print("----Maximize_browser_window: Done")
    time.sleep(2)
# 5. Click 10 times in a row on Back / Previous / backward arrow
    expect(page.locator(h.swbutt_prev_link)).to_be_visible()
    print("----Expect(page.locator(h.swbutt_prev_link)).to_be_visible(): Done")
    prev = page.locator(h.swbutt_prev_link)
    countp=0
    for j in range(1,11):
        if prev.is_enabled():
            prev.click()
            countp+=1
            print("----Prev Click: Ok ", j)
        else:
            print(f"----Can't click prev ({j})")
    print(f"----Prev.click() {countp} times: Done")
