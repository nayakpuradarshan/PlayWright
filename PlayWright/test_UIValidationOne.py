import time
from playwright.async_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("checkout").click()


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        # Step 1
        # Step 2
        page.locator(".blinkingText").click()        # New Page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        words = text.split("at")                                    # split will device string into two parts
        email = words[1].strip().split(" ")[0]                      # strip() method will remove space from beginning and end
        print(email)
        assert email == "mentor@rahulshettyacademy.com"










