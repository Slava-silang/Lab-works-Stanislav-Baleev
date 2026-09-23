import json

from . import constants


def save_history(expression, result):
    if constants.HISTORY_PATH.exists():
        with open(constants.HISTORY_PATH, "r", encoding="utf-8") as file:
            content = file.read().strip()
        if content:
            history = json.loads(content)
        else:
            history = []
    else:
        history = []

    history.append({"expression": expression, "result": result})

    with open(constants.HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)


def get_history():
    if not constants.HISTORY_PATH.exists():
        return []

    with open(constants.HISTORY_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
