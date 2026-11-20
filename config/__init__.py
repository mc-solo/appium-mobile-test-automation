"""Config package: settings, environment presets, capabilities."""

from config.environments import ENVIRONMENTS, get_environment_preset
from config.settings import Settings, get_settings

__all__ = [
    "ENVIRONMENTS",
    "Settings",
    "get_android_capabilities",
    "get_environment_preset",
    "get_settings",
]

from config.capabilities import get_android_capabilities  # noqa: E402
