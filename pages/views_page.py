"""Views page of ApiDemos, reached from the home screen."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ViewsPage(BasePage):
    BUTTONS = (AppiumBy.ACCESSIBILITY_ID, "Buttons")
    CONTROLS = (AppiumBy.ACCESSIBILITY_ID, "Controls")
    TEXT_FIELDS = (AppiumBy.ACCESSIBILITY_ID, "TextFields")
    LISTS = (AppiumBy.ACCESSIBILITY_ID, "Lists")
    # First text field on the Views > TextFields screen.
    TEXT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[1]")

    def open_buttons(self):
        self.tap(self.BUTTONS)

    def open_controls(self):
        self.tap(self.CONTROLS)

    def open_text_fields(self):
        self.tap(self.TEXT_FIELDS)

    def open_lists(self):
        self.tap(self.LISTS)

    def go_back(self):
        self.driver.back()

    def type_in_text_field(self, text):
        self.enter_text(self.TEXT_FIELD, text)

    def long_press_buttons(self, duration_ms=1000):
        self.long_press(self.BUTTONS, duration_ms)

    def scroll_to_lists(self, max_swipes=5):
        return self.scroll_to_text("Lists", max_swipes)

    def get_text_field_value(self):
        return self.get_text(self.TEXT_FIELD)
