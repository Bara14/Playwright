from playwright.sync_api import Page


class SauceDemoInventoryPage:
    URL = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_header = page.locator(".title")
        self.basket_icon = page.locator("#shopping_cart_container")
        self.hamburger_menu = page.locator("#react-burger-menu-btn")
        self.hamburger_menu_all_items = page.locator("#inventory_sidebar_link")
        self.item = page.locator("xpath=//div[contains(@class,'inventory_item_name') and contains(text(),'Sauce Labs Bolt T-Shirt')]")

    def load(self) -> None:
        self.page.goto(self.URL)

