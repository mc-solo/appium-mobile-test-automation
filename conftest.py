"""Pytest fixtures for the Appium tests.

The driver fixture only connects when a test actually uses it.
Importing this file, or running --collect-only, does not start Appium
or touch a device. All connection settings come from config.settings.
"""

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.settings import get_settings
from pages.home_page import HomePage
from pages.views_page import ViewsPage


@pytest.fixture(scope="function")
def driver():
    """Create an Appium driver session, quit it after the test."""
    settings = get_settings()
    options = UiAutomator2Options()
    options.load_capabilities(settings.capabilities())
    driver = webdriver.Remote(settings.server_url, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope="function")
def views_page(driver):
    return ViewsPage(driver)
