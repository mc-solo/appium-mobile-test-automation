"""Load test data from the test-data/ JSON files.

Tests never hard-code the strings they type or assert on; they load
them here so the same test can run against different data without
editing code.
"""

import json
from pathlib import Path

TEST_DATA_DIR = Path(__file__).resolve().parents[1] / "test-data"


def load_json(name):
    """Load ``test-data/<name>.json`` and return it as a dict."""
    path = TEST_DATA_DIR / f"{name}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)
