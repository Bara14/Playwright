import os
import pytest


from pages.login import SauceDemoLoginPage
from pages.inventory import SauceDemoInventoryPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
#  search fixtures
# ------------------------------------------------------------

@pytest.fixture
def login_page(page: Page) -> SauceDemoLoginPage:
    return SauceDemoLoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> SauceDemoInventoryPage:
    return SauceDemoInventoryPage(page)

