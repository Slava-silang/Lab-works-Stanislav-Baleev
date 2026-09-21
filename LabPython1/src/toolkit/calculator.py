from . import check, make_number, processes


def processing(expression):
    expression = '0' + expression
    expression = expression.replace('(', '(0')
    expression = expression.replace('0(', '(')
    """For correct work with negative numbers we need to change work, 
    otherwise program counting -2-3 gives -1, but 0-2-3 gives correct answer"""

    expression = expression.replace('--', '-1+')
    expression = expression.replace('++', '1+')
    expression = expression.replace('//', '|')
    """Makes easier to work with double operands"""

    expression = expression.replace(' ', '')
    """Makes work easier because we dont need to process spaces"""

    return expression


def polish_calc(expression):
    operation = []
    operand = []
    """Makes stack for operands and operation"""

    expression = processing(expression)

    while token := expression[:1]:

        expression = expression[1:]

        ex = expression[0] if len(expression) > 0 else ""

        if token == '-' and ex != '(':
            """Makes negative numbers, instead of using minus uses + with negative number"""

            num, expression = make_number.neg_num(expression)
            operand, operation = processes.clearing(operand, operation)
            operation.append(num)
            operand.append(1)

        elif check.is_num(token):
            """Makes number and put it to stack"""
            num, expression = make_number.make_num(token, expression)
            operation.append(num)

        elif check.is_operand(token):

            op = check.what_operand(token)

            if (operand and abs(operand[-1]) > abs(op) or ex == '(') and len(operation) > 1:

                operand, operation = processes.clearing(operand, operation)
                """Makes possible calculating with numbers before branch"""

            operand.append(op)

            if ex == '(' and op != 0:
                operand.append(0)
                expression = expression[1:]
                """It helps to avoid a mistake if branch is the first character"""

        elif token == ')':

            operand, operation = processes.clearing(operand, operation, 0)
            """Meeting closing branch we make all possible calculating till first opening branch"""

        elif token == '-' and ex == '(':

            operand.append(1)
            operand.append(-0.1)
            expression = expression[1:]
            """Program goes to the end of expression, calculates it and makes negative"""

    operand, operation = processes.clearing(operand, operation)
    """clears stack when it is the end"""

    return operation.pop()
