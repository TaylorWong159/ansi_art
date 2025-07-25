# ANSI Art
Print text and images using ANSI escape codes

## ANSI Text
Print text colored using ANSI escape codes

### Usage

```bash
ansi_text [-h] [--foreground FOREGROUND] [--background BACKGROUND] [TEXT]
```
- **--help, -h** Print the help screen
- **--foreground, -f** The foreground color either as an ANSI 256 color code (0-255) or as an rgb value (rgb(0-255, 0-255, 0-255))
- **--background, -b** The background color either as an ANSI 256 color code (0-255) or as an rgb value (rgb(0-255, 0-255, 0-255))
- **TEXT** The text to print


## ANSI Image
Print an image to the console colored using characters and ANSI escape codes

### Usage

```bash
ansi_image [-h] [--file FILE] [--width WIDTH] [TEXT]
```
- **--help, -h** Print the help screen
- **--file, -f** The image file to display
- **--width, -w** The width in pixels to down sample to
