import pytest
from pandas.core.computation.expr import PARSERS
from pytest_bdd import given, when, then, parsers, scenarios

from playwright_base.pageObjects.Dashboard import UserDashboard
from playwright_base.pageObjects.login import UserLogin
from playwright_base.utils.API_testing import APIutils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    api_obj = APIutils()
    order_Id = api_obj.create_order(playwright, username, password)
    shared_data['order_Id'] = order_Id

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal_page(browserInstance, username, password, shared_data):
    login_user = UserLogin(browserInstance)
    user_dashboard = login_user.navigate(username, password)
    shared_data['user_dashboard'] = user_dashboard

@when('navigate to orders page Select the OrderId')
def navigate_to_orders_page(shared_data):
    user_dashboard = shared_data['user_dashboard']
    user_orders = user_dashboard.navigate_to_orders()
    shared_data['user_orders'] = user_orders

@then('Order message is successfully displayed')
def order_message( shared_data):
    user_orders = shared_data['user_orders']
    order_Id = shared_data['order_Id']
    user_orders.verify_order_present(order_Id)
