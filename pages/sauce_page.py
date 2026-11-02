from playwright.sync_api import expect

class SaucePage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

    def add_backpack(self):
        self.page.locator(
            "#add-to-cart-sauce-labs-backpack"
        ).click()

    def remove_backpack(self):
        self.page.locator(
            "#remove-sauce-labs-backpack"
        ).click()

    def open_cart(self):
        self.page.locator(
            ".shopping_cart_link"
        ).click()

    def checkout(self, first_name, last_name, postal_code):
        self.page.locator("#checkout").click()
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)
        self.page.locator("#continue").click()
        self.page.locator("#finish").click()
