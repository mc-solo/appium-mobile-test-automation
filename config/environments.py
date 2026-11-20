"""Named environment presets for the Appium tests.

A preset is only a set of *defaults*. Every value can still be
overridden with an environment variable (see config/settings.py),
so the same code runs on a different emulator or a real device
without editing any file.

Pick a preset with APPIUM_ENV. Default: "emulator".
"""

ENVIRONMENTS = {
    "emulator": {
        "platform_name": "Android",
        "device_name": "Android Emulator",
        "platform_version": "14",
        "automation_name": "UiAutomator2",
        "app_package": "io.appium.android.apis",
        "app_activity": ".ApiDemos",
        "no_reset": False,
        "new_command_timeout": 60,
        "timeout": 10,
        "server_url": "http://127.0.0.1:4723",
        "screenshot_dir": "screenshots",
    },
    "real_device": {
        "platform_name": "Android",
        # Generic placeholder: set APPIUM_DEVICE_NAME to the real
        # device name shown by `adb devices`, and
        # APPIUM_PLATFORM_VERSION to the device's Android version.
        "device_name": "Android Device",
        "platform_version": "14",
        "automation_name": "UiAutomator2",
        "app_package": "io.appium.android.apis",
        "app_activity": ".ApiDemos",
        "no_reset": False,
        "new_command_timeout": 60,
        "timeout": 10,
        "server_url": "http://127.0.0.1:4723",
        "screenshot_dir": "screenshots",
    },
}

DEFAULT_ENVIRONMENT = "emulator"


def get_environment_preset(name):
    """Return the preset dict for ``name`` (unknown names fall back)."""
    if name not in ENVIRONMENTS:
        known = ", ".join(sorted(ENVIRONMENTS))
        raise ValueError(
            f"Unknown APPIUM_ENV={name!r}. Known environments: {known}."
        )
    return dict(ENVIRONMENTS[name])
