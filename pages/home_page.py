"""Home page of the ApiDemos app: the list of demo categories.

Locators live here because they describe this screen. The category
names tests *assert* on live in test-data/launch_data.json instead.
"""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    # ApiDemos home screen is a list; each row is identified by its text.
    ACCESSIBILITY = (AppiumBy.ACCESSIBILITY_ID, "Accessibility")
    APP = (AppiumBy.ACCESSIBILITY_ID, "App")
    CONTENT = (AppiumBy.ACCESSIBILITY_ID, "Content")
    GRAPHICS = (AppiumBy.ACCESSIBILITY_ID, "Graphics")
    MEDIA = (AppiumBy.ACCESSIBILITY_ID, "Media")
    OS = (AppiumBy.ACCESSIBILITY_ID, "OS")
    TEXT = (AppiumBy.ACCESSIBILITY_ID, "Text")
    VIEWS = (AppiumBy.ACCESSIBILITY_ID, "Views")

    # Items on the Text category screen, keyed by the name used in
    # test-data/navigation_data.json.
    TEXT_SCREEN_ITEMS = {
        "LogTextBox": (AppiumBy.ACCESSIBILITY_ID, "LogTextBox"),
        "Linkify": (AppiumBy.ACCESSIBILITY_ID, "Linkify"),
    }

    def get_categories(self):
        return [el.text for el in self.find_all((AppiumBy.XPATH, "//android.widget.TextView"))]

    def open_views(self):
        self.tap(self.VIEWS)

    def open_text(self):
        self.tap(self.TEXT)

    def open_accessibility(self):
        self.tap(self.ACCESSIBILITY)

    def open_app(self):
        self.tap(self.APP)

    def is_text_screen_visible(self, item_names):
        """True if any of the named Text-screen items is visible."""
        locators = [self.TEXT_SCREEN_ITEMS[name] for name in item_names]
        return self.is_any_visible(locators)
