def isNum(tok):
    return tok in '0123456789'


def isOp(tok):
    return tok in '+-*/('


def whatOp(tok):
    match tok:
        case '-':
            return -1
        case '+':
            return 1
        case '*':
            return 2
        case '/':
            return -2
        case '(':
            return 0