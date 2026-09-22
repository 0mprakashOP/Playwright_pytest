import json
import time
import pytest
from playwright.sync_api import Playwright, expect
from playwright_base.pageObjects.login import UserLogin
from playwright_base.utils.API_testing import APIutils

empty_order_json = {
    "data": [],
    "message": "No Orders"
}

with open('playwright_base/data/credentials.json') as config_file:
    data = json.load(config_file)
    print(data)
    user_credentials_list = data['user_credentials']


def intercept_response(route):
    print("Intercepted:", route.request.url)

    route.fulfill(
        status=200,
        content_type="application/json",
        json=empty_order_json
    )

@pytest.mark.parametrize("user_credentials",user_credentials_list)
def test_inturuppt_response(playwright: Playwright, user_credentials, browserInstance):
    # import fet token finction to get token of user
    userEmail = user_credentials["user_email"]
    user_Password = user_credentials["user_password"]

    login_user = UserLogin(browserInstance)
    user_dashboard = login_user.navigate(userEmail, user_Password)


    user_dashboard.page.route("https://www.rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    user_dashboard.page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)
    expect(user_dashboard.page.get_by_text("You have No Orders to show at this time")).to_be_visible()






