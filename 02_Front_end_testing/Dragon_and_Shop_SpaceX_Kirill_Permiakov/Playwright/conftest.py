
import pytest

# @pytest.fixture(params=["chrome", "firefox"], ids=["Google Chrome", "Firefox"])
@pytest.fixture(params=["chrome"], ids=["Google Chrome"])
def page(request, playwright):
    browser_type = request.param

    if browser_type == "chrome":
        browser = playwright.chromium.launch(
            channel="chrome", headless=True
        )
    else:
        browser = playwright.firefox.launch(headless=True)

    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    yield page

    context.close()
    browser.close()
