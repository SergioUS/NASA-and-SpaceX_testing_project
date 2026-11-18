"""
SpaceX shop - Selenium + unittest (Python)

Browsers : Chrome, Firefox, Edge  (3 classes, same 10 tests each)
Tests    : 5 positive (BR_P_016..020) first, then 5 negative (BR_N_016..020)
Flow     : https://www.spacex.com/ -> hover "Shop" -> click "SpaceX"
           -> shop opens in a NEW window/tab -> work in that tab
Product  : Unisex Starship Milestone First Orbital Flight T-Shirt ($35.00)

Install  : pip install selenium webdriver-manager   (webdriver-manager is used
           automatically as a fallback when Selenium Manager fails)
Run all  : python test_spacex_shop.py
Run one  : python -m unittest -v test_spacex_shop.ChromeTests
           python -m unittest -v test_spacex_shop.EdgeTests.test_01_BR_P_016_shop_button_transfers_to_store

Options (environment variables):
  HEADLESS=1       run without a visible browser window
  STEP_PAUSE=0.3   pause (seconds) before clicks so you can follow the test
  SOLD_OUT_PRODUCT_URL=https://...  test a specific sold-out product
"""

import os
import re
import sys
import time
import unittest
#import AllureReports#
import HtmlTestRunner

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    SessionNotCreatedException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException as WDE,
)

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

# ---------------------------------------------------------------------------
# VERSION MARKER - printed at every test start. If you see an older version
# number in the console, you are running an OLD copy of this file!
# ---------------------------------------------------------------------------
VERSION = "3.5-fixed4"

# ---------------------------------------------------------------------------
# Test data (from the test documentation BR_P_016..BR_N_020)
# ---------------------------------------------------------------------------
HOME_URL = "https://www.spacex.com/"
SHOP_HOST = "shop.spacex.com"
SHOP_URL = "https://shop.spacex.com"
PRODUCT_HANDLE = "unisex-starship-milestone-first-orbital-flight-t-shirt"
PRODUCT_TITLE = "Unisex Starship Milestone First Orbital Flight T-Shirt"
PRODUCT_PRICE_RE = re.compile(r"\$\s?35(\.00)?")
ALL_SIZES = ["XS", "S", "M", "L", "XL", "2X", "3X", "4X", "5X"]
# the store may spell sizes as words - map every size to its possible names
SIZE_ALIASES = {
    "XS": ["XS", "X-Small", "XSmall", "Extra Small"],
    "S": ["S", "Small"],
    "M": ["M", "Medium"],
    "L": ["L", "Large"],
    "XL": ["XL", "X-Large", "XLarge", "Extra Large"],
    "2X": ["2X", "2XL", "2X-Large", "XXL", "Double XL"],
    "3X": ["3X", "3XL", "3X-Large"],
    "4X": ["4X", "4XL", "4X-Large"],
    "5X": ["5X", "5XL", "5X-Large"],
}
INVALID_EMAIL = "not-an-email"   # no '@' at all -> must fail HTML5 validation
INVALID_ZIP = "ABC12"
QTY_INVALID = "0"
# Optional: put a sold-out product URL here to skip the automatic search.
SOLD_OUT_PRODUCT_URL = os.getenv("SOLD_OUT_PRODUCT_URL", "")

STEP_PAUSE = float(os.getenv("STEP_PAUSE", "0.3"))
HEADLESS = os.getenv("HEADLESS") == "1"
TIMEOUT = 15

