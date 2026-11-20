# Setup

## What you need

- Python 3.10+
- Node.js (for the Appium server)
- Android Studio, or an Android SDK with `adb`
- An Android emulator (AVD) or a real device with USB debugging on
- The ApiDemos APK (`io.appium.android.apis`)

## 1. Install the Appium server

```bash
npm install -g appium
appium driver install uiautomator2
```

Check it with:

```bash
appium --version
appium driver list
```

## 2. Install the Python dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Configure (optional)

Defaults target a local emulator running ApiDemos. To change
anything, copy `.env.example` to `.env` and edit it, or export the
variables directly:

```bash
cp .env.example .env
```

| Variable | Default | Meaning |
| --- | --- | --- |
| `APPIUM_ENV` | `emulator` | Preset in `config/environments.py` (`emulator`, `real_device`) |
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` | Appium server URL |
| `APPIUM_DEVICE_NAME` | `Android Emulator` | Device/emulator name |
| `APPIUM_PLATFORM_VERSION` | `14` | Android version |
| `APPIUM_APP_PACKAGE` | `io.appium.android.apis` | App under test |
| `APPIUM_APP_ACTIVITY` | `.ApiDemos` | App launch activity |
| `APPIUM_TIMEOUT` | `10` | Explicit-wait timeout, seconds |
| `APPIUM_NEW_COMMAND_TIMEOUT` | `60` | Appium session timeout, seconds |

Never commit a real `.env` file; it is git-ignored.

## 4. Start an emulator or connect a device

Create an AVD in Android Studio (AVD Manager) and launch it, or
connect a real device with USB debugging enabled. Verify it is seen:

```bash
adb devices
```

Install ApiDemos on it:

```bash
adb install path/to/ApiDemos.apk
```

## 5. Start the Appium server

In a separate terminal:

```bash
appium
```

It listens on `http://127.0.0.1:4723` by default. Leave it running
while the tests execute.
