import json
from pathlib import Path


HISTORY_PATH = Path(__file__).resolve().parents[2] / "history.json"

def save_history(expression, result):
    if HISTORY_PATH.exists():
        with open(HISTORY_PATH, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if content:
            history = json.loads(content)
        else:
            history = []
    else:
        history = []

    history.append({
        "expression": expression,
        "result": result
    })

    with open(HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)


def get_history():
    if not HISTORY_PATH.exists():
        return []

    with open(HISTORY_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
