from chek import *
from makeNumber import *


def clearing(opnd, opon2, opon1):    #made to clear stack: calculate exp that we already have

    second = opon2
    first = opon1

    match opnd:                      #cheking kind of operand
        case -1:
            res = first - second
        case 1:
            res = first + second
        case 2:
            res = first * second
        case -2:
            res = first / second
        case _:
            res = 0
            raise SyntaxError('Unknown operand')

    return res


def polishCalc(expretion):          #the main function to calculate expretion
    operation = []                  #list with numbers
    operand = []                    #list with operands

    expretion = '0' + expretion
    expretion = expretion.replace('(', '(0')  #exclude variant when we have negative number

    while token := expretion[:1]:
        expretion = expretion[1:]

        if isNum(token):                               #if meet number - get it and add to stack
            num, expretion = makeNum(token, expretion)
            operation.append(num)

        if isOp(token):                                #if meet operand - try to make calc or just add it to stack
            op = whatOp(token)

            if operand and abs(operand[-1]) > abs(op):
                while operand:                         #if met "(" or "+" after "*" - make calc and go next
                    res = clearing(operand.pop(), operation.pop(), operation.pop())
                    operation.append(res)

            operand.append(op)

    while operand:                                     #final calculating
        res = clearing(operand.pop(), operation.pop(), operation.pop())
        operation.append(res)

    return operation.pop()


print(polishCalc('20+3*6-2'))