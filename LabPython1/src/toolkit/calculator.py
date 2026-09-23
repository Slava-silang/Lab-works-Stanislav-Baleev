from . import check, make_number, processes, errors


def processing(expression):
    expression = expression.replace(' ', '')
    """Makes work easier because we dont need to process spaces"""

    return expression


def polish_calc(expression):
    numbers = []
    operators = []
    """Makes stack for operands and numbers"""

    expression = processing(expression)
    errors.check_expression(expression)

    i = 0
    expecting_numbers = True

    while i < len(expression):

        token = expression[i]

        if check.is_num(token):
            start = i

            number, i = make_number.make_num(expression, i, start)

            numbers.append(number)
            expecting_numbers = False
            continue

        if token == '+' and expecting_numbers:
            i += 1
            continue

        if token == '-' and expecting_numbers:
            i += 1
            start = i

            number, i = make_number.make_num(expression, i, start)
            numbers.append(-number)
            expecting_numbers = False
            continue

        if token == '(':
            operators.append(0)
            expecting_numbers = True
            i += 1
            continue

        if token == ')':

            while operators and operators[-1] != 0:
                operators, numbers = processes.clearing(operators, numbers)

            operators.pop()
            expecting_numbers = False
            i += 1
            continue

        if check.is_operand(token):

            operator, i = check.what_operator(expression, i)

            while (
                operators
                and operators[-1] != 0
                and processes.priority(operators[-1])
                >= processes.priority(operator)
            ):
                operators, numbers = processes.clearing(operators, numbers)

            operators.append(operator)
            expecting_numbers = True
            continue

    while operators:
        operators, numbers = processes.clearing(operators, numbers)

    if len(numbers) != 1:
        raise ValueError("Sorry, your expression is incorrect")

    return numbers.pop()
