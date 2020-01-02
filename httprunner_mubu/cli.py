import argparse
import sys

from httprunner_mubu.runner import run_yaml


def main():
    """ API test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description="hogwarts httprunner")
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version")
    parser.add_argument(
        'yaml_path',
        help="yaml file path")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        # no argument passed
        parser.print_help()
        return 0
    print("testpath---",args.yaml_path)
    success = run_yaml(args.yaml_path)
    return success


if __name__ == '__main__':
    main()