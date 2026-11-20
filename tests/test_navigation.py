"""Navigation tests: move from home into Views and back.

Expected Text-screen items come from test-data/navigation_data.json.
"""

import pytest

from tests.data_loader import load_json

DATA = load_json("navigation_data")


@pytest.mark.navigation
def test_open_views_from_home(home_page, views_page):
    home_page.open_views()
    assert views_page.is_visible(views_page.BUTTONS)


@pytest.mark.navigation
def test_open_views_then_go_back(home_page, views_page):
    home_page.open_views()
    assert views_page.is_visible(views_page.CONTROLS)
    views_page.go_back()
    assert home_page.is_visible(home_page.VIEWS)


@pytest.mark.navigation
def test_open_text_category_from_home(home_page):
    home_page.open_text()
    assert home_page.is_text_screen_visible(DATA["text_screen_items"])
