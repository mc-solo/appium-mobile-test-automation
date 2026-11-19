"""Appium capabilities for the ApiDemos Android app.

A real Android emulator or device is required to run these tests.
Nothing here starts an emulator or connects to a device on import.
"""

import os


def get_android_capabilities():
    """Return the desired capabilities dict for an Android emulator.

    Every value can be overridden with an environment variable, so the
    same code works on a different emulator or a real device without
    editing this file.
    """
    return {
        "platformName": os.getenv("APPIUM_PLATFORM_NAME", "Android"),
        "appium:deviceName": os.getenv(
            "APPIUM_DEVICE_NAME", "Android Emulator"
        ),
        "appium:platformVersion": os.getenv("APPIUM_PLATFORM_VERSION", "14"),
        "appium:automationName": os.getenv("APPIUM_AUTOMATION_NAME", "UiAutomator2"),
        "appium:appPackage": os.getenv("APPIUM_APP_PACKAGE", "io.appium.android.apis"),
        "appium:appActivity": os.getenv("APPIUM_APP_ACTIVITY", ".ApiDemos"),
        "appium:noReset": os.getenv("APPIUM_NO_RESET", "false").lower() == "true",
        "appium:newCommandTimeout": int(os.getenv("APPIUM_NEW_COMMAND_TIMEOUT", "60")),
    }


def get_appium_server_url():
    """URL of the Appium server. Default is the local server."""
    return os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
