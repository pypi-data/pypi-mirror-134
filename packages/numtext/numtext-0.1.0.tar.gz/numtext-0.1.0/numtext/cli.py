"""Console script for numtext."""
import argparse
import sys

import numtext


def main():
    """Console script for numtext."""
    parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    parser.add_argument('number', type=str)
    parser.add_argument('--capitalize', default=False, action="store_true")
    args = parser.parse_args()

    text = numtext.convert(args.number)
    print(args.number)


    # print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into numtext.cli.main" + "text")
    print(text)
    print(args.capitalize)
    return 0


if __name__ == "__main__":
    sys.exit(main())
