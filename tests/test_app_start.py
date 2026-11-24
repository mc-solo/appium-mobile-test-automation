"""App start tests: install/start checks and a deep link into a view.

The app under test is ApiDemos. The driver fixture in conftest.py
already starts the app from the package/activity in config/settings,
so the start tests verify that session: the app is installed, the
expected package is in front, and the home list is reached. A
restart test terminates the app and activates it again.

The deep link test opens a link into the Views screen with the
UiAutomator2 "mobile: deepLink" command (see
BasePage.open_deep_link) and asserts the Views list is showing
(Buttons is its first item). The link itself lives in
test-data/app_start_data.json, and the package comes from the same
file, so nothing is hard-coded here.

Note: ApiDemos publishes no documented deep-link scheme, so the URL
in test-data/app_start_data.json could not be verified against the
app's manifest here (no device/emulator was available). Before
trusting a deep-link run, check the installed ApiDemos build handles
that URL and update the test-data file if it uses a different one;
the test is written to fail at the Views assertion if the link does
not land on that screen, rather than pass silently.

On failure, the hook in conftest.py saves a screenshot to
screenshots/ (via utils/screenshot.py), as for the other suites.
"""

import pytest

from tests.data_loader import load_json

DATA = load_json("app_start_data")

pytestmark = pytest.mark.app_start


def test_app_is_installed(driver):
    assert driver.is_app_installed(DATA["expected_package"])


def test_app_starts_and_reaches_home(driver, home_page):
    assert driver.current_package == DATA["expected_package"]
    categories = home_page.get_categories()
    assert len(categories) > 0
    assert DATA["required_category"] in categories


def test_app_restarts_after_terminate(driver, home_page):
    driver.terminate_app(DATA["expected_package"])
    driver.activate_app(DATA["expected_package"])
    assert driver.current_package == DATA["expected_package"]
    categories = home_page.get_categories()
    assert DATA["required_category"] in categories


def test_deep_link_opens_views(home_page, views_page):
    home_page.open_deep_link(
        DATA["deep_link_url"], DATA["expected_package"]
    )
    assert views_page.is_visible(views_page.BUTTONS)


def test_deep_link_then_back_returns_home(home_page, views_page):
    home_page.open_deep_link(
        DATA["deep_link_url"], DATA["expected_package"]
    )
    assert views_page.is_visible(views_page.BUTTONS)
    views_page.go_back()
    assert home_page.is_visible(home_page.VIEWS)
