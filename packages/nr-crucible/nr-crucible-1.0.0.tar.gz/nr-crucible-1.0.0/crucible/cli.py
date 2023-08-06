"""Console script for crucible."""
import argparse
import logging
import pathlib
import sys

from crucible.calendar import generate_calendar

logging.getLogger('crucible').addHandler(logging.NullHandler())


def main() -> int:
    """Console script for crucible."""
    parser = argparse.ArgumentParser(
        description=(
            'Converts a data csv into a styled Word document.'
        )
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        default=False,
        help='Show debug logging',
    )
    subparsers = parser.add_subparsers()

    # create the subparser for the "calendar" command
    parser_calendar = subparsers.add_parser(
        'calendar',
        description=(
            'Commands for converting a csv into a styled docx'
        )
    )
    parser_calendar.add_argument(
        '-i', '--infile',
        required=True,
        type=argparse.FileType('r'),
        help='The csv data file to be styled (.csv)',
    )
    parser_calendar.add_argument(
        '-o', '--outfile',
        required=True,
        type=pathlib.Path,
        help='Save the styled output to this file (.docx)',
    )

    parser_calendar.set_defaults(func=generate_calendar)
    args = parser.parse_args()

    logging.basicConfig(
        format='%(levelname)s %(name)s: %(message)s',
        level=logging.DEBUG if args.debug else logging.INFO,
    )

    if args.debug:
        logging.debug('DEBUG SET')

    try:
        # Show usage if no cli args found
        args.func(args)
    except AttributeError:
        logging.critical('Invalid cli arguments given')
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
