# Appium Mobile Test Automation

Python + Appium starter for testing the ApiDemos Android app on an emulator or a real device.

## What this is

A small, real starter: capabilities with env overrides, page objects for the ApiDemos home and Views screens, and pytest tests for launch, navigation, and text input.

## What this is not

These tests were **not run on a device** in this scaffold build. They need a running emulator or device and an Appium server, neither of which was available here. Do not treat this as a passing suite until you run it yourself.

## Setup

1. Install Python 3.10+ and the Appium server:
   ```bash
   npm install -g appium
   appium driver install uiautomator2
   ```
2. Create a virtual environment and install the dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Start an Android emulator (Android Studio AVD Manager) or connect a real device with USB debugging on.
4. Install the ApiDemos apk on the emulator/device:
   ```bash
   adb install path/to/ApiDemos.apk
   ```
5. Start the Appium server:
   ```bash
   appium
   ```

## Run the tests

```bash
pytest
```

To run one file:

```bash
pytest tests/test_app_launch.py -v
```

A HTML report is written to `reports/report.html`.

## Config

Capabilities live in `config/capabilities.py`. Override them without editing code:

| Env var | Default |
| --- | --- |
| `APPIUM_DEVICE_NAME` | `Android Emulator` |
| `APPIUM_PLATFORM_VERSION` | `14` |
| `APPIUM_APP_PACKAGE` | `io.appium.android.apis` |
| `APPIUM_APP_ACTIVITY` | `.ApiDemos` |
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` |

## Layout

```
config/capabilities.py   Android capabilities + env overrides
pages/base_page.py       tap, find, enter text, screenshot helpers
pages/home_page.py       ApiDemos home list
pages/views_page.py      ApiDemos Views list
tests/test_app_launch.py
tests/test_navigation.py
tests/test_input.py
conftest.py              driver fixture (connects only when a test runs)
```
