import json
from re import findall

from . import constants


def check_expression(expression: str = ""):
    """Checks almost all possible to find before calculating
    errors in expression."""
    if len(expression) == 0:
        raise ValueError("Sorry, your expression is empty.")

    if ".." in expression:
        raise SyntaxError("Sorry, your expression is incorrect")

    if len(findall(r"[-+/*%]\)|\([*/%]", expression)):
        raise SyntaxError("Sorry, your expression is incorrect")

    if "()" in expression:
        raise SyntaxError("Sorry, your expression is incorrect")

    branches = []

    for i in range(len(expression)):
        allowed = "0123456789-+/*%()."

        if i == len(expression) - 1 and expression[i] in "-+":
            raise SyntaxError("Sorry, your expression is incorrect")

        if expression[i] not in allowed:
            raise SyntaxError(f"Sorry, unknown character {expression[i]}")

        if expression[i] == "(":
            branches.append(0)

        if expression[i] == ")":
            branches.append(1)

    if len(branches) > 0 and (
        branches[0] == 1 or branches[-1] == 0 or branches.count(0) != branches.count(1)
    ):
        raise SyntaxError("Sorry, your branches is incorrect")

    if len(branches) == len(expression):
        raise ValueError("Sorry, your expression is empty")

    opened = []
    for i in branches:
        if i == "(":
            opened.append(1)

        if i == ")":
            if len(opened) == 0:
                raise SyntaxError("Sorry, your branches is incorrect")

            else:
                opened.pop()


def check_units(amount: float, from_: str, to: str):
    """Checks unit compatibility and whether
    temperature is above absolute zero."""
    amount = float(amount)

    with open(constants.CONFIG_PATH, "r", encoding="utf-8") as file:
        units = json.load(file)
    from_ = from_.lower()
    to = to.lower()

    from_group = None
    to_group = None

    for group, group_units in units.items():
        if from_ in group_units:
            from_group = group
        if to in group_units:
            to_group = group

    if from_group is None or to_group is None:
        raise SyntaxError("sorry, unknown unit")

    if from_group != to_group:
        raise ValueError(f"Sorry, we cannot convert {from_} to {to}")

    if from_group == "temperature":
        if from_ == "c" and amount < constants.ABSOLUTE_ZERO_C:
            raise ValueError("Sorry, temperature cannot be under absolute zero")

        if from_ == "k" and amount < constants.ABSOLUTE_ZERO_K:
            raise ValueError("Sorry, temperature cannot be under absolute zero")

        if from_ == "f" and amount < constants.ABSOLUTE_ZERO_F:
            raise ValueError("Sorry, temperature cannot be under absolute zero")
