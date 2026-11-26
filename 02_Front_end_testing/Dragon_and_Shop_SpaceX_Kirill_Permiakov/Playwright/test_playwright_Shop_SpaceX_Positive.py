from playwright.sync_api import Page, expect
import helpers as h

def test_case_009_shop_spacex_Positive (page: Page):

# 1. Open homepage https://www.spacex.com/
    page.goto(h.SPACEX)
    # Check web page is right
    h.open_checked(page, h.SPACEX, h.homepage_logo, h.home_title)
# 2. Hover over SHOP item in header
    shop = page.locator(h.shop_link)
    expect(shop).to_be_visible()
    print("----Shop is visible: OK")
    shop.hover()
# 3. Click on SpaceX
    shop_spacex = page.locator(h.shop_spacex_link)
    expect(shop_spacex).to_be_visible()
    print("----Shop_spacex is visible: OK")

    with page.expect_popup() as popup_info: #
        shop_spacex.click()
    shop_page = popup_info.value
    shop_page.wait_for_load_state("domcontentloaded")

# 4. Check web page is right
    h.open_checked(shop_page, h.SHOP, h.shop_spacex_logo, h.shop_spacex_title)

def test_case_010_shop_spacex_Positive (page: Page):

# 1. Open https://shop.spacex.com/
    page.goto(h.SHOP)
    # Check web page is right
    h.open_checked(page, h.SHOP, h.shop_spacex_logo, h.shop_spacex_title)
# 2. Select any in-stock item and open its PDP (Product Display Page)
    # Starship Milestone First Orbital Flight Mission Patch (2nd item)
    # Quantity: 1
    item2 = page.locator(h.shop_item2_link)
    expect(item2).to_be_visible()
    print("----item2 is visible: OK")
    item2.click()
    print("----item2 was clicked: OK")
# 3. Select size / quantity if required
    expect(page.locator(h.quantity_link)).to_be_visible()
    quantity = page.locator(h.quantity_link)
    print("----Quantity field is visible and save to quantity variable: OK")

    expect(page.locator(h.inc_quantity)).to_be_visible()
    ink_qua = page.locator(h.inc_quantity)
    print("----inc_quantity button is visible and save to ink_qua variable: OK")

    expect(page.locator(h.dec_quantity)).to_be_visible()
    dec_qua = page.locator(h.dec_quantity)
    print("----dec_quantity button is visible and save to dec_qua variable: OK")

    for _ in range(9): ink_qua.click()
    expect(quantity).to_have_value("10")
    print("----inc_quantity was clicked 9 times and = ", quantity.input_value())

    for _ in range(5): dec_qua.click()
    expect(quantity).to_have_value("5")
    print("----dec_quantity was clicked 5 times and = ", quantity.input_value())

    quantity.fill(h.ITEM_QUANTITY)
    expect(quantity).to_have_value(h.ITEM_QUANTITY)
    print("----QUANTITY was fill: " + h.ITEM_QUANTITY + " OK")

    quantity_val = int(quantity.input_value()) # save QUANTITY value
    print("----QUANTITY was saved = " + h.ITEM_QUANTITY + " OK")

# 4. Click Add to Cart button
    expect(page.locator(h.add_to_cart_link)).to_be_visible()
    add_cart_button = page.locator(h.add_to_cart_link)
    add_cart_button.click()
    print("----add_to_cart_link was clicked: OK")

# 5. Check the result
    h.open_checked(page, h.CART, h.cart_header, h.cart_title)

    expect(page.locator(h.cart_quantity_link)).to_be_visible()
    quantity_cart = page.locator(h.cart_quantity_link)

    quantity_cart_val = int(quantity_cart.input_value())

    h.check_quantity(page, quantity_val, quantity_cart_val)
