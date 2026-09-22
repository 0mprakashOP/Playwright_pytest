from urllib import response

from playwright.sync_api import Playwright
from selenium.webdriver.common import api_request_context

orders_payload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
#token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTdmNDYxOTIxMDU0YmE0NjVkMzRlNWEiLCJ1c2VyRW1haWwiOiJvbXRlc3RAZ21haWwuY29tIiwidXNlck1vYmlsZSI6ODk4OTg5ODk4OSwidXNlclJvbGUiOiJjdXN0b21lciIsImlhdCI6MTc4NjgwNzYwNywiZXhwIjoxODE4MzY1MjA3fQ.7oFnf4ra2Av4nzUXlcb7LvHx91nxe1-G_g7EklgGl3Y'
class APIutils:

    def get_token(self, playwright: Playwright, user_email: str, user_password: str):
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com/api/")
        response = api_request_context.post(url = "ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        print(response.json())
        return response.json().get("token")


    def create_order(self, playwright:Playwright, user_email: str, user_password: str):
        token = self.get_token(playwright, user_email, user_password)
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com/api/")
        response = api_request_context.post(url="ecom/order/create-order",
                                            data=orders_payload,
                                            headers={
                                                "Authorization":token
                                            })
        print(response.json())
        return response.json().get("orders")[0]



