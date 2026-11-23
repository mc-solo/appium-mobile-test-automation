"""Gesture tests: swipe, long press, scroll and tap.

Gestures go through the UiAutomator2 "mobile:" commands in
pages/base_page.py (Appium-Python-Client 4 has no TouchAction).
Directions, durations and targets come from
test-data/gestures_data.json, loaded by tests/data_loader.py.
"""

import pytest

from tests.data_loader import load_json

DATA = load_json("gestures_data")

pytestmark = pytest.mark.gestures


def test_swipe_down_then_up_on_views(home_page, views_page):
    home_page.open_views()
    assert views_page.is_visible(views_page.BUTTONS)
    views_page.swipe(DATA["swipe"]["directionDown"], DATA["swipe"]["percent"])
    views_page.swipe(DATA["swipe"]["directionUp"], DATA["swipe"]["percent"])
    assert views_page.is_visible(views_page.BUTTONS)


def test_long_press_on_buttons(home_page, views_page):
    home_page.open_views()
    views_page.long_press_buttons(DATA["longPress"]["durationMs"])
    assert views_page.is_visible(views_page.BUTTONS)


def test_scroll_to_lists(home_page, views_page):
    home_page.open_views()
    assert views_page.scroll_to_lists(DATA["scroll"]["maxSwipes"])
    assert views_page.is_visible(views_page.LISTS)


def test_tap_at_screen_centre(home_page, views_page):
    home_page.open_views()
    views_page.tap_at(DATA["tap"]["xRatio"], DATA["tap"]["yRatio"])
    # The tap may open an item or do nothing, depending on what is
    # under the centre point; either way the Views screen or the
    # screen it opened must still be showing something expected.
    assert views_page.is_any_visible([views_page.BUTTONS, home_page.VIEWS])
