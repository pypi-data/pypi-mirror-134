from math import pi
import cairo


def hex_return(dec):
    return str(format(dec, 'x'))


class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, alpha: int = 255):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        self.status = True

    def setColor(self, red: int, green: int, blue: int, alpha: int = 255):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def getColor(self):
        return self.red / 255, self.green / 255, self.blue / 255, self.alpha / 255

    def setStatus(self, status: bool):
        self.status = status

    def getStatus(self):
        return self.status

    def __str__(self):
        str_to_print = f"rgb= ({self.red}, {self.green}, {self.blue}, {self.alpha})\n"
        str_to_print += f"#{hex_return(self.red)}{hex_return(self.green)}{hex_return(self.blue)}"
        return str_to_print


class Drawing:
    def __init__(self, name: str, width: int, height: int, typefile: str):

        if f".{typefile}" not in name:
            name += f".{typefile}"
        if typefile == "svg":
            self.surface = cairo.SVGSurface(name, width, height)
        elif typefile == "png":
            self.surface = cairo.ImageSurface(
                cairo.FORMAT_ARGB32, width, height)

        self.context = cairo.Context(self.surface)
        self.width, self.height = width, height

        # -----------------
        #   set colors
        # -----------------

        self.fill_color = Color(255, 255, 255, 255)
        self.stroke_color = Color()

        # ----------------------------
        #   set default parameters
        # ----------------------------
        self.context.set_font_size(11)
        self.context.select_font_face("Arial",
                                      cairo.FONT_SLANT_NORMAL,
                                      cairo.FONT_WEIGHT_NORMAL)

        self.context.set_line_width(1)
        self.context.set_source_rgba(0, 0, 0, 1)

    """
    -------------------------
            Shapes
    ------------------------    
    """

    def line(self, x_a: float, y_a: float, x_b: float, y_b: float):
        self.setStroke()
        self.context.move_to(x_a, y_a)
        self.context.line_to(x_b, y_b)
        self.context.stroke()

    def square(self, x: float, y: float, length: float):
        self.rect(x, y, length, length)

    def rect(self, x: float, y: float, width: float, height: float):
        self.setStroke()
        self.context.move_to(x, y)
        # doing the rectangle clockwise
        self.context.line_to(x + width, y)
        self.context.line_to(x + width, y + height)
        self.context.line_to(x, y + height)
        self.context.line_to(x, y - self.context.get_line_width() / 2)
        self.setFill()

    def circle(self, x: float, y: float, radius: float):
        self.setStroke()
        self.context.arc(x, y, radius, 0, 2 * pi)

        self.setFill()

    def ellipse(self, x: float, y: float, width: float, height: float):
        print("ellipse are complicated", self.width)
        pass

    def arc(self, x: float, y: float, radius: float, start: float, end: float, radians: bool = True):
        if not radians:
            start = pi / 180 * start
            end = pi / 180 * end

        self.setStroke()
        self.context.arc(x, y, radius, start, end)

        """print(
            f"\t{x = }, \n"
            f"\t{y = }, \n"
            f"\t{radius = }, \n"
            f"\t{start = }, \n"
            f"\t{end = }, \n")"""

        self.setFill()

        pass

    """
    -------------------------
            Text
    ------------------------    
    """

    def text(self, text: str, x: float, y: float):
        self.context.move_to(x, y)
        self.context.show_text(text)
        pass

    def textSize(self, size: int):
        self.context.set_font_size(size)

    def font(self, font_name: str):
        self.context.select_font_face(font_name,
                                      cairo.FONT_SLANT_NORMAL,
                                      cairo.FONT_WEIGHT_NORMAL)

    """
    -------------------------
          attribute
    ------------------------    
    """

    def strokeWeight(self, thickness: float):
        self.context.set_line_width(thickness)

    def stroke(self, red: int, green: int, blue: int, alpha: int = 255):
        self.stroke_color.setColor(red, green, blue, alpha)

    def strokehex(self, hex_color: str):
        hex_color = hex_color.replace("#", "")
        if len(hex_color) == 6:
            colors = [int(hex_color[index:index + 2], 16)
                      for index in range(0, 6, 2)]
            """for index in range(0, 6, 2):
                print(hex_color[index:index + 2])
            print(colors)"""
            self.stroke_color.setColor(*colors, 255)

    def fill(self, red: int, green: int, blue: int, alpha: int = 255):
        self.fill_color.setStatus(True)
        self.fill_color.setColor(red, green, blue, alpha)

    def noFill(self):
        self.fill_color.setStatus(False)

    def setStroke(self):
        self.context.stroke()
        self.context.set_source_rgba(*self.stroke_color.getColor())

    def setFill(self):
        if self.fill_color.getStatus():
            self.context.stroke_preserve()
            self.context.set_source_rgba(*self.fill_color.getColor())
            self.context.fill()
        else:
            self.context.stroke()
