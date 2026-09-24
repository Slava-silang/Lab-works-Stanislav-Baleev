def calculating(operator: int, second: float, first: float):
    """Performs calculating depending on the operator."""
    res = 0

    match operator:
        case -3:
            if second == 0:
                raise ZeroDivisionError("Sorry, we cannot divide by zero")
            return first // second

        case -2:
            if second == 0:
                raise ZeroDivisionError("Sorry, we cannot divide by zero")
            return first / second

        case -1:
            return first - second

        case 1:
            return first + second

        case 2:
            return first * second

        case 3:
            if second == 0:
                raise ZeroDivisionError("Sorry, we cannot divide by zero")
            return first % second

    return res


def priority(operator: int):
    """Makes correct calculating by
    returning the priority of operator"""
    if operator in [1, -1]:
        return 1

    if operator in (2, -2, -3, 3):
        return 2

    return 0


def clearing(operators: list, numbers: list):
    """Directs numbers and operator to calculating def
    and returns result."""
    if not operators:
        return operators, numbers

    if len(numbers) < 2:
        raise SyntaxError("Sorry, your expression is incorrect")

    operator = operators.pop()

    second = numbers.pop()
    first = numbers.pop()

    result = calculating(operator, second, first)
    numbers.append(result)

    return operators, numbers
