import time
from logging import exception

from playwright.sync_api import Page, expect
import helpers as h

def test_case_009_shop_spacex_Negative (page: Page):
    print("\n")
    print("test_case_009_shop_spacex_Negative")

# 1. Open https://shop.spacex.com/
    page.goto(h.SHOP)
    # Checking page
    h.open_checked(page, h.SHOP, h.shop_spacex_logo, h.shop_spacex_title)
# 2. Find Search field in header
    expect(page.locator(h.search_btn_link)).to_be_enabled()
    expect(page.locator(h.search_btn_link)).to_be_visible()
    #expect(page.locator(h.search_btn_link)).to_be_clickable()
    search_b = page.locator(h.search_btn_link)
    search_b.click()

    expect(page.locator(h.search_input_link)).to_be_enabled()
    expect(page.locator(h.search_input_link)).to_be_visible()
    search_i = search_b = page.locator(h.search_input_link)
# 3. Type special symbols "!@#$%^&()" into search field
    search_i.fill(h.NEGATIVE_SEARCH)
# 4. Press Enter
    search_i.press("Enter")  # press enter
# 5. Check result
    result_title = page.locator(h.search_res_link)
    h.check_element(page, h.search_res_link)
    print("----Text: ",result_title.inner_text())

    h.check_title(page, h.search_res_title)

    h.search_items_count(page) # counting items

def test_case_010_shop_spacex_Negative (page: Page):
    print("\n")
    print("test_case_010_shop_spacex_Negative")
# 1. Open https://shop.spacex.com/
    page.goto(h.SHOP)
    # Checking page
    h.open_checked(page, h.SHOP, h.shop_spacex_logo, h.shop_spacex_title)
# 2. Click on the 3rd item in catalog and open its PDP (Product Detail Page)
    products = page.locator(h.search_items_link)
    products.nth(2).click() # Click on the 3rd item
    print("Item num #3 clicked: Ok")
# 3. Find Quantity: field
    quantity = page.locator(h.quantity_link)
# 4. Clear field and type letters "qwerty"
    quantity.clear()
    print("Quantity field was cleared: Ok")
    quantity.fill("qwerty")
    print("Quantity field was filled 'qwerty': Ok")
# 5. Click Add to cart button
    add_to_cart_btn = page.locator(h.add_to_cart_link)
    add_to_cart_btn.click()
    print("Click Add to cart button: Ok")
# 6. Check result
    cart_quantity = page.locator(h.cart_quantity_link)
    expect(cart_quantity).to_have_value("1")
    print("Cart quantity has value '1' checked: Ok")


