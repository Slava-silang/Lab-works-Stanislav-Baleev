def is_num(token):
    """Check whether token is number ot its part."""
    return token in "0123456789."


def is_operator(token):
    """Check whether token is operator."""
    return token in "+*/(%-"


def what_operator(expression, i):
    """Makes tokenization and return result.
    Also check whether it is // or /"""
    token = expression[i]

    if token == "/" and len(expression) > i + 1 and expression[i + 1] == "/":
        operator = -3
        i += 2
    elif token == "/":
        operator = -2
        i += 1

    match token:
        case "+":
            operator = 1
            i += 1
        case "-":
            operator = -1
            i += 1
        case "*":
            operator = 2
            i += 1
        case "%":
            operator = 3
            i += 1

    return operator, i
