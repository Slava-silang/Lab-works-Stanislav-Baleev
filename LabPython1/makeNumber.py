def makeNum(tok, exp):              #makes positive number with its characters
    number = tok
    count = 0
    for i in exp:
        if i in '0123456789.':
            number += i
            count += 1
        else:
            break
    return float(number), exp[count:]


def negNum(exp):                    #makes negative numbers
    number = ""
    count = 0
    for i in exp:
        if i in '0123456789.':
            number += i
            count += 1
        else:
            break
    return -1*float(number), exp[count:]