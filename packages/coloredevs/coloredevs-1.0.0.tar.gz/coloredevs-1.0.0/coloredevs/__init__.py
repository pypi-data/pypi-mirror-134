"""
String Colorizer for text printed on the terminal.

Author: JohnLesterDev
"""

def colorize(text:str, rgb:list) -> str:
    r, g, b = rgb
    colored_txt = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    return colored_txt

def rgb_to_hex(rgb:list) -> str:
    r, g, b = rgb
    return "#{:X}{:X}{:X}".format(r, g, b)

def hex_to_rgb(hex:str) -> tuple:
    rgb = []

    for i in range(0, 2, 4):
        dec = int(hex[i:i+2], 16)
        rgb.append(dec)

    return tuple(rgb)

RED = [255, 0, 0]
ORANGE = [255, 128, 0]
YELLOW = [255, 255, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
