from . import check, make_number, processes


def processing(expretion):

    expretion = '0' + expretion
    expretion = expretion.replace('(', '(0')
    expretion = expretion.replace('0(', '(')
    # for correct work with negative numbers

    expretion = expretion.replace('--', '-1+')
    expretion = expretion.replace('++', '1+')
    expretion = expretion.replace('//', '|')

    expretion = expretion.replace(' ', '')

    return expretion
def polish_calc(expretion):

    operation = []
    operand = []
    #make stack for operands and operations

    expretion = processing(expretion)

    while token := expretion[:1]:

        expretion = expretion[1:]
        #cut our expretion
        ex = expretion[0] if len(expretion) > 0 else ""
        #we need to look at next character
        if token == '-' and ex != '(':
            #we need a special treatment for negative numbers
            num, expretion = make_number.neg_num(expretion)
            operand, operation = processes.clearing(operand, operation)
            operation.append(num)
            operand.append(1)
            """If program meet minus it makes a number negative and replace - with +"""

        elif check.is_num(token):

            num, expretion = make_number.make_num(token, expretion)
            operation.append(num)
            """Makes number and put it to stack"""

        elif check.is_operand(token):

            op = check.what_operand(token)

            if (operand and abs(operand[-1]) > abs(op) or ex == '(') and len(operation) > 1:
                #chek all options to make sure it is not exception
                operand, operation = processes.clearing(operand, operation)
            """Makes possible calculating with numbers before branch"""

            operand.append(op)

            if ex == '(' and op != 0:

                operand.append(0)
                expretion = expretion[1:]
            """It helps to avoid a mistake if branch is the first character"""

        elif token == ')':
            #special treatment to closing branch
            operand, operation = processes.clearing(operand, operation, 0)
            """Meeting closing branch we make all possible calculating till first opening branch"""

        elif token == '-' and ex == '(':
            #special treatment for negative expretion in branches
            operand.append(1)
            operand.append(-0.1)
            expretion = expretion[1:]
            """Program goes to the end of expretion, calculates it and makes negative"""

    operand, operation = processes.clearing(operand, operation)
    """clears stack when it is the end"""

    return operation.pop()