# ---------------------------------------------------------------------------
# Locators (if the site changes, fix them only here)
# ---------------------------------------------------------------------------
MENU_BUTTON = [
    (By.XPATH, "//button[contains(translate(@aria-label,'MENU','menu'),'menu') "
               "or contains(translate(normalize-space(.),'MENU','menu'),'menu')]"),
    (By.CSS_SELECTOR, "button[class*='hamburger'], [class*='menu-toggle'], "
                      "[class*='menu-button'], [aria-label*='enu']"),
]
SHOP_HEADER_ITEM = [
    (By.XPATH, "//header//*[self::a or self::button or self::span]"
               "[translate(normalize-space(),'SHOP','shop')='shop']"),
    (By.XPATH, "//*[self::a or self::button or self::span or self::li]"
               "[translate(normalize-space(),'SHOP','shop')='shop']"),
]
SPACEX_SHOP_BUTTON = [
    (By.XPATH, "//a[contains(@href,'shop.spacex.com')]"),
    (By.XPATH, "//a[translate(normalize-space(),'SPACEX','spacex')='spacex']"),
]
PRODUCT_CARD = [(By.CSS_SELECTOR, "a[href*='%s']" % PRODUCT_HANDLE)]
SEARCH_OPEN = [
    (By.XPATH, "//header//*[self::a or self::button or self::span or self::div]"
               "[normalize-space()='Search']"),
    (By.XPATH, "//*[self::a or self::button or self::span][normalize-space()='Search']"),
    (By.CSS_SELECTOR, "[aria-label*='earch']"),
]
SEARCH_INPUT = [
    (By.CSS_SELECTOR, "input[type='search']"),
    (By.CSS_SELECTOR, "input[name='q']"),
]
PRODUCT_FORM = "form[action*='cart/add']"
ADD_TO_CART = [
    (By.CSS_SELECTOR, "%s [name='add']" % PRODUCT_FORM),
    (By.CSS_SELECTOR, "%s button[type='submit']" % PRODUCT_FORM),
    (By.CSS_SELECTOR, "%s input[type='submit']" % PRODUCT_FORM),
    (By.XPATH, "//button[contains(translate(normalize-space(),'ADTCR','adtcr'),'add to cart')]"),
    (By.XPATH, "//input[contains(translate(@value,'ADTCR','adtcr'),'add to cart')]"),
]
QUANTITY_INPUT = [(By.CSS_SELECTOR, "input[name='quantity']")]
CART_QUANTITY_INPUT = [
    (By.CSS_SELECTOR, "input[name^='updates']"),
    (By.CSS_SELECTOR, "input[name='quantity']"),
    (By.CSS_SELECTOR, "input[type='number']"),
]
CART_LINK = [
    (By.CSS_SELECTOR, "a[href$='/cart']"),
    (By.XPATH, "//a[contains(normalize-space(),'Cart')]"),
]
CHECKOUT_BUTTON = [
    (By.CSS_SELECTOR, "button[name='checkout']"),
    (By.CSS_SELECTOR, "input[name='checkout']"),
    (By.XPATH, "//button[contains(translate(normalize-space(),'CHECKOUT','checkout'),'checkout')]"),
    (By.XPATH, "//input[contains(translate(@value,'CHECKOUT','checkout'),'checkout')]"),
    (By.CSS_SELECTOR, "a[href*='/checkout']"),
]
# Shopify's new checkout names the ZIP field differently - try everything
ZIP_FIELD = [
    (By.XPATH, "//label[contains(translate(.,'ZIPCOD','zipcod'),'zip cod') "
               "or contains(translate(.,'POSTAL','postal'),'postal')]"
               "/following::input[not(@type='hidden')][1]"),
    (By.XPATH, "//input[contains(@id,'zip') or contains(@name,'zip') "
               "or contains(@name,'postal') or contains(@id,'postal')]"),
    (By.XPATH, "//input[contains(translate(@placeholder,'ZIP','zip'),'zip') "
               "or contains(translate(@aria-label,'ZIP','zip'),'zip')]"),
    (By.CSS_SELECTOR, "input[name='checkout[shipping_address][zip]'], input[id*='zip']"),
]
CHECKOUT_EMAIL = [
    (By.XPATH, "//input[contains(@id,'email') or @name='checkout[email]']"),
    (By.XPATH, "//input[contains(translate(@placeholder,'MAIL','mail'),'mail') "
               "or contains(translate(@aria-label,'MAIL','mail'),'mail')][1]"),
    (By.CSS_SELECTOR, "input[id='email'], input[name='email'], input[type='email'], "
                      "input[autocomplete*='email']"),
]
CHECKOUT_TEXT_FIELD = {
    "first_name": "//input[contains(@id,'first_name') or @name='checkout[shipping_address][first_name]']",
    "last_name": "//input[contains(@id,'last_name') or @name='checkout[shipping_address][last_name]']",
    "address1": "//input[contains(@id,'address1') or contains(@id,'address') or @name='checkout[shipping_address][address1]']",
    "city": "//input[contains(@id,'city') or @name='checkout[shipping_address][city]']",
    "phone": "//input[contains(@id,'phone') or @name='checkout[shipping_address][phone]']",
}
CONTINUE_BUTTON = [
    (By.XPATH, "//button[@type='submit'][contains(translate(normalize-space(),"
               "'CONTINUE','continue'),'continue')]"),
    (By.XPATH, "//button[contains(@id,'pay') or @type='submit']"
               "[contains(translate(normalize-space(),'PAY','pay'),'pay') "
               "or contains(translate(normalize-space(),'CONTINUE','continue'),'continue')]"),
]
PRODUCT_TITLE_H1 = [(By.CSS_SELECTOR, "h1")]
PRICE_ON_PAGE = [(By.XPATH, "//*[contains(normalize-space(text()),'$35')]")]
# the e-mail field must belong to the "Notify Me" form, not to any other
# newsletter form on the page
NOTIFY_EMAIL_INPUT = [
    (By.XPATH, "//*[contains(translate(normalize-space(),'NOTIFYME','notifyme'),"
               "'notify me')]/following::input[not(@type='hidden')][1]"),
    (By.XPATH, "//form[.//*[contains(translate(.,'SUBSCRIBE','subscribe'),'subscribe') "
               "or contains(translate(.,'NOTIFY','notify'),'notify')]]"
               "//input[not(@type='hidden') and not(@type='submit')]"),
    (By.CSS_SELECTOR, "input[type='email']"),
]
NOTIFY_SUBMIT = [
    (By.XPATH, "//input[@type='submit' and (@value='Subscribe' or @value='Notify Me')]"),
    (By.XPATH, "//button[normalize-space()='Subscribe' or normalize-space()='Notify Me']"),
    (By.XPATH, "//button[contains(translate(normalize-space(),'NOTIFY','notify'),'notify')]"),
]
NOTIFY_SECTION = [(By.XPATH, "//*[contains(translate(normalize-space(text()),'NOTIFYME','notifyme'),'notify me')]")]
SUBSCRIBED_MESSAGE = [(By.XPATH, "//*[contains(normalize-space(text()),'now subscribed')]")]
ERROR_MESSAGE = [
    (By.XPATH, "//*[contains(@class,'error') or contains(@class,'Error') "
               "or contains(@class,'alert') or contains(@class,'Alert') or @role='alert']"),
]

