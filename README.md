# Appium Mobile Test Automation

Python + Appium tests for the ApiDemos Android app on an emulator or a real device.

## Status — honest

**These tests have only been collected, never run on a device or
emulator.** `pytest --collect-only` finds 12 tests. There was no
Appium server and no emulator/device available when this was built,
so there are no passing or failing results yet. Do not treat this as
a passing suite until you run it yourself.

## Folder tree

```
config/            settings, environment presets, capabilities
test-data/         JSON test data (typed text, expected labels, gestures)
pages/             page objects (Base, Home, Views) incl. gestures
tests/             smoke, navigation, input, gestures tests
utils/             screenshot helper (used by the failure hook)
docs/              SETUP.md, TESTING.md
conftest.py        driver + page fixtures
pytest.ini         markers, HTML report to reports/report.html
```

See `ARCHITECTURE.md` for why each folder exists and how to add a
new test.

## Setup

Full guide: `docs/SETUP.md`.

```bash
npm install -g appium
appium driver install uiautomator2

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # optional, edit only what differs
adb install path/to/ApiDemos.apk
appium                     # separate terminal, leave running
```

## Run the tests

Requires a connected emulator/device with ApiDemos installed and
the Appium server running.

```bash
pytest
pytest tests/test_app_launch.py -v
pytest -m smoke -v
pytest -m navigation -v
pytest -m input -v
pytest -m gestures -v
```

When a test fails, a screenshot of the failing screen is saved to
`screenshots/` by the hook in `conftest.py`.

A HTML report is written to `reports/report.html`.

## Config

All settings live in `config/settings.py` (env vars override the
preset selected by `APPIUM_ENV` in `config/environments.py`).
Copy `.env.example` to `.env` to change them without editing code.

| Env var | Default |
| --- | --- |
| `APPIUM_ENV` | `emulator` |
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` |
| `APPIUM_DEVICE_NAME` | `Android Emulator` |
| `APPIUM_PLATFORM_VERSION` | `14` |
| `APPIUM_APP_PACKAGE` | `io.appium.android.apis` |
| `APPIUM_APP_ACTIVITY` | `.ApiDemos` |
| `APPIUM_TIMEOUT` | `10` |
| `APPIUM_NEW_COMMAND_TIMEOUT` | `60` |

## What is tested

| File | Covers |
| --- | --- |
| `tests/test_app_launch.py` | App launches, home list visible, expected categories |
| `tests/test_navigation.py` | Home → Views, Views → back, Home → Text |
| `tests/test_input.py` | Type / clear / retype in Views → TextFields |
| `tests/test_gestures.py` | Swipe, long-press, scroll to Lists, tap at screen centre |

Details: `docs/TESTING.md`.
