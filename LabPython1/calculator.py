from chek import *
from makeNumber import *
from processes import *


def polishCalc(expretion):

    operation = []
    operand = []
    #make stack for operands and operations

    expretion = '0' + expretion
    expretion = expretion.replace('(', '(0')
    expretion = expretion.replace('0(', '(')

    while token := expretion[:1]:

        expretion = expretion[1:]

        if token == '-':
            #we need a special treatment for negative numbers
            num, expretion = negNum(expretion)
            operand, operation = clearing(operand, operation)
            operation.append(num)
            operand.append(1)

        elif isNum(token):

            num, expretion = makeNum(token, expretion)
            #make number
            operation.append(num)
            #and put it to stack

        elif isOp(token):

            op = whatOp(token)

            ex = expretion[0]
            #we need to look at the next character if it is "("

            if operand and abs(operand[-1]) > abs(op) or ex == '(' and len(operation) > 1:
                #chek all options to make sure it is not exception
                operand, operation = clearing(operand, operation)

            operand.append(op)

            if ex == '(' and op != 0:
                #if we did not put "(" to stack before
                operand.append(0)
                expretion = expretion[1:]

        elif token == ')':
            #special treatment to closing branch
            operand, operation = clearing(operand, operation, 0)
        else:
            #to warn user about mistake
            raise SyntaxError("Sorry, you wrote unknown symbol")

    operand, operation = clearing(operand, operation)
    #clear stack when it is the end

    return operation.pop()


print(polishCalc('((5+4)+(7+9)*4)*7'))
