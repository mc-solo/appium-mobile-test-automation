"""Screenshot helper for the Appium tests.

Used by the failure hook in conftest.py: when a test fails, the
driver screenshot is saved under the configured screenshot folder.
The folder and the file name come from config, never hard-coded here.
"""

import re
from datetime import datetime
from pathlib import Path


def safe_name(name):
    """Make a test name safe to use as a file name."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)


def screenshot_path(name, screenshot_dir):
    """Full path for a screenshot of the given test name."""
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return Path(screenshot_dir) / f"{safe_name(name)}-{stamp}.png"


def save_screenshot(driver, name, screenshot_dir):
    """Save a screenshot and return its path as a string.

    Returns None if the driver cannot take one (for example the
    session is already dead). Never raises: a failed screenshot
    must not hide the test failure it is documenting.
    """
    try:
        path = screenshot_path(name, screenshot_dir)
        path.parent.mkdir(parents=True, exist_ok=True)
        driver.save_screenshot(str(path))
        return str(path)
    except Exception:
        return None
