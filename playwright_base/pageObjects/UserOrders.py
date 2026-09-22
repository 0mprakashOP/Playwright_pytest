import time

from playwright.sync_api import expect


class UserOrders:
    def __init__(self, page):
        self.page = page

    def verify_order_present(self, order_Id):
        product_locator = self.page.locator("tr").filter(has_text=order_Id)
        product_locator.get_by_role("button", name="View").click()
        expect(self.page.locator('//p[text()="Thank you for Shopping With Us"]')).to_be_visible()