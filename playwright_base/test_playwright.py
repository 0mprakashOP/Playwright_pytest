import time

from playwright.sync_api import Page, expect


def signin_user(page):
    page.goto("https://www.rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("radio", name="Admin").click()

    page.get_by_role("button", name="Sign In").click()


def test_addtocart(page:Page):
    signin_user(page)
    iphone_Locator = page.locator("app-card").filter(has_text="iphone X")
    iphone_Locator.get_by_role("button", name="Add").click()
    Blackberry_Locator = page.locator("app-card").filter(has_text="Blackberry")
    Blackberry_Locator.get_by_role("button", name="Add").click()
    #class="nav-item active"
    page.locator("li.nav-item.active", has_text="Checkout").click()
    checkout_count = page.locator("div.media")
    assert checkout_count.count() == 2
    time.sleep(5)


def test_new_page_test(page:Page):
    page.goto("https://www.rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as new_page:
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page = new_page.value
        txt = child_page.locator("p.red").text_content()
        email_expected = txt.split("at")[1].strip(" ").split(" ")[0]
        assert email_expected == "mentor@rahulshettyacademy.com"


def test_UIChecks(page:Page):

    # verify hidden item to be hided
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # verufy alert dialog box handled

    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Alert").click()
    time.sleep(5)

    #handle frames

    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access Plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    # handling table data
    colVal = 0
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            colVal = index
            break
    row_rice = page.locator("tr").filter(has_text="Rice")
    price = row_rice.locator("td").nth(colVal).text_content()
    assert int(price) == 37





