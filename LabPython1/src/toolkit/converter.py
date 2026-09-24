import json

from . import constants, errors


def load_units():
    """Loads units from configuration file."""
    with open(constants.CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def converter(amount, from_, to):
    """Converts from unit_1 to unit_2 by looking for
    ratios of units in configuration file."""
    errors.check_units(amount, from_, to)

    units = load_units()

    amount = float(amount)
    from_ = from_.lower()
    to = to.lower()

    from_group = None
    to_group = None

    for group, group_units in units.items():
        if from_ in group_units:
            from_group = group

        if to in group_units:
            to_group = group

    if from_group == to_group == "temperature":
        if from_ == "c":
            celsius = amount
        elif from_ == "f":
            celsius = (amount - 32) * 5 / 9
        else:
            celsius = amount + constants.ABSOLUTE_ZERO_C

        if to == "c":
            return celsius
        elif to == "f":
            return celsius * 9 / 5 + 32
        else:
            return celsius - constants.ABSOLUTE_ZERO_C

    else:
        base_value = amount * units[from_group][from_]
        return base_value / units[to_group][to]
