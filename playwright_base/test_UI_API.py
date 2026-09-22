import json

import pytest
from playwright.sync_api import Playwright, expect

from playwright_base.pageObjects.login import UserLogin
from playwright_base.utils.API_testing import APIutils

with open('playwright_base/data/credentials.json') as config_file:
    data = json.load(config_file)
    print(data)
    user_credentials_list = data['user_credentials']

@pytest.mark.parametrize("user_credentials",user_credentials_list)
def test_web_ui_api(playwright: Playwright, user_credentials, browserInstance):
    userEmail = user_credentials["user_email"]
    user_Password = user_credentials["user_password"]

    # get order ID by creating order
    api_obj = APIutils()
    order_Id = api_obj.create_order(playwright, userEmail, user_Password)
    print(order_Id)

    # login user by POM
    login_user = UserLogin(browserInstance)
    user_dashboard = login_user.navigate(userEmail, user_Password)

    #user orders check
    user_orders = user_dashboard.navigate_to_orders()
    user_orders.verify_order_present(order_Id)
