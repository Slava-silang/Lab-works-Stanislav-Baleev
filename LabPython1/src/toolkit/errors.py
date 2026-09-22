import json
from re import findall

from . import constants


def check_expression(expression: str):
    if len(expression) < 0:
        raise ValueError("Sorry, your expression is empty.")

    if expression.count(")") < expression.count("("):
        raise SyntaxError("Sorry, you forgot to close the branch.")

    if expression.count(")") > expression.count("("):
        raise SyntaxError("Sorry, you forgot to open the branch.")

    if expression.count('/0') - expression.count('/0.') != 0:
        raise ValueError("Sorry, dividing by zero is impossible.")

    if len(findall(r"/0\.(0)+", expression)) != len(findall(r"/0\.(0)+[123456789]", expression)):
        raise ValueError("Sorry, dividing by zero is impossible.")

    if len(findall(r"([*%]{2})|([+-/]{3})|(\w[+-]{2}\w)|[*%][-+*/%]|[-+*/%][*%]|\w[+-]{2}", expression)):
        raise SyntaxError("Sorry, your expression is incorrect.")

    for i in range(len(expression)):

        if expression[i] in '-/+' and expression[i-1] in '-/+' and expression[i] != expression[i+1]:
            raise SyntaxError("Sorry, your expression is incorrect.")

        allowed = '0123456789-+/*%'

        if expression[i] not in allowed:
            raise SyntaxError(f"Sorry, unknown character {expression[i]}")


def check_units(amount: float, from_: str, to: str):

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

    if from_group != to_group:
        raise ValueError(f"Sorry, we cannot convert {from_} to {to}")

    if from_group == "temperature":

        if from_ == 'c' and amount < constants.ABSOLUTE_ZERO_C:
            raise ValueError("Sorry, temperature cannot be under absolute zero")

        if from_ == 'k' and amount < constants.ABSOLUTE_ZERO_K:
            raise ValueError("Sorry, temperature cannot be under absolute zero")

        if from_ == 'f' and amount < constants.ABSOLUTE_ZERO_F:
            raise ValueError("Sorry, temperature cannot be under absolute zero")
