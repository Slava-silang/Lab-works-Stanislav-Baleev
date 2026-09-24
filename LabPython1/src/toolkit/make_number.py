def make_num(expression, i, start):
    """Makes numbers by going through all tokens until finds
    a symbol that cannot belong to number."""
    while i < len(expression) and expression[i] in "0123456789.":
        i += 1

    number = float(expression[start:i])

    return number, i
