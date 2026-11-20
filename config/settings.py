"""Central settings for the Appium tests.

All configuration lives here. Nothing else in the repo (pages,
tests, conftest) hard-codes a server URL, device name, platform
version, app package/activity, or timeout: they all read it from
:func:`get_settings`.

Precedence, highest first:
1. Environment variables (see .env.example for the full list).
2. The preset for APPIUM_ENV in config/environments.py.
3. The built-in defaults in that preset.

A ``.env`` file in the repo root is loaded automatically when
``python-dotenv`` is installed; it is never required.
"""

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv is optional; env vars still work.
    pass

from config.environments import DEFAULT_ENVIRONMENT, get_environment_preset


def _env_str(name, default):
    return os.getenv(name, default)


def _env_int(name, default):
    return int(os.getenv(name, str(default)))


def _env_bool(name, default):
    return os.getenv(name, str(default)).lower() == "true"


@dataclass(frozen=True)
class Settings:
    environment: str
    platform_name: str
    device_name: str
    platform_version: str
    automation_name: str
    app_package: str
    app_activity: str
    no_reset: bool
    new_command_timeout: int
    timeout: int
    server_url: str
    screenshot_dir: str

    def capabilities(self):
        """Desired capabilities dict for an Android session."""
        return {
            "platformName": self.platform_name,
            "appium:deviceName": self.device_name,
            "appium:platformVersion": self.platform_version,
            "appium:automationName": self.automation_name,
            "appium:appPackage": self.app_package,
            "appium:appActivity": self.app_activity,
            "appium:noReset": self.no_reset,
            "appium:newCommandTimeout": self.new_command_timeout,
        }


def get_settings(environment=None):
    """Build Settings from the named environment preset + env vars."""
    env_name = environment or os.getenv("APPIUM_ENV", DEFAULT_ENVIRONMENT)
    preset = get_environment_preset(env_name)
    return Settings(
        environment=env_name,
        platform_name=_env_str("APPIUM_PLATFORM_NAME", preset["platform_name"]),
        device_name=_env_str("APPIUM_DEVICE_NAME", preset["device_name"]),
        platform_version=_env_str(
            "APPIUM_PLATFORM_VERSION", preset["platform_version"]
        ),
        automation_name=_env_str(
            "APPIUM_AUTOMATION_NAME", preset["automation_name"]
        ),
        app_package=_env_str("APPIUM_APP_PACKAGE", preset["app_package"]),
        app_activity=_env_str("APPIUM_APP_ACTIVITY", preset["app_activity"]),
        no_reset=_env_bool("APPIUM_NO_RESET", preset["no_reset"]),
        new_command_timeout=_env_int(
            "APPIUM_NEW_COMMAND_TIMEOUT", preset["new_command_timeout"]
        ),
        timeout=_env_int("APPIUM_TIMEOUT", preset["timeout"]),
        server_url=_env_str("APPIUM_SERVER_URL", preset["server_url"]),
        screenshot_dir=_env_str("APPIUM_SCREENSHOT_DIR", preset["screenshot_dir"]),
    )
