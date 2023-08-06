from pcairo.cairoP import hex_return
from typing import Union


def hueTRgb(h: Union[int, float],
            s: Union[int, float],
            v: Union[int, float],
            max: tuple = (360, 1, 1)
            ) -> tuple:
    """retun the RGB values of a given hue and saturation and brightness

    Args:
        h (Union[int, float]): hue value                default: 0-360
        s (Union[int, float]): saturation value         default: 0-1
        v (Union[int, float]): vibrance / brightness    default: 0-1
        max (tuple, optional): new range value for h, s ,v . Defaults to (360, 1, 1).

    Returns:
        tuple: rgb value in a tuple
    """
    real_max = (360, 1, 1)
    hsv = [h, s, v]
    for index in range(len(hsv)):
        hsv[index] /= max[index]
        hsv[index] *= real_max[index]
    h, s, v = hsv[0], hsv[1], hsv[2]

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    rgbp = 0, 0, 0
    if 0 <= h < 60:
        rgbp = c, x, 0
    if 60 <= h < 120:
        rgbp = x, c, 0
    if 120 <= h < 180:
        rgbp = 0, c, x
    if 180 <= h < 240:
        rgbp = 0, x, c
    if 240 <= h < 300:
        rgbp = x, 0, c
    if 300 <= h < 360:
        rgbp = c, 0, x

    rgb = (rgbp[0] + m) * 255, (rgbp[1] + m) * 255, (rgbp[2] + m) * 255
    rgb = round(rgb[0]), round(rgb[1]), round(rgb[2])

    return rgb


def DectoHex(nb: int) -> str:
    """convert a decimal value in a hexadecimal string

    Args:
        nb (int): decimal value to convert

    Returns:
        str: hex output in string
    """
    ditcHexDec = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D",
                  14: "E",
                  15: "F"}
    hexversion = ""
    hexlist = []
    if nb < 16:
        hexlist.append(0)
    while nb >= 16:
        hexlist.append(ditcHexDec[nb % 16])
        nb = int(nb / 16)
    hexlist.append(ditcHexDec[nb])

    for loop in range(len(hexlist) - 1, -1, -1):
        hexversion += str(hexlist[loop])
    return hexversion


def rgbToHex(r: int, g: int, b: int, a: int = None) -> str:
    """convert rgbs values to hex #rrggbb or #rrggbbaa 

    Args:
        r (int): red 0-255
        g (int): green 0-255
        b (int): blue 0-255
        a (int, optional): alpha / trancparency 0-255

    Returns:
        str: hex value of rgb
    """
    str = "#"
    str += hex_return(r)
    str += hex_return(g)
    str += hex_return(b)
    if a is not None:
        str += hex_return(a)
    return str


def main():
    r, g, b = hueTRgb(0, 0, 0.75)
    print(hueTRgb(201, 88, 89, (360, 100, 100)))


if __name__ == '__main__':
    main()
