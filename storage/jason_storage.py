import json
import os

DATA_FILE = "data/apps.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tabs": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"tabs": []}


def save_data(data):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)