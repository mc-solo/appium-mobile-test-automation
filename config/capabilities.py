"""Appium capabilities for the ApiDemos Android app.

Thin compatibility layer over config.settings: all values come from
the environment preset plus env vars, so nothing is hard-coded here.
Prefer importing ``get_settings`` from config.settings directly.

A real Android emulator or device is required to run these tests.
Nothing here starts an emulator or connects to a device on import.
"""

from config.settings import get_settings


def get_android_capabilities():
    """Return the desired capabilities dict for an Android session."""
    return get_settings().capabilities()


def get_appium_server_url():
    """URL of the Appium server. Default is the local server."""
    return get_settings().server_url
