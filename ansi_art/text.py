"""
Print ansi colored text
"""

from argparse import ArgumentParser
import re
import sys
from typing import NamedTuple

from ansi_art.utils import ansi_color #pylint: disable=import-error

RGB_PATTERN = re.compile(r"rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")

class Args(NamedTuple):
    """
    Args typehint for command line arguments.
    """
    text: str
    foreground: str | None
    background: str | None

def main():
    """
    Print ANSI colored text based on command line arguments.
    Usage:
        python print.py [<options>] "Your text here"
    Options:
        --foreground, -f <color>   Set the foreground color (e.g., 12, rgb(1, 2, 3))
        --background, -b <color>   Set the background color (e.g., 6, rgb(4, 5, 6))
    """
    parser = ArgumentParser(description="Print ANSI colored text")
    parser.add_argument(
        "--foreground", '-f',
        type=str,
        help="Foreground color code or rgb value (e.g., 12, rgb(1, 2, 3))",
        required=False
    )
    parser.add_argument(
        "--background", '-b',
        type=str,
        help="Background color (e.g., 6, 'rgb(4, 5, 6)')",
        required=False
    )

    parsed = parser.parse_known_args(sys.argv[1:])
    args: Args = parsed[0]
    text = ' '.join(parsed[1])

    # Validate foreground
    if args.foreground is not None:
        match = RGB_PATTERN.match(args.foreground)
        if match:
            foreground = tuple(int(c) for c in match.groups())
        else:
            try:
                foreground = int(args.foreground)
            except ValueError:
                raise ValueError(f"Invalid foreground color: {args.foreground}") from None
    else:
        foreground = None

    # Validate background
    if args.background is not None:
        match = RGB_PATTERN.match(args.background)
        if match:
            background = tuple(int(c) for c in match.groups())
        else:
            try:
                background = int(args.background)
            except ValueError:
                raise ValueError(f"Invalid background color: {args.background}") from None
    else:
        background = None

    print(ansi_color(text, foreground=foreground, background=background))

if __name__ == "__main__":
    main()
