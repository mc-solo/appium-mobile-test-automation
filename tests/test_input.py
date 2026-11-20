"""Input tests: type text into a Views > TextFields field.

Text to type comes from test-data/input_data.json; the field locator
lives on the ViewsPage page object.
"""

import pytest

from pages.views_page import ViewsPage
from tests.data_loader import load_json

DATA = load_json("input_data")


@pytest.mark.input
def test_type_text_in_text_field(driver, home_page):
    home_page.open_views()
    views = ViewsPage(driver)
    views.open_text_fields()
    views.type_in_text_field(DATA["type_text"])
    assert views.get_text_field_value() == DATA["type_text"]


@pytest.mark.input
def test_clear_and_retype_text_field(driver, home_page):
    home_page.open_views()
    views = ViewsPage(driver)
    views.open_text_fields()
    views.type_in_text_field(DATA["first_text"])
    views.type_in_text_field(DATA["second_text"])
    assert views.get_text_field_value() == DATA["second_text"]
