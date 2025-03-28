from http.client import responses

from playwright.sync_api import Playwright
ordersPayLoad = {}

class APIutils:

    def createOrder(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("/api/ecom/order/create-order",
                                        data=ordersPayLoad,
                                        headers={"authorization": token,
                                                 "content-Type": "application/json"
                                                 })
        print(response.json())