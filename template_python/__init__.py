import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Python Template")
    args = parser.parse_args()
    return args


def main(args):
    print(args)


def cli():
    """Entry point for the application script"""
    args = parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(0)
