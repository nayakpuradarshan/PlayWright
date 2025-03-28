import time
from playwright.sync_api import Page, Playwright, expect            # import Page class if you want auto-suggestion


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

# chromium headless mode, 1 single context
def test_playwrightShortCut(page:Page):
    page.goto   ("https://rahulshettyacademy.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")                       # You can found label tag on web element
    page.get_by_label("Password:").fill("learningddd")
    page.get_by_role("combobox").select_option("teach")                             # Just hover over the get_by_role method and
                                                                            # You'll see option available where you can use role method
    page.locator("#terms").check()                                                  # Using locator method you can use CSS and XPath
    page.get_by_role("link", name="terms and conditions").click()              # Using name, you can specify a name from all button on webpage
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefoxBrowser(playwright:Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    context = firefoxBrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningdddd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()















