import os
import pytest


from pages.login import SauceDemoLoginPage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
# DuckDuckGo search fixtures
# ------------------------------------------------------------

@pytest.fixture
def login_page(page: Page) -> SauceDemoLoginPage:
    return SauceDemoLoginPage(page)