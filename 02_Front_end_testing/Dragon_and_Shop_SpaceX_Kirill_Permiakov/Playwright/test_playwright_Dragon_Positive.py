from playwright.sync_api import Page, expect
import helpers as h

def test_case_006_Dragon_Positive (page: Page):
    print("\n")
# 1. Open browser and go to https://www.spacex.com/
    page.goto(h.SPACEX)
# Checking page title
    expect(page).to_have_title(h.home_title)
    print("The Page has a title:" , page.title())
# Checking page url
    expect(page).to_have_url(h.SPACEX)
    print("The Page has a url:" , page.url)
# Checking page logo
    expect(page.locator(h.homepage_logo)).to_be_visible()
    print("The Page has a visible homepage_logo")
# 2. Hover over VEHICLES in the top header
    expect(page.locator(h.vehicles_link)).to_be_visible()
    print("Menu VEHICLES is visible")
    vehicles = page.locator(h.vehicles_link)
    vehicles.hover()
    print("Mouse hovered over VEHICLES")
# 3. Verify dropdown appears with items: StarShip, Dragon, Falcon 9, Falcon Heavy, etc.
    expect(page.locator(h.dragon_link)).to_be_visible()
    print("Menu VEHICLES/dragon   is visible")
    expect(page.locator(h.falcon_h_link)).to_be_visible()
    print("Menu VEHICLES/falcon_h is visible")
    expect(page.locator(h.falcon_9_link)).to_be_visible()
    print("Menu VEHICLES/falcon_9 is visible")
    expect(page.locator(h.starship_link)).to_be_visible()
    print("Menu VEHICLES/starship is visible")
# 4. Click on Dragon
    page.locator(h.dragon_link).click()
    print("Menu VEHICLES/dragon   Click: Done")
# 5. Check page URL and Title
# Checking page title
    expect(page).to_have_title(h.dragon_title)
    print("The Page has a title:" , page.title())
# Checking page url
    expect(page).to_have_url(h.DRAGON)
    print("The Page has a url:" , page.url)

def test_case_007_Dragon_Positive (page: Page):
    print("\n")
#1. Open page https://www.spacex.com/vehicles/dragon/
    page.goto(h.DRAGON)
#2. Check URL in browser address bar
    expect(page).to_have_url(h.DRAGON)
    print("The Page has a url:" , page.url)
#3. Refresh page (F5) and verify URL stays the same
    page.reload()
    expect(page).to_have_url(h.DRAGON)
    print("The Page has a url:" , page.url)

def test_case_008_Dragon_Positive (page: Page):
    print("\n")
# 1. Open page https://www.spacex.com/vehicles/dragon/
    page.goto(h.DRAGON)
# Checking page
    h.open_checked(page, h.DRAGON, h.dragon_homepage_logo, h.dragon_title)
# 2. Scroll down to ENGINES section
    page.locator(h.draco_link).scroll_into_view_if_needed()
    print("----Scroll to Draco: Done")
# 3. Find Draco and SuperDraco links
    draco = page.locator(h.draco_link)
    print("----Find Draco: Done")
    expect(draco).to_be_visible()
    print("----Draco is visible: OK")
    superdraco = page.locator(h.superdraco_link)
    print("----Find SuperDraco: Done")
    expect(superdraco).to_be_visible()
    print("----SuperDraco is visible: OK")
# 4. Click on Draco and SuperDraco links
    superdraco.click()
    print("----SuperDraco is clicked: OK")
    expect(page.locator(h.superdraco_img_link)).to_be_visible()
    print("----SuperDraco img is visible: OK")

    draco.click()
    print("----Draco is clicked: OK")
    expect(page.locator(h.draco_img_link)).to_be_visible()
    print("----Draco img is visible: OK")
