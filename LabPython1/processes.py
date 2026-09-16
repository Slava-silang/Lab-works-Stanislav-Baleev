def calculating(opnd, opon2, opon1):

    second = opon2
    first = opon1
    res = 0

    match opnd:
        case -1:
            res = first - second
        case 1:
            res = first + second
        case 2:
            res = first * second
        case -2:
            res = first / second
        case -1:
            res = first - second
        case 0:
            raise SyntaxError("Sorry, you forgot to close a bracket")

    return res


def clearing(operand, operation, status=1):

    if status:

        while operand and operand[-1] != 0:

            res = calculating(operand.pop(), operation.pop(), operation.pop())
            operation.append(res)

    else:

        while operand and operand[-1] != 0:

            res = calculating(operand.pop(), operation.pop(), operation.pop())
            operation.append(res)

        if operand[-1] == 0:

            operand.pop()

        else:

            raise SyntaxError("Sorry, you forgot to open bracket")

    return operand, operation
