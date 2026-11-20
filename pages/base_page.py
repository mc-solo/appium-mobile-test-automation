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
