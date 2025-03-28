
from playwright.sync_api import Playwright


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/auth/login")

    # create order ---> order ID


    # Login
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmial.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()

    # Order history page --> order is present

