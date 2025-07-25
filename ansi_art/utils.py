"""
ANSI Printing Utilities
"""

from PIL import Image
import numpy as np

def ansi_color(
    text: str,
    *,
    foreground: int | tuple[int, int, int] | None = None,
    background: int | tuple[int, int, int] | None = None,
    clear_sequence: str = "\033[0m"
) -> str:
    """
    Return ANSI colored text.

    Args:
        text (str): The text to color.
        foreground (int | tuple[int, int, int] | None): Foreground color as an RGB tuple or
            256-color code.
        background (int | tuple[int, int, int] | None): Background color as an RGB tuple or
            256-color code.
        clear_sequence (str): ANSI sequence to reset colors.
    """
    # Get foreground color code
    if foreground is None:
        foreground_code = ''
    elif isinstance(foreground, int):
        foreground_code = f'\033[38;5;{foreground:03}m'
    elif isinstance(foreground, tuple):
        r, g, b = foreground
        foreground_code = f'\033[38;2;{r};{g};{b}m'
    else:
        raise ValueError(
            f'Unexpected value "{foreground}" for foreground color must be an int or RGB tuple'
        )

    # Get background color code
    if background is None:
        background_code = ''
    elif isinstance(background, int):
        background_code = f'\033[48;5;{background:03}m'
    elif isinstance(background, tuple):
        r, g, b = background
        background_code = f'\033[48;2;{r};{g};{b}m'
    else:
        raise ValueError(
            f'Unexpected value "{background}" for background color must be an int or RGB tuple'
        )

    # Combine codes and text
    return f"{foreground_code}{background_code}{text}{clear_sequence}"


def ansi_image(image: np.ndarray, *, width: int | None = None) -> str:
    """
    Convert an image to an ANSI printable format

    Args:
        iamge (np.ndarray): The image to convert.
        width (int | None): The width to scale the image to or None to use the original width.

    Returns:
        str: ANSI formatted string representing the image.
    """
    if image.ndim != 3:
        raise ValueError("Image must be a 3D array (height, width, channels)")
    if image.shape[2] != 3:
        raise ValueError("Image must have 3 channels (RGB)")

    if width is not None:
        height = int(image.shape[0] * (width / image.shape[1]))
        image = np.array(Image.fromarray(image).resize((width, height)))

    # Convert to ANSI escape codes
    ansi_str = ''
    for row in image:
        ansi_row = ''.join(
            ansi_color('  ', background=(r, g, b)) for r, g, b in row
        )
        ansi_str += ansi_row + '\n'

    return ansi_str
