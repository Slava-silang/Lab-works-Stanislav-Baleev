def make_num(tok, exp):
                    #makes positive numbers
    number = tok
    count = 0

    for i in exp:

        if i in '0123456789.':
            number += i
            count += 1

        else:
            break

    return float(number), exp[count:]


def neg_num(exp):
                    #makes negative numbers
    number = ""
    count = 0

    for i in exp:

        if i in '0123456789.':
            number += i
            count += 1

        else:
            break

    return -1*float(number), exp[count:]
