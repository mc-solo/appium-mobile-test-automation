# Architecture

## Folder tree

```
appium-mobile-test-automation/
├── .env.example          safe default config (copy to .env, never commit .env)
├── .gitignore
├── ARCHITECTURE.md       this file
├── README.md
├── conftest.py           pytest fixtures: driver, home_page, views_page
├── pytest.ini            testpaths, markers, HTML report location
├── requirements.txt
├── config/
│   ├── __init__.py       re-exports get_settings / capabilities helpers
│   ├── capabilities.py   thin wrapper over settings (backwards compat)
│   ├── environments.py   named presets: emulator, real_device
│   └── settings.py       Settings dataclass; env vars > preset > defaults
├── docs/
│   ├── SETUP.md          install, emulator, Appium server
│   └── TESTING.md        what is tested, how to run, reports
├── pages/
│   ├── __init__.py
│   ├── base_page.py      find/tap/enter text/visibility/screenshot
│   ├── home_page.py      ApiDemos home list + Text screen items
│   └── views_page.py     ApiDemos Views list + text field
├── test-data/
│   ├── input_data.json       text typed into fields
│   ├── launch_data.json      expected package + home categories
│   └── navigation_data.json  expected Text-screen items
└── tests/
    ├── __init__.py
    ├── data_loader.py        loads test-data/*.json
    ├── test_app_launch.py    smoke tests
    ├── test_input.py         input tests
    └── test_navigation.py    navigation tests
```

Generated at runtime (git-ignored): `reports/`, `screenshots/`, `.venv/`, `__pycache__/`.

## Why each folder exists

- `config/` — the single source of truth for everything that varies
  by machine or device: server URL, device name, platform version,
  app package/activity, timeouts. Nothing else in the repo contains
  one of those values.
- `test-data/` — the strings tests type and assert on, as JSON. Data
  changes without touching test code.
- `pages/` — page objects. Each class knows the locators and actions
  of one screen and nothing about test data or configuration, except
  that `BasePage` reads its timeout and screenshot folder from
  `config.settings`.
- `tests/` — test logic only: arrange via page objects, assert
  against loaded test data. A test never builds a driver, a
  capability, or a locator string.
- `docs/` — setup and testing guides, so the README stays short.

## Data flow

```
.env / env vars ─┐
                 ├─► config/environments.py (preset for APPIUM_ENV)
                 │        │
                 │        ▼
                 │   config/settings.py (Settings)
                 │        ├──► config/capabilities.py ─► conftest.py driver fixture
                 │        └──► pages/base_page.py (timeout, screenshot dir)
                 │
test-data/*.json ────────► tests/data_loader.py ─► tests/test_*.py
                                                        │
pages/*.py (locators + actions) ◄── conftest.py fixtures ─┘
```

1. `conftest.py` builds the Appium driver from
   `config.settings.get_settings()` and hands page objects to tests.
2. Tests load their expected values from `test-data/*.json` via
   `tests/data_loader.py`.
3. Tests call page-object methods (`home_page.open_views()`,
   `views.type_in_text_field(...)`); assertions compare the app's
   state with the loaded data.

## How config / test-data / pages / tests connect

| Piece | Knows about | Must not contain |
| --- | --- | --- |
| `config/` | env vars, presets | test logic, locators, test data |
| `test-data/` | expected strings only | code, locators, config |
| `pages/` | locators + actions for one screen | test data, assertions, config values (except via `settings`) |
| `tests/` | page objects + loaded data | hard-coded strings, drivers, capabilities |
| `conftest.py` | settings + page objects | test data, assertions |

## How to add a new test

1. If the test needs a new screen, add a page object in `pages/`
   extending `BasePage`, with one locator constant and one method per
   action. Reuse `BasePage` helpers; do not add waits or paths.
2. If the test types or asserts on a string, add it to the matching
   `test-data/*.json` file (or a new one) and load it with
   `load_json(...)` from `tests/data_loader.py`.
3. If the test needs a new setting (new device, new timeout), add it
   to `config/settings.py` (and the preset in
   `config/environments.py` plus `.env.example`), never inline.
4. Add `tests/test_<area>.py`, mark it (`@pytest.mark.smoke`,
   `navigation`, `input`, or a new marker registered in
   `pytest.ini`), and use the `driver` / page fixtures from
   `conftest.py`.
5. Verify with `pytest --collect-only`, then run against an emulator
   or device with the Appium server up.
