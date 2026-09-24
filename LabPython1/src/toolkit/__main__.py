import argparse
import sys

from . import calculator, converter, history


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
    |     Kinds of operation that are possible                  |
    |         + plus                                            |
    |         - minus                                           |
    |         * multiply                                        |
    |         / divide                                          |
    |         ++ unary plus                                     |
    |         -- unary minus                                    |
    |         % mod                                             |
    |         // integer division                               |
    |convert <value> --from <unit> --to <unit>                  |
    |    Convert a value from one unit to another.              |
    |    Arguments:                                             |
    |        <value>       Value to convert.                    |
    |        --from        Source unit.                         |
    |        --to          Target unit.                         |
    |    Examples:                                              |
    |        python -m toolkit convert 10 --from km --to mm     |
    |    Allows:                                                |
    |        km: kilometer                                      |
    |        m: meter                                           |                
    |        dm: decimeter                                      |
    |        cm: centimeter                                     |
    |        mm: millimeter                                     |
    |        kg: kilogram                                       |
    |        g: gram                                            |
    |        c: celsius                                         |
    |        k: kelvin                                          |
    |        f: fahrenheit                                      |
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
    return 0


def main():
    """The Main function. Launch when user write toolkit. With this function
    Python launch all tools. Also return errors and manage history."""
    if len(sys.argv) < 3 or sys.argv[1] == "--help":
        help_user()

    elif sys.argv[1] == "calc":
        try:
            result = calculator.polish_calc(sys.argv[2])
            print(result)
            history.save_history(sys.argv[2], result)
            return 0

        except (SyntaxError, ValueError, ZeroDivisionError) as error:
            print(error, file=sys.stderr)
            return 2

    elif sys.argv[1] == "convert":
        if len(sys.argv) < 5:
            help_user()

        parser = argparse.ArgumentParser()

        parser.add_argument("command")
        parser.add_argument("amount")
        parser.add_argument("--from", dest="from_")
        parser.add_argument("--to", dest="to")

        args = parser.parse_args()

        try:
            result = converter.converter(args.amount, args.from_, args.to)
            print(result)
            return 0

        except (ValueError, ZeroDivisionError) as error:
            print(error, file=sys.stderr)
            return 2

    else:
        help_user()


if __name__ == "__main__":
    sys.exit(main())
