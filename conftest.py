"""Pytest fixtures for the Appium tests.

The driver fixture only connects when a test actually uses it.
Importing this file, or running --collect-only, does not start Appium
or touch a device.
"""

import pytest
from appium import webdriver

from config.capabilities import get_android_capabilities, get_appium_server_url


@pytest.fixture(scope="function")
def driver():
    """Create an Appium driver session, quit it after the test."""
    caps = get_android_capabilities()
    # Build the session with UiAutomator2 options from the capabilities dict.
    from appium.options.android import UiAutomator2Options

    options = UiAutomator2Options()
    options.load_capabilities(caps)
    driver = webdriver.Remote(get_appium_server_url(), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    from pages.home_page import HomePage

    return HomePage(driver)


@pytest.fixture(scope="function")
def views_page(driver):
    from pages.views_page import ViewsPage

    return ViewsPage(driver)
