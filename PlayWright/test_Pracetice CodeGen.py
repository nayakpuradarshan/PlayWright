import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Alert").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("button", name="Hide").click()
    page.get_by_role("button", name="Show").click()
    page.locator("iframe[name=\"iframe-name\"]").content_frame.get_by_role("link", name="NEW All Access plan").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
