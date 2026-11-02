
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://the-internet.herokuapp.com/login"


# TC_001: Login with valid credentials
def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()

        assert "/secure" in page.url
        assert "You logged into a secure area!" in page.locator("#flash").inner_text()

        print("TC_001 PASSED: Valid login successful")
        browser.close()


# TC_002: Login with invalid username
def test_invalid_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)

        page.locator("#username").fill("wronguser")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()

        assert "Your username is invalid!" in page.locator("#flash").inner_text()

        print("TC_002 PASSED: Invalid username rejected")
        browser.close()


# TC_003: Login with invalid password
def test_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("wrongpassword")
        page.locator("button[type='submit']").click()

        assert "Your password is invalid!" in page.locator("#flash").inner_text()

        print("TC_003 PASSED: Invalid password rejected")
        browser.close()

