import argparse
import sys

from . import calculator, converter, errors, history


def help_user():
    print("""
    _____________________________________________________________
    |Toolkit — Command Line Utility                             |
    |Usage:                                                     |
    |    python -m toolkit <command> <arguments>                |
    |AVAILABLE COMMANDS                                         |
    |------------------                                         |
    |calc <expression>                                          |
    |    Calculate a mathematical expression.                   |
    |    Examples:                                              |
    |        python -m toolkit calc "2 + 2"                     |
    |        python -m toolkit calc "(10 + 5) * 2"              |
    |convert <value> --from <unit> --to <unit>                  |
    |    Convert a value from one unit to another.              |
    |    Arguments:                                             |
    |        <value>       Value to convert.                    |
    |        --from        Source unit.                         |
    |        --to          Target unit.                         |
    |    Examples:                                              |
    |        python -m toolkit convert 10 --from km --to miles  |
    |--help                                                     |
    |    Display this help message.                             |
    |    Example:                                               |
    |        python -m toolkit --help                           |
    |EXAMPLES                                                   |
    |--------                                                   |
    |Calculate:                                                 |
    |    python -m toolkit calc "15 * 4"                        |
    |Convert:                                                   |
    |    python -m toolkit convert 100 --from mm --to sm        |
    |Show help:                                                 |
    |    python -m toolkit --help                               |
    |___________________________________________________________|
    """)

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help":

        help_user()

    elif sys.argv[1] == "calc":

        errors.check_expression(sys.argv[2])

        result = calculator.polish_calc(sys.argv[2])
        history.save_history(sys.argv[2], result)
        print(result)

    elif sys.argv[1] == "convert":

        if len(sys.argv) < 5:
            help_user()

        parser = argparse.ArgumentParser()

        parser.add_argument('command')
        parser.add_argument('amount')
        parser.add_argument('--from', dest="from_")
        parser.add_argument('--to', dest="to")

        args = parser.parse_args()

        print(converter.converter(args.amount, args.from_, args.to))

    else:

        help_user()


if __name__ == "__main__":
    main()
