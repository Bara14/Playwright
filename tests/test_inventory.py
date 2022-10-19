
from playwright.sync_api import expect


def login_as_standard_user(login_page) -> None:
    login_page.load()
    login_page.fillLoginForm("standard_user", "secret_sauce")


def test_hamburger_menu_content(login_page,inventory_page) -> None:
    login_page.load()
    login_page.fillLoginForm("standard_user", "secret_sauce")
    inventory_page.hamburger_menu.click()
    expect(inventory_page.hamburger_menu_all_items).to_have_text("All Items")
