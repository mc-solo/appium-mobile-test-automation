# Testing

## What is tested

All tests drive the ApiDemos Android app (`io.appium.android.apis`)
on an emulator or real device through Appium (UiAutomator2).

| File | Marker | What it covers |
| --- | --- | --- |
| `tests/test_app_launch.py` | `smoke` | App launches (correct package in front), home list is visible, expected categories are present |
| `tests/test_navigation.py` | `navigation` | Home → Views, Views → back to home, Home → Text category |
| `tests/test_input.py` | `input` | Type text into Views → TextFields, clear and retype |
| `tests/test_gestures.py` | `gestures` | Swipe down then up on Views, long-press Buttons, scroll to Lists, tap at the centre of the screen |

Test data (typed text, expected labels) lives in `test-data/*.json`
and is loaded by the tests; no test hard-codes those values.
Gesture directions, durations and targets live in
`test-data/gestures_data.json`.

## Screenshots on failure

When a test fails, the hook in `conftest.py` saves a screenshot of
the screen it failed on to `screenshots/` (via
`utils/screenshot.py`, file name `<test-name>-<timestamp>.png`).
Screenshots taken on demand by page objects go to the same folder.
`screenshots/` is git-ignored.

## How to run

Prerequisites: emulator/device connected, ApiDemos installed, and
the Appium server running (see `docs/SETUP.md`).

Run everything:

```bash
pytest
```

Run one file or one marker:

```bash
pytest tests/test_app_launch.py -v
pytest -m smoke -v
pytest -m navigation -v
pytest -m input -v
pytest -m gestures -v
```

## Reports

Each run writes an HTML report to `reports/report.html`
(configured in `pytest.ini`). The `reports/` folder is git-ignored.

Screenshots taken on demand by page objects go to `screenshots/`
(also git-ignored).

## Current status — read before trusting a result

**These tests have only been collected, never run on a device or
emulator.** `pytest --collect-only` finds 12 tests (8 before, plus
4 gesture tests); there was no Appium server and no emulator/device
available when this was built, so there are no passing/failing
results yet. Do not treat this as a passing suite until you run it
yourself against a real emulator or device.
