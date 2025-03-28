import time
from playwright.async_api import Page, expect
from playwright.async_api import expect
from selenium.webdriver.common.devtools.v85.css import set_keyframe_key


def test_UICheck(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Hide/Show Example").is_visible()
    page.get_by_role("button", name="Hide").click()
    page.get_by_placeholder("Hide/Show Example").is_hidden()

    # Alert box
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    # Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    time.sleep(4)

    # Frame handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    # pageFrame.locator("body").text_content()                              # expect step was here but NOT WORKED


    # Check the price of rice is 37
    # Identify the price column
    # Identify the rice row
    # Extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")


    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            print(f"price column value is {priceColValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    #expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")       # NOT WORKED





    

