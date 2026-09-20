from chek import *
from makeNumber import *
from processes import *


def polishCalc(expretion):

    if len(expretion) == 0:
        raise ValueError("Sorry, your expretion is incorrect")

    operation = []
    operand = []
    #make stack for operands and operations

    expretion = '0' + expretion
    expretion = expretion.replace('(', '(0')
    expretion = expretion.replace('0(', '(')
    #for correct work with negative numbers

    expretion = expretion.replace('--', '-1')
    expretion = expretion.replace('++', '+1')

    expretion = expretion.replace(' ', '')
    #we do not need space

    while token := expretion[:1]:

        expretion = expretion[1:]
        #cut our expretion
        ex = expretion[0] if len(expretion) > 0 else ""
        #we need to look at next character
        if token == '-' and ex != '(':
            #we need a special treatment for negative numbers
            num, expretion = negNum(expretion)
            operand, operation = clearing(operand, operation)
            operation.append(num)
            operand.append(1)
            """If program meet minus it makes a number negative and replace - with +"""

        elif isNum(token):

            num, expretion = makeNum(token, expretion)
            operation.append(num)
            """Makes number and put it to stack"""

        elif isOp(token):

            op = whatOp(token)

            if (operand and abs(operand[-1]) > abs(op) or ex == '(') and len(operation) > 1:
                #chek all options to make sure it is not exception
                operand, operation = clearing(operand, operation)
            """Makes possible calculating with numbers before branch"""

            operand.append(op)

            if ex == '(' and op != 0:

                operand.append(0)
                expretion = expretion[1:]
            """It helps to avoid a mistake if branch is the first character"""

        elif token == ')':
            #special treatment to closing branch
            operand, operation = clearing(operand, operation, 0)
            """Meeting closing branch we make all possible calculating till first opening branch"""

        elif token == '-' and ex == '(':
            #special treatment for negative expretion in branches
            operand.append(1)
            operand.append(-0.1)
            expretion = expretion[1:]
            """Program goes to the end of expretion, calculates it and makes negative"""
        else:
            #to warn user about mistake
            raise SyntaxError("Sorry, you wrote unknown symbol")

    operand, operation = clearing(operand, operation)
    """clears stack when it is the end"""

    return operation.pop()


print(polishCalc('-3-((2+5)*(4-2))'))
