import pytest

from pages.login import SauceDemoLoginPage
from playwright.sync_api import expect, Page


def test_SauceDemo_login(
        login_page) -> None:
    # Given the DuckDuckGo home page is displayed
    login_page.load()

    # When the user searches for a phrase
    login_page.loginForm("aaa", "ddd")
    expect(login_page.login_error_message).to_have_text('Epic sadface: Username and password do not match any user in this service')
