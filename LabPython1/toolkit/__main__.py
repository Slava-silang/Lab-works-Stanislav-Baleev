import sys
import argparse
from . import calculator
from . import converter

if sys.argv[1] == "calc":
    calculator.polishCalc(sys.argv[2])

if sys.argv[1] == "converter":
    try:

        parser = argparse.ArgumentParser()
        
        parser.add_argument('amount')
        parser.add_argument('--from', "from_")
        parser.add_argument('--to', "to")

        args = parser.parse_args()

        converter.converter(args.amount, args.from_, args.to)

    except:

        raise SyntaxError("Sorry, your format is wrong. Try use toolkit --help")