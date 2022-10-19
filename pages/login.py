
from playwright.sync_api import Page


class SauceDemoLoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.search_button = page.locator('#login-button')
        self.login_error_message = page.locator("xpath=//h3[contains(@data-test, 'error')]")
        page.locator('#login-button')

    def load(self) -> None:
        self.page.goto(self.URL)

    def fillLoginForm(self, login: str, password: str) -> None:
        self.username_input.fill(login)
        self.password_input.fill(password)
        self.search_button.click()