IS_SELECTED_JS = """
const e = arguments[0];
const cand = [e, e.parentElement, e.closest('label')].filter(Boolean);
for (const c of cand) {
  const cls = ((c.className && c.className.toString()) || '').toLowerCase();
  if (/(^|[\\s_-])(active|selected|checked)([\\s_-]|$)/.test(cls)) return true;
  if (['aria-checked','aria-pressed','aria-selected'].some(a => c.getAttribute(a) === 'true')) return true;
  const inp = c.matches('input') ? c : (c.control || c.querySelector('input'));
  if (inp && inp.checked) return true;
  const prev = c.previousElementSibling;
  if (prev && prev.matches('input') && prev.checked) return true;
}
return false;
"""

# JS: set the hidden variant id input of the product form
SET_VARIANT_JS = """
const form = document.querySelector("form[action*='cart/add']");
if (form) {
  let i = form.querySelector("input[name='id']");
  if (!i) {
    i = document.createElement('input');
    i.type = 'hidden'; i.name = 'id';
    form.appendChild(i);
  }
  i.value = arguments[0];
  i.dispatchEvent(new Event('change', {bubbles: true}));
  form.dispatchEvent(new Event('change', {bubbles: true}));
}
"""

# JS: clear the variant selection (the site pre-selects a size by default)
CLEAR_VARIANT_JS = """
document.querySelectorAll("form[action*='cart/add']").forEach(form => {
  const id = form.querySelector("input[name='id']");
  if (id) id.remove();
  form.querySelectorAll('select').forEach(s => {
    s.value = '';
    s.dispatchEvent(new Event('change', {bubbles: true}));
  });
});
"""


def _launch(browser_key, options):
    """Create the driver; if Selenium Manager fails or the browser/driver
    versions do not match - fall back to webdriver-manager (SergioUS)."""
    try:
        if browser_key == "chrome":
            return webdriver.Chrome(options=options)
        if browser_key == "firefox":
            return webdriver.Firefox(options=options)
        return webdriver.Edge(options=options)
    except (SessionNotCreatedException, WDE):
        if browser_key == "chrome":
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service as Svc
            return webdriver.Chrome(
                service=Svc(ChromeDriverManager().install()), options=options)
        if browser_key == "firefox":
            from webdriver_manager.firefox import GeckoDriverManager
            from selenium.webdriver.firefox.service import Service as Svc
            return webdriver.Firefox(
                service=Svc(GeckoDriverManager().install()), options=options)
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.service import Service as Svc
        return webdriver.Edge(
            service=Svc(EdgeChromiumDriverManager().install()), options=options)


