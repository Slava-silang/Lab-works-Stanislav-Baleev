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
        case -3:
            res = first // second
        case 3:
            res = first - (first // second) * second

    return res


def clearing(operand, operation, status=1):
    if status:

        while operand and operand[-1] not in [0, -0.1]:
            res = calculating(operand.pop(), operation.pop(), operation.pop())
            operation.append(res)

    else:

        while operand and operand[-1] not in [0, -0.1]:

            res = calculating(operand.pop(), operation.pop(), operation.pop())
            operation.append(res)

        if operand[-1] == 0:

            operand.pop()
        elif operand[-1] == -0.1:

            operand.pop()
            operation[-1] = operation[-1] * (-1)

    return operand, operation
