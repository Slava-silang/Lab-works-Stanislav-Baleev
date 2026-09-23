def is_num(tok):
    return tok in "0123456789."


def is_operand(tok):
    return tok in "+*/(%-"


def what_operator(expression, i):
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