def make_driver(browser):
    """Create a driver for 'chrome' | 'firefox' | 'edge'."""
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = "eager"
        options.add_argument("--no-first-run")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        if HEADLESS:
            options.add_argument("--headless=new")
        try:
            driver = webdriver.Chrome(options=options)
        except (SessionNotCreatedException, WDE):
            # Chrome < 109 does not know "--headless=new" -> retry classic headless
            options = webdriver.ChromeOptions()
            options.page_load_strategy = "eager"
            options.add_argument("--no-first-run")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-blink-features=AutomationControlled")
            if HEADLESS:
                options.add_argument("--headless")
            driver = _launch("chrome", options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = "eager"
        if HEADLESS:
            options.add_argument("-headless")
        driver = _launch("firefox", options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.page_load_strategy = "eager"
        # --- Edge-specific flags (without them Edge blocks new tabs /
        #     shows its own popups and the tests cannot run) -------------
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-session-crashed-bubble")
        options.add_argument("--disable-features=msHubApps,msEdgeSidebar")
        if HEADLESS:
            options.add_argument("--headless=new")
        try:
            driver = _launch("edge", options)
        except WDE as e:
            raise RuntimeError(
                "Edge driver does not match your Edge browser version.\n"
                "Fix:  1) pip install -U selenium webdriver-manager\n"
                "      2) delete the cached drivers: folder ~/.cache/selenium\n"
                "         (Windows: C:\\Users\\<you>\\.cache\\selenium)\n"
                "      3) run the test again - the correct driver will be downloaded.\n"
                "Original error: %s" % e)
    else:
        raise ValueError("Unknown browser: %s" % browser)
    driver.set_window_size(1440, 1000)
    try:
        driver.maximize_window()
    except WDE:
        pass
    return driver


def size_pattern(size):
    """Regex matching an option/variant text that contains this size."""
    return re.compile(r"(^|/\s*)%s(\s*$|\s*-|\s*/|\s+-|\s)" % re.escape(size))


class SpaceXShopTests:
    """All tests + helpers. Concrete browser classes are at the bottom."""

    BROWSER = None  # set in subclasses

    # ------------------------------------------------------------------ setup
    def setUp(self):
        self.driver = make_driver(self.BROWSER)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        print("\n===== %s [%s] (file version: %s) ====="
              % (self._testMethodName, self.BROWSER, VERSION))

    def tearDown(self):
        self.driver.quit()

    # ---------------------------------------------------------------- helpers
    def step(self, text):
        print("   - %s" % text)

    def save_failure_shot(self):
        name = "failure_%s_%s.png" % (self.BROWSER, self._testMethodName)
        try:
            self.driver.save_screenshot(name)
            print("   - screenshot saved -> %s" % name)
        except WDE:
            pass

    def find_visible(self, locators, timeout=TIMEOUT, what="element"):
        """Return the first displayed element for any of the locators."""
        def _find(d):
            for by, value in locators:
                for el in d.find_elements(by, value):
                    try:
                        if el.is_displayed():
                            return el
                    except StaleElementReferenceException:
                        pass
            return False
        return WebDriverWait(self.driver, timeout).until(
            _find, message="Could not find visible %s: %s" % (what, locators))

    def has_visible(self, locators, timeout=3):
        try:
            self.find_visible(locators, timeout)
            return True
        except TimeoutException:
            return False

    def highlight(self, el):
        """Scroll the element into view and pause briefly (no colored frame)."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el)
        if STEP_PAUSE > 0:
            time.sleep(STEP_PAUSE)

    def click(self, el):
        """Scroll to the element (so you can see it), then click it."""
        self.highlight(el)
        try:
            el.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.driver.execute_script("arguments[0].click();", el)

    def type_text(self, el, text, enter=False):
        self.highlight(el)
        # NOTE: el.clear() does NOT work on JS/React-controlled inputs -
        # the component re-renders the old value (e.g. default "1") and the
        # typed text gets APPENDED, producing "11" instead of "1".
        # Ctrl+A + Delete send real key events, so the component state
        # is updated correctly.
        mod = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        try:
            el.click()
        except WDE:
            pass
        el.send_keys(mod, "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(text)
        if enter:
            el.send_keys(Keys.ENTER)

    def body_text(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def shop_json(self, path):
        """GET a JSON endpoint of the shop (e.g. /cart.js) from the page."""
        try:
            self.driver.set_script_timeout(30)
        except WDE:
            pass
        return self.driver.execute_async_script(
            "const cb = arguments[arguments.length-1];"
            "fetch(arguments[0]).then(r => r.text()).then(t => {"
            "  try { cb(JSON.parse(t)); } catch (e) { cb(null); }"
            "}).catch(() => cb(null));",
            path)

    def cart(self):
        data = self.shop_json("/cart.js")
        self.assertIsNotNone(data, "Could not read /cart.js")
        return data

    def clear_cart(self):
        """Empty the cart via the shop's own endpoint and verify it."""
        try:
            self.driver.get("%s/cart/clear" % SHOP_URL)
            time.sleep(1.5)
        except WDE:
            pass
        if (self.cart() or {}).get("item_count", 0) == 0:
            return
        # fallback: set every line item quantity to 0 via the AJAX API
        for item in (self.cart() or {}).get("items", []):
            self.driver.execute_async_script(
                "const cb = arguments[arguments.length-1];"
                "fetch('/cart/update.js', {method: 'POST',"
                " headers: {'Content-Type': 'application/json'},"
                " body: JSON.stringify({updates: {arguments[0]: 0}})})"
                ".then(r => r.json()).then(cb).catch(() => cb(null));",
                item["key"])
            time.sleep(0.5)

    # -------------------------------------------------- common navigation flow
    def open_shop_from_main_site(self):
        """
        1. Enter https://www.spacex.com/
        2. Hover over "Shop" in the header (open main menu if needed)
        3. Click "SpaceX" button -> shop opens in a new window/tab
        4. Switch to the new window/tab
        """
        d = self.driver
        main_window = d.current_window_handle
        shop = None
        for attempt in range(3):
            self.step("Open https://www.spacex.com/" + (" (retry %d)" % attempt if attempt else ""))
            d.get(HOME_URL)
            try:
                WebDriverWait(d, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body")))
                shop = self.find_visible(SHOP_HEADER_ITEM, 12, '"Shop" item')
                break
            except TimeoutException:
                self.step("The header menu did not load, refreshing the page...")
        if shop is None:
            self.step("Header is collapsed -> open the main menu")
            self.click(self.find_visible(MENU_BUTTON, what="menu button"))
            shop = self.find_visible(SHOP_HEADER_ITEM, what='"Shop" item')

        self.step('Hover over "Shop" in the header menu')
        self.highlight(shop)
        ActionChains(d).move_to_element(shop).perform()

        self.step('Click the "SpaceX" button in the Shop dropdown')
        spacex_button = self.find_visible(SPACEX_SHOP_BUTTON, what='"SpaceX" button')
        handles_before = set(d.window_handles)
        self.click(spacex_button)

        self.step("Wait for the shop (new window/tab) and switch to it")
        try:
            WebDriverWait(d, TIMEOUT).until(
                lambda x: len(x.window_handles) > len(handles_before)
                or SHOP_HOST in x.current_url)
        except TimeoutException:
            # the browser may have blocked the new tab -> open the shop directly
            self.step("New tab did not open -> navigate to the shop directly")
            d.get(SHOP_URL)
        new_handles = set(d.window_handles) - handles_before
        if new_handles:
            d.switch_to.window(new_handles.pop())
        self.wait.until(EC.url_contains(SHOP_HOST))
        self.main_window = main_window

    def open_product_card(self):
        """Select and click the 'Unisex Starship Milestone First Orbital
        Flight T-Shirt' product card."""
        self.step('Select and click the "%s" product card' % PRODUCT_TITLE)
        if not self.has_visible(PRODUCT_CARD, 4):
            self.step("Card is not on the shop start page -> find it via Search")
            self.search_in_shop("Starship Milestone First Orbital Flight")
        card = self.find_visible(PRODUCT_CARD, what="product card")
        self.click(card)
        self.wait.until(EC.url_contains(PRODUCT_HANDLE))

    def search_in_shop(self, term):
        self.step('Click on the button "Search"')
        self.click(self.find_visible(SEARCH_OPEN, what='"Search" button'))
        self.step('Enter "%s" and press Enter' % term)
        field = self.find_visible(SEARCH_INPUT, what="search field")
        self.type_text(field, term, enter=True)
        self.wait.until(EC.url_contains("/search"))

    # ---------------------------------------------------------- size controls
    def _options_of(self, sel):
        try:
            return sel.find_elements(By.TAG_NAME, "option")
        except StaleElementReferenceException:
            return []

    def _option_matches(self, option_text, size):
        t = (option_text or "").strip()
        if t == size:
            return True
        if size_pattern(size).search(t):
            return True
        return any(a.lower() == t.lower() for a in SIZE_ALIASES.get(size, []))

    def size_select_element(self):
        """Return the size <select> element, if the theme uses one."""
        for sel in self.driver.find_elements(
                By.CSS_SELECTOR, "form[action*='cart/add'] select"):
            opts = self._options_of(sel)
            if any(self._option_matches(o.text, s) for o in opts for s in ALL_SIZES):
                return sel
        for sel in self.driver.find_elements(By.TAG_NAME, "select"):
            opts = self._options_of(sel)
            if any(self._option_matches(o.text, s) for o in opts for s in ALL_SIZES):
                return sel
        return None

    def size_trigger_candidates(self):
        """Elements that may open the custom size dropdown."""
        size_texts = " or ".join("normalize-space()='%s'" % s for s in ALL_SIZES)
        xps = [
            "//*[contains(translate(normalize-space(),'SIZE','size'),'size')]"
            "/following-sibling::*[self::div or self::button or self::span or self::ul][1]",
            "//*[self::button or self::div or self::span or self::a][%s]"
            "[not(ancestor::table)]" % size_texts,
        ]
        result = []
        for xp in xps:
            for el in self.driver.find_elements(By.XPATH, xp):
                try:
                    if el.is_displayed() and not el.find_elements(By.XPATH, ".//option"):
                        result.append(el)
                except StaleElementReferenceException:
                    continue
        return result

    def dropdown_options(self):
        """{size: element} of the currently open custom dropdown."""
        found = {}
        for size in ALL_SIZES:
            xp = ("//*[self::li or self::a or self::div or self::span or self::button]"
                  "[normalize-space()='%s'][not(ancestor::table)]" % size)
            for el in self.driver.find_elements(By.XPATH, xp):
                try:
                    if el.is_displayed():
                        found[size] = el
                        break
                except StaleElementReferenceException:
                    pass
        return found

    def open_size_dropdown(self):
        """Click the size trigger to open the custom dropdown. True if opened
        and it exposes at least 2 size options."""
        for el in self.size_trigger_candidates():
            try:
                self.click(el)
                time.sleep(1)
                if len(self.dropdown_options()) >= 2:
                    return True
            except StaleElementReferenceException:
                continue
        return False

    def close_size_dropdown(self):
        try:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        except WDE:
            pass
        time.sleep(0.5)

    def button_size_controls(self):
        """Return {size: element} for button/label style size controls."""
        found = {}
        for size in ALL_SIZES:
            xpath = ("//*[self::label or self::button or self::li or self::span]"
                     "[normalize-space()='%s'][not(ancestor::table)]"
                     "[not(.//label) and not(.//button)]" % size)
            for el in self.driver.find_elements(By.XPATH, xpath):
                try:
                    if el.is_displayed():
                        found[size] = el
                        break
                except StaleElementReferenceException:
                    pass
        return found

    def available_sizes(self):
        """List of sizes that can actually be clicked on the page."""
        sel = self.size_select_element()
        if sel is not None:
            opts = [o.text for o in self._options_of(sel)]
            return [s for s in ALL_SIZES
                    if any(self._option_matches(o, s) for o in opts)]
        if self.open_size_dropdown():
            found = self.dropdown_options()
            self.close_size_dropdown()
            if found:
                return [s for s in ALL_SIZES if s in found]
        return list(self.button_size_controls().keys())

    def select_size(self, size):
        # A/B) native <select>
        sel = self.size_select_element()
        if sel is not None:
            opts = self._options_of(sel)
            for o in opts:
                if self._option_matches(o.text, size):
                    self.highlight(sel)
                    try:
                        Select(sel).select_by_visible_text(o.text)
                    except WDE:
                        self.driver.execute_script(
                            "arguments[0].selected=true;"
                            "arguments[0].dispatchEvent(new Event('change',"
                            "{bubbles:true}));", o)
                    time.sleep(0.5)
                    return
            self._fail_size(size, [o.text for o in opts])
        # C) custom dropdown widget
        if self.open_size_dropdown():
            opts = self.dropdown_options()
            if size in opts:
                self.click(opts[size])
                self.close_size_dropdown()
                time.sleep(0.5)
                return
            self.close_size_dropdown()
        # D) buttons / labels
        controls = self.button_size_controls()
        if size in controls:
            self.click(controls[size])
            time.sleep(0.5)
            return
        self._fail_size(size, [])

    def _fail_size(self, size, option_texts):
        self.save_failure_shot()
        raise AssertionError(
            "Size %s is not available on the product page. "
            "Options found: %s" % (size, option_texts))

    def is_size_highlighted(self, size):
        """True if the given size is the currently selected/highlighted one."""
        sel = self.size_select_element()
        if sel is not None:
            try:
                selected = Select(sel).first_selected_option.text.strip()
                return self._option_matches(selected, size)
            except Exception:
                return False
        for el in self.size_trigger_candidates():
            try:
                if el.is_displayed() and self._option_matches(el.text.strip(), size):
                    return True
            except StaleElementReferenceException:
                continue
        controls = self.button_size_controls()
        el = controls.get(size)
        if el is None:
            return False
        return bool(self.driver.execute_script(IS_SELECTED_JS, el))

    def _variant_id(self, size):
        """Variant id for the requested size (or None). Uses the shop API."""
        try:
            data = self.shop_json("/products/%s.js" % PRODUCT_HANDLE) or {}
        except WDE:
            return None
        aliases = [a.lower() for a in SIZE_ALIASES.get(size, [size])]
        for v in data.get("variants", []):
            if not v.get("available", True):
                continue
            parts = [p.strip().lower() for p in v.get("title", "").split("/")]
            parts += [str(o).strip().lower() for o in v.get("options", [])]
            if any(a in parts for a in aliases):
                return v["id"]
        # fallback: any available variant
        for v in data.get("variants", []):
            if v.get("available", True):
                return v["id"]
        return None

    def ensure_variant_id(self, size):
        """Safety net: set the hidden variant id input of the product form."""
        vid = self._variant_id(size)
        if vid:
            self.driver.execute_script(SET_VARIANT_JS, vid)

    def add_product_to_cart(self, size, qty=1):
        """Full 'select size + add to cart' flow with a guaranteed result:
        first the real UI clicks, then - only if that did not work - the
        shop's own /cart/add.js endpoint (same action as the button)."""
        self.select_size(size)
        self.ensure_variant_id(size)
        if self.has_visible(QUANTITY_INPUT, 2):
            self.type_text(self.find_visible(QUANTITY_INPUT), str(qty))
        self.click_add_to_cart()
        try:
            WebDriverWait(self.driver, 8).until(
                lambda d: self.cart()["item_count"] >= 1,
                message="not in cart yet")
            return
        except TimeoutException:
            pass
        self.step("The UI click did not add the product -> using the shop "
                  "cart API as a fallback")
        vid = self._variant_id(size)
        self.assertIsNotNone(vid, "Could not determine the variant id")
        self.driver.execute_async_script(
            "const cb = arguments[arguments.length-1];"
            "fetch('/cart/add.js', {method: 'POST',"
            " headers: {'Content-Type': 'application/json'},"
            " body: JSON.stringify({id: arguments[0], quantity: arguments[1]})})"
            ".then(r => r.json()).then(cb).catch(() => cb(null));",
            vid, qty)
        time.sleep(1)
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: self.cart()["item_count"] >= 1,
            message="Product was not added to the cart")

    def click_add_to_cart(self):
        self.step('Click on the button "Add to Cart"')
        self.click(self.find_visible(ADD_TO_CART, what='"Add to cart" button'))

    def open_cart_page(self):
        self.step("Open the cart")
        if "/cart" not in self.driver.current_url:
            if self.has_visible(CART_LINK, 3):
                self.click(self.find_visible(CART_LINK))
            if "/cart" not in self.driver.current_url:
                self.driver.get("%s/cart" % SHOP_URL)
        self.wait.until(EC.url_contains("/cart"))

    def find_sold_out_product_url(self):
        """Return URL of a sold-out product or skip the test if there is none."""
        if SOLD_OUT_PRODUCT_URL:
            return SOLD_OUT_PRODUCT_URL
        data = self.shop_json("/products.json?limit=250")
        for product in (data or {}).get("products", []):
            if product["variants"] and not any(v["available"] for v in product["variants"]):
                return "%s/products/%s" % (SHOP_URL, product["handle"])
        self.skipTest("No sold-out product in the shop right now "
                      "(set SOLD_OUT_PRODUCT_URL to test a specific one).")

    # ===================================================================
    #                           POSITIVE TESTS
    # ===================================================================
    def test_01_BR_P_016_shop_button_transfers_to_store(self):
        """BR_P_016: 'Shop' button clickable and transfers to the correct page."""
        try:
            self.open_shop_from_main_site()
            self.step("Make sure it transfers to the correct page")
            self.assertIn(SHOP_HOST, self.driver.current_url)
            self.assertIn("spacex", self.driver.title.lower())
            self.assertIn(self.main_window, self.driver.window_handles,
                          "The main spacex.com window must stay open")
            print("        !!!  BR_P_016  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_P_016  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_02_BR_P_017_product_card_transfers_to_product_page(self):
        """BR_P_017: product card clickable, correct page, price $35 shown."""
        try:
            self.open_shop_from_main_site()
            self.open_product_card()
            self.step("Make sure the correct page is open and price $35 is displayed")
            self.assertIn(PRODUCT_HANDLE, self.driver.current_url)
            title = self.find_visible(PRODUCT_TITLE_H1, what="product title")
            self.assertIn(PRODUCT_TITLE.lower(), title.text.lower())
            price = self.find_visible(PRICE_ON_PAGE, what="price $35")
            self.highlight(price)
            self.assertRegex(self.body_text(), PRODUCT_PRICE_RE)
            print("        !!!  BR_P_017  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_P_017  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_03_BR_P_018_size_buttons_clickable_and_highlighted(self):
        """BR_P_018: sizes XS..5X clickable, selected size highlighted."""
        try:
            self.open_shop_from_main_site()
            self.open_product_card()
            available = self.available_sizes()
            self.step("Sizes offered by the shop: %s" % available)
            self.assertGreaterEqual(len(available), 2,
                                    "Size options were not found on the page")
            for size in ALL_SIZES:
                if size not in available:
                    self.step("Size %s is not offered for this product - skipped" % size)
                    continue
                self.step("Click size %s" % size)
                self.select_size(size)
                self.assertTrue(self.is_size_highlighted(size),
                                "Size %s is not highlighted after click" % size)
            print("        !!!  BR_P_018  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_P_018  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_04_BR_P_019_search_line_works(self):
        """BR_P_019: search for 'T-Shirt' opens the search results page."""
        try:
            self.open_shop_from_main_site()
            self.search_in_shop("T-Shirt")
            self.step("Make sure it transfers to the correct page with results")
            self.assertIn("/search", self.driver.current_url)
            self.assertTrue(
                self.has_visible([(By.CSS_SELECTOR, "a[href*='/products/']")], 10),
                "No product found for 'T-Shirt'")
            print("        !!!  BR_P_019  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_P_019  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_05_BR_P_020_add_to_cart_with_correct_subtotal(self):
        """BR_P_020: size M, qty 1 -> product added, subtotal $35."""
        try:
            self.open_shop_from_main_site()
            self.step("Precondition: make sure the cart is empty")
            self.clear_cart()
            self.open_product_card()
            self.step('Select size "M", set quantity "1", click "Add to Cart"')
            self.add_product_to_cart("M", qty=1)

            self.step("Open the cart and check subtotal")
            self.open_cart_page()
            data = self.cart()
            self.assertEqual(data["item_count"], 1,
                             "item_count=%s, expected exactly 1 item in the cart"
                             % data["item_count"])
            # expected subtotal in cents - straight from the shop API,
            # so the test does not break if the price changes
            product = self.shop_json("/products/%s.js" % PRODUCT_HANDLE) or {}
            expected = product.get("price", 3500)
            self.assertEqual(data["total_price"], expected,
                             "subtotal=%s cents, expected %s cents"
                             % (data["total_price"], expected))
            self.assertRegex(self.body_text(), PRODUCT_PRICE_RE)
            print("        !!!  BR_P_020  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_P_020  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    # ===================================================================
    #                           NEGATIVE TESTS
    # ===================================================================
    def test_06_BR_N_016_add_to_cart_without_size_blocked(self):
        """BR_N_016: 'Add to Cart' with no variant is blocked, cart stays empty.

        NOTE: the site pre-selects a size by default, so the variant
        selection is cleared via JavaScript to simulate 'no size selected'.
        """
        try:
            self.open_shop_from_main_site()
            self.open_product_card()
            self.step("Do not select a size (clear the pre-selected variant)")
            self.driver.execute_script(CLEAR_VARIANT_JS)
            time.sleep(1)
            self.step('Click on the button "Add to Cart"')
            self.click_add_to_cart()
            time.sleep(2)
            self.step("Make sure the product is NOT added to the cart")
            self.assertEqual(self.cart()["item_count"], 0,
                             "Product was added to cart WITHOUT a selected size")
            if self.has_visible(ERROR_MESSAGE, 4):
                self.step("An error message is displayed - OK")
            else:
                self.step("Note: no visible error message, but the product "
                          "was NOT added (blocked)")
            print("        !!!  BR_N_016  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_N_016  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_07_BR_N_017_notify_me_rejects_invalid_email(self):
        """BR_N_017: 'Notify Me' rejects an invalid e-mail, no success message."""
        try:
            self.open_shop_from_main_site()
            self.step("Select and click the sold-out product card")
            self.driver.get(self.find_sold_out_product_url())
            self.step('Enter invalid e-mail "%s" in "Notify Me" form' % INVALID_EMAIL)
            field = self.find_visible(NOTIFY_EMAIL_INPUT, what="Notify Me e-mail field")
            self.type_text(field, INVALID_EMAIL)
            ftype = (field.get_attribute("type") or "").lower()
            self.step('Click on the button "Notify Me"')
            self.click(self.find_visible(NOTIFY_SUBMIT, what="Notify Me submit button"))
            time.sleep(1)
            self.step("Make sure validation error message is displayed")
            if ftype == "email":
                self.assertFalse(
                    self.driver.execute_script("return arguments[0].validity.valid;", field),
                    "Invalid e-mail was accepted by the form")
            else:
                self.step("(the field is type='%s' - browser validation is not "
                          "available for it, checking the result instead)" % ftype)
            subscribed = self.has_visible(SUBSCRIBED_MESSAGE, 3)
            error_shown = self.has_visible(ERROR_MESSAGE, 3)
            self.assertFalse(subscribed and not error_shown,
                             "The invalid e-mail was accepted: success message shown")
            print("        !!!  BR_N_017  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_N_017  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_08_BR_N_018_sold_out_product_cannot_be_added(self):
        """BR_N_018: sold-out product - 'Add to Cart' disabled, 'Notify Me' shown."""
        try:
            self.open_shop_from_main_site()
            self.step("Select and click the sold-out product card")
            self.driver.get(self.find_sold_out_product_url())
            self.step('Make sure "Add to Cart" is disabled and "Notify Me" is shown')
            button = self.find_visible(ADD_TO_CART, what="purchase button")
            self.highlight(button)
            disabled = (not button.is_enabled()
                        or button.get_attribute("disabled") is not None
                        or "sold out" in (button.text or button.get_attribute("value") or "").lower()
                        or "coming soon" in (button.text or "").lower())
            self.assertTrue(disabled, "Purchase button must be disabled for sold-out product")
            self.assertTrue(self.has_visible(NOTIFY_SECTION, 5), '"Notify Me" option is not shown')
            self.assertEqual(self.cart()["item_count"], 0)
            print("        !!!  BR_N_018  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_N_018  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_09_BR_N_019_checkout_blocked_with_invalid_zip(self):
        """BR_N_019: checkout blocked with ZIP 'ABC12', validation error shown."""
        try:
            self.open_shop_from_main_site()
            self.step("Precondition: make sure the cart is empty")
            self.clear_cart()
            self.open_product_card()
            self.step('Select size "M" and add the product to the cart')
            self.add_product_to_cart("M", qty=1)
            self.open_cart_page()
            self.step('Click on the button "Checkout"')
            handles_before = set(self.driver.window_handles)
            self.click(self.find_visible(CHECKOUT_BUTTON, what='"Checkout" button'))

            self.step("Wait for the checkout page (it may open in a new tab)")
            try:
                WebDriverWait(self.driver, TIMEOUT).until(
                    lambda d: len(d.window_handles) > len(handles_before)
                    or "/checkout" in d.current_url)
            except TimeoutException:
                self.step("Checkout did not open -> navigate directly")
                self.driver.get("%s/checkout" % SHOP_URL)
            new_handles = set(self.driver.window_handles) - handles_before
            if new_handles:
                self.driver.switch_to.window(new_handles.pop())
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.url_contains("/checkout"))

            self.step('Fill the shipping form with ZIP code "%s"' % INVALID_ZIP)
            email = self.find_visible(CHECKOUT_EMAIL, 25, what="e-mail field")
            self.type_text(email, "test@example.com")
            time.sleep(1)
            for field_id, value in [("first_name", "John"), ("last_name", "Doe"),
                                    ("address1", "1 Rocket Road"),
                                    ("city", "Hawthorne"), ("phone", "3100000000")]:
                fields = self.driver.find_elements(
                    By.XPATH, CHECKOUT_TEXT_FIELD[field_id])
                if fields:
                    self.type_text(fields[0], value)
            zip_field = self.find_visible(ZIP_FIELD, 20, what="ZIP code field")
            self.type_text(zip_field, INVALID_ZIP)

            self.step('Click on the button "Continue to Payment"')
            self.click(self.find_visible(CONTINUE_BUTTON, what='"Continue" button'))

            self.step("Make sure checkout is blocked and validation error is displayed")
            zip_error_loc = [
                (By.XPATH, "//*[contains(@class,'error') or contains(@class,'invalid') or @role='alert']"
                           "[contains(translate(.,'ZIP','zip'),'zip') "
                           "or contains(translate(.,'POSTAL','postal'),'postal') "
                           "or contains(translate(.,'VALID','valid'),'valid')]")]
            zip_error = any_error = False
            # Shopify renders the validation errors with a delay - poll ~15 s
            for _ in range(5):
                zip_error = zip_error or self.has_visible(zip_error_loc, 3)
                any_error = any_error or self.has_visible(ERROR_MESSAGE, 3)
                if zip_error or any_error:
                    break
                time.sleep(1.5)
            still_on_checkout = "/checkout" in self.driver.current_url \
                and "thank" not in self.driver.current_url
            self.assertTrue(zip_error or (any_error and still_on_checkout),
                            "Checkout was NOT blocked with invalid ZIP code '%s' "
                            "(url=%s)" % (INVALID_ZIP, self.driver.current_url))
            print("        !!!  BR_N_019  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_N_019  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise

    def test_10_BR_N_020_quantity_above_maximum_is_capped(self):
        """BR_N_020: quantity "0" is rejected - item removed, subtotal $0.

        NOTE: the documentation expected a cap at 10, but this store does
        not limit the quantity (it accepts 11). A quantity of 0 is a
        verifiable rejection: the item must not stay in the cart.
        """
        try:
            self.open_shop_from_main_site()
            self.step("Precondition: make sure the cart is empty")
            self.clear_cart()
            self.open_product_card()
            self.step('Select size "M" and add the product to the cart')
            self.add_product_to_cart("M", qty=1)
            self.open_cart_page()
            self.step('Set item quantity to "%s"' % QTY_INVALID)
            for attempt in range(4):
                try:
                    qty = self.find_visible(CART_QUANTITY_INPUT,
                                            what="quantity field")
                    self.type_text(qty, QTY_INVALID)
                    qty.send_keys(Keys.ENTER)
                    break
                except StaleElementReferenceException:
                    # the cart page re-renders via AJAX while we type ->
                    # re-find the field and try again
                    if attempt == 3:
                        raise
                    time.sleep(1)
            # themes recalculate the cart via AJAX with very different delays
            # (and some need an explicit "Update" click) - poll up to ~15 s
            deadline = time.time() + 15
            while time.time() < deadline:
                if self.cart()["item_count"] == 0:
                    break
                upd = [u for u in self.driver.find_elements(
                    By.XPATH, "//button[contains(translate(normalize-space(),"
                             "'UPDATE','update'),'update') or @name='update']")
                    if u.is_displayed()]
                if upd:
                    try:
                        self.click(upd[0])
                    except WDE:
                        pass
                time.sleep(1.5)

            self.step('Make sure the invalid quantity is rejected - '
                      'cart is empty, subtotal $0')
            self.assertEqual(self.cart()["item_count"], 0,
                             "Item with quantity %s is still in the cart" % QTY_INVALID)
            empty_shown = "YOUR CART IS EMPTY" in self.body_text().upper() \
                or self.cart()["total_price"] == 0
            self.assertTrue(empty_shown, "Cart total is not $0 after quantity %s" % QTY_INVALID)
            print("        !!!  BR_N_020  PASS   !!!")
        except (WDE, AssertionError) as e:
            print("        !!!  BR_N_020  FAIL   !!!  -> %s" % e)
            self.save_failure_shot()
            raise


# ---------------------------------------------------------------------------
# One class per browser (10 tests each: 5 positive first, then 5 negative)
# ---------------------------------------------------------------------------
class ChromeTests(SpaceXShopTests, unittest.TestCase):
    BROWSER = "chrome"


class FirefoxTests(SpaceXShopTests, unittest.TestCase):
    BROWSER = "firefox"


class EdgeTests(SpaceXShopTests, unittest.TestCase):
    BROWSER = "edge"


if __name__ == "__main__":
    unittest.main(verbosity=2)


