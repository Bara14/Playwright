import pytest

from playwright.sync_api import expect, Page


def test_SauceDemo_incorrect_login(
        login_page) -> None:
    login_page.load()
    login_page.fillLoginForm("aaa", "ddd")
    expect(login_page.login_error_message).to_have_text('Epic sadface: Username and password do not match any user in this service')

def test_SauceDemo_correct_login(
        login_page, inventory_page) -> None:
    login_page.load()
    login_page.fillLoginForm("standard_user", "secret_sauce")
    expect(inventory_page.product_header).to_have_text('Products')
