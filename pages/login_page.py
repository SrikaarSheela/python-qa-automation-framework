class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.message = page.locator("#flash")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_message(self):
        return self.message.inner_text()
