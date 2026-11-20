"""Smoke tests: the ApiDemos app launches and shows its home list.

Expected values come from test-data/launch_data.json.
"""

import pytest

from tests.data_loader import load_json

DATA = load_json("launch_data")


@pytest.mark.smoke
def test_app_launches(driver):
    assert driver is not None
    # The app is running if a session exists and the package is in front.
    assert driver.current_package == DATA["expected_package"]


@pytest.mark.smoke
def test_home_list_is_visible(home_page):
    categories = home_page.get_categories()
    assert len(categories) > 0
    assert DATA["required_category"] in categories


@pytest.mark.smoke
def test_home_categories_include_expected_items(home_page):
    categories = home_page.get_categories()
    for expected in DATA["expected_categories"]:
        assert expected in categories, f"{expected} missing from home list"
