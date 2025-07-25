"""
Print ansi colored text
"""

from argparse import ArgumentParser
import re
import sys
from typing import NamedTuple

import imageio.v3 as iio

from ansi_art.utils import ansi_image, ansi_color #pylint: disable=import-error

RGB_PATTERN = re.compile(r"rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")

class Args(NamedTuple):
    """
    Args typehint for command line arguments.
    """
    file: str | None
    width: int | None

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
        "--file", '-f',
        type=str,
        help="The image file to display as ANSI art",
        required=False
    )
    parser.add_argument(
        "--width", '-w',
        type=int,
        help=(
            "The width to scale the image to. Each pixel will be represented by 2 characters so if "
            "you can only fit 80 characters in your terminal you should set this to 40"
        ),
        required=False
    )

    parsed = parser.parse_known_args(sys.argv[1:])
    args: Args = parsed[0]
    text = ' '.join(parsed[1])

    file = args.file or text
    width = args.width

    image = iio.imread(file)
    if width is None:
        proceed = input(
            ansi_color(
                f'WARNING no width specified. Use image width {image.shape[1]}? (y/n): ',
                foreground=(255, 212, 0)
            )
        )
        while proceed.lower() not in ('y', 'n'):
            proceed = input(
                ansi_color(
                    'Please enter "y" or "n": ',
                    foreground=(255, 212, 0)
                )
            )
        if proceed.lower() == 'n':
            print(ansi_color(
                'Exiting without printing image...',
                foreground=(255, 32, 57)
            ))
            sys.exit(1)

    print(ansi_image(image, width=width))

if __name__ == "__main__":
    main()
