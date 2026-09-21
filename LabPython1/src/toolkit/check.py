def is_num(tok):
    return tok in '0123456789'


def is_operand(tok):
    return tok in '+*/(|%'


def what_operand(tok):
    match tok:
        case '+':
            return 1
        case '*':
            return 2
        case '/':
            return -2
        case '(':
            return 0
        case '|':
            return -3
        case '%':
            return 3
