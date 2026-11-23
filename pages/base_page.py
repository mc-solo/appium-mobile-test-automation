"""Base page with the common actions every page object uses.

Timeouts and the screenshot folder come from config.settings, so no
wait or path is hard-coded here.
"""

from pathlib import Path

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import get_settings


class BasePage:
    def __init__(self, driver, timeout=None):
        self.driver = driver
        settings = get_settings()
        self.timeout = timeout if timeout is not None else settings.timeout
        self.screenshot_dir = Path(settings.screenshot_dir)

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def tap(self, locator):
        self.find(locator).click()

    def tap_by_accessibility_id(self, accessibility_id):
        self.tap((AppiumBy.ACCESSIBILITY_ID, accessibility_id))

    def tap_by_text(self, text):
        self.tap(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
        )

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def is_any_visible(self, locators):
        """True if at least one of the given locators is visible."""
        return any(self.is_visible(locator) for locator in locators)

    def take_screenshot(self, name):
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(str(self.screenshot_dir / f"{name}.png"))

    # ---- gestures (UiAutomator2 "mobile:" commands) ----
    # Appium-Python-Client 4 has no TouchAction; gestures go through
    # the driver's mobile: commands, which UiAutomator2 understands.
    # Directions and ratios come from test-data/gestures_data.json.

    def _window_size(self):
        size = self.driver.get_window_size()
        return size["width"], size["height"]

    def _point(self, x_ratio, y_ratio):
        width, height = self._window_size()
        return int(width * x_ratio), int(height * y_ratio)

    def swipe(self, direction, percent=0.75):
        """Swipe across most of the screen in the given direction."""
        width, height = self._window_size()
        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 100,
                "top": 100,
                "width": width - 200,
                "height": height - 200,
                "direction": direction,
                "percent": percent,
            },
        )

    def swipe_up(self, percent=0.75):
        self.swipe("up", percent)

    def swipe_down(self, percent=0.75):
        self.swipe("down", percent)

    def long_press(self, locator, duration_ms=1000):
        """Long-press the element found by locator."""
        element = self.find(locator)
        self.driver.execute_script(
            "mobile: longClickGesture",
            {"elementId": element.id, "duration": duration_ms},
        )

    def tap_at(self, x_ratio, y_ratio):
        """Tap a point given as ratios of the screen width/height."""
        x, y = self._point(x_ratio, y_ratio)
        self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})

    def scroll_to_text(self, text, max_swipes=5):
        """Swipe up until an element with the given text is visible."""
        locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{text}")',
        )
        for _ in range(max_swipes):
            if self.is_visible(locator):
                return True
            self.swipe_up()
        return self.is_visible(locator)
