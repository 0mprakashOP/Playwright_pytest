from playwright_base.pageObjects.UserOrders import UserOrders


class UserDashboard:
    def __init__(self, page):
        self.page = page

    def navigate_to_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        user_orders = UserOrders(self.page)
        return user_orders