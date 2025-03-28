import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/")
    page.get_by_label("Phone number, username or").dblclick()
    page.get_by_label("Phone number, username or").fill("darshan.patel_7696")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Log in", exact=True).click()
    page.get_by_role("button", name="Not now").click()
    page.get_by_label("Direct messaging – 1 new").click()
    page.get_by_role("button", name="Not Now").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Explore Explore").click()
    page.get_by_role("link", name="Instagram", exact=True).click()
    page.get_by_role("link", name="darshan.patel_7696", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
