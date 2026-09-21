import argparse
import sys

from . import calculator, converter, errors


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


if len(sys.argv) < 2 or sys.argv[1] == "--help":

    help_user()

elif sys.argv[1] == "calc":

    result_og_checking = errors.check_expretion(sys.argv[2])

    if result_og_checking != 1:

        raise SyntaxError(result_og_checking)

    print(calculator.polish_calc(sys.argv[2]))

elif sys.argv[1] == "converter":

    if len(sys.argv) < 5:
        help_user()

    parser = argparse.ArgumentParser()

    parser.add_argument('amount')
    parser.add_argument('--from', dest="from_")
    parser.add_argument('--to', dest="to")

    args = parser.parse_args()

    converter.converter(args.amount, args.from_, args.to)

else:

    help_user()
