from playwright.sync_api import Page, expect
from faker import Faker
import helpers as h

fake = Faker("en_US")

def test_example(page: Page) -> None:
    page.goto("https://www.spacex.com/")

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Go to the SpaceX Shop").click()

    page1 = page1_info.value
    products = page1.locator(h.search_items_link)
    products.nth(1).click()  # Click on the 2nd item

    page1.get_by_role("button", name="Add to cart").click()
    page1.get_by_role("button", name="CHECKOUT").click()

##################################################################################
    page1.wait_for_load_state("domcontentloaded") # waiting for full page load
    print(f"----Current URL: {page1.url}")
    print(f"----Page title: {page1.title()}")
    print(f"----Number of tabs: {len(page1.context.pages)}")
    #page1.screenshot(path="screenshot/checkout_debug.png", full_page=True)
##################################################################################

    city_fake = fake.random_element([
        "New York",
        "Buffalo",
        "Rochester",
        "Albany",
        "Syracuse",
        "Yonkers"
    ])

    # Generate fake customer data
    email = fake.safe_email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address()
    city = city_fake
    zip_code = fake.zipcode_in_state("NY")
    #zip_code = str(fake.random_int(min=10001, max=10040)) # Manhattan
    phone = fake.numerify("929-5##-####")

    # Fill checkout fields
    page1.get_by_role("textbox", name="Email").fill(email)
    page1.get_by_role("textbox", name="First name").fill(first_name)
    page1.get_by_role("textbox", name="Last name").fill(last_name)
    page1.get_by_role("combobox", name="Address").fill(address)
    page1.get_by_role("textbox", name="City").fill(city)
    page1.get_by_role("textbox", name="ZIP code").fill(zip_code)
    page1.get_by_role("textbox", name="Phone").fill(phone)
    page1.get_by_label("State").select_option("NY")

    # Take a screenshot of the completed checkout form
    page1.screenshot(path="screenshot/checkout_faker.png", full_page=True)
    print("----Checkout screenshot saved: OK")

    # Print generated customer data
    print(f"----Email: {email}")
    print(f"----First name: {first_name}")
    print(f"----Last name: {last_name}")
    print(f"----Address: {address}")
    print(f"----City: {city}")
    print(f"----ZIP code: {zip_code}")
    print(f"----Phone: {phone}")

    page1.get_by_role("button", name="Continue to shipping").click()
    print("----Continue to shipping clicked: Ok")
    expect(page1.locator("#checkout-main")).to_contain_text("Continue to payment")
    print("----'Continue to payment' Assert text: Ok")

# playwright codegen --channel=chrome --target=python-pytest -o test_playwright_codegen_faker_draft.py https://spacex.com/
# pytest --html="Reports/report_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').html" --self-contained-html --capture=tee-sys
# start Reports/report.html