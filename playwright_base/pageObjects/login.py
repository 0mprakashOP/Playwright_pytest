import time
from playwright_base.pageObjects.Dashboard import UserDashboard


class UserLogin:
    def __init__(self, page):
        self.page = page
    def navigate(self, userEmail, user_Password):
        self.page.goto("https://www.rahulshettyacademy.com/client")
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.locator("#userPassword").fill(user_Password)
        self.page.get_by_role("button", name="login").click()
        time.sleep(5)
        user_dashboard = UserDashboard(self.page)
        return user_dashboard


