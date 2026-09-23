def make_num(expression, i, start):

    while i < len(expression) and expression[i] in '0123456789.':
        i += 1

    number = float(expression[start:i])

    return number, i
