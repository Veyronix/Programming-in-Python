import Shape
import re
import numbers


class JSONParser:
    def __init__(self, json):
        if JSONParser._parser(json) == 1:
            raise ValueError("Bad json")
        shapes = []
        self.screen = dict()
        self.palette = dict()

        for i in json["Palette"]:
            self.palette[i] = JSONParser.return_color(dict(), json["Palette"][i])

        self.screen["width"] = json["Screen"]["width"]
        self.screen["height"] = json["Screen"]["height"]
        self.screen["bg_color"] = JSONParser.return_color(self.palette, json["Screen"]["bg_color"])
        self.screen["fg_color"] = JSONParser.return_color(self.palette, json["Screen"]["fg_color"])

        for i in json["Figures"]:
            type = i["type"]
            if type == "point":
                if "color" in i:
                    color = JSONParser.return_color(self.palette, i["color"])
                else:
                    color = self.screen["fg_color"]
                shapes.append(Shape.Point(i["x"], i["y"], color))
            elif type == "polygon":
                if "color" in i:
                    color = JSONParser.return_color(self.palette, i["color"])
                else:
                    color = self.screen["fg_color"]
                shapes.append(Shape.Polygon(i["points"], color))
            elif type == "rectangle":
                if "color" in i:
                    color = JSONParser.return_color(self.palette, i["color"])
                else:
                    color = self.screen["fg_color"]
                shapes.append(Shape.Rectangle(i["x"], i["y"], i["width"], i["height"], color))
            elif type == "square":
                if "color" in i:
                    color = JSONParser.return_color(self.palette, i["color"])
                else:
                    color = self.screen["fg_color"]
                shapes.append(Shape.Square(i["x"], i["y"], i["size"], color))
            elif type == "circle":
                if "color" in i:
                    color = JSONParser.return_color(self.palette, i["color"])
                else:
                    color = self.screen["fg_color"]
                shapes.append(
                    Shape.Circle(i["x"], i["y"], i["radius"], color=color))
            else:
                print("Bad type of figure")
                raise ValueError("Bad type of figure")

        self.shapes = shapes

    @staticmethod
    def _parser(json):
        if "Figures" not in json or "Screen" not in json or "Palette" not in json:
            print("Bad json")
            return 1
        tmp = json["Screen"]
        if "width" not in tmp or "height" not in tmp or "bg_color" not in tmp or "fg_color" not in tmp:
            print("Bad json")
            return 1
        for i in json["Figures"]:
            type = i["type"]
            if type == "point":
                if "x" not in i or "y" not in i:
                    return 1
            elif type == "polygon":
                if "points" not in i or "color" not in i:
                    return 1
            elif type == "rectangle":
                if "x" not in i or "y" not in i or "width" not in i or "height" not in i:
                    return 1
            elif type == "square":
                if "x" not in i or "y" not in i or (("size" not in i) == ("radius" not in i)):
                    return 1
            elif type == "circle":
                if "x" not in i or "y" not in i or "radius" not in i:
                    return 1

            else:
                return 1
        for i in json["Figures"]:
            for j in i:
                if j not in ["color", "points", "type"]:
                    if not isinstance(i[j], numbers.Integral):
                        print("Argument", j, "isn't number")
                        return 1
                elif j in ["color", "type"]:
                    if not isinstance(i[j], str):
                        print("Argument", j, "isn't string")
                        return 1

        i = json["Screen"]
        if not ("width" in i and isinstance(i["width"],
                                            numbers.Integral) and "height" in i and isinstance(i["height"],
                                                                                               numbers.Integral) and "bg_color" in i and "fg_color" in i):
            print("Bad Screen")
            return 1

    @staticmethod
    def return_color(palette, color):
        if color in palette:
            return palette[color]
        if not (isinstance(color, str) and len(color) > 0 and (color[0] == "#" or color[0] == "(")):
            print("Bad kind format of color")
            return 1
        elif re.match('^\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$', color):
            m = re.findall('(\d{1,3})', color)
            if not (0 <= int(m[0]) <= 255 and 0 <= int(m[1]) <= 255 and 0 <= int(m[2]) <= 255):
                print("Bad size of color")
                return 1
            r = str(hex(int(m[0])).split('x')[-1])
            g = str(hex(int(m[1])).split('x')[-1])
            b = str(hex(int(m[2])).split('x')[-1])
            if len(r) != 2:
                r = "0" + r
            if len(g) != 2:
                g = "0" + g
            if len(b) != 2:
                b = "0" + b
            return "#" + r + g + b
        elif re.match('^#([0-f]{6})', color):
            return color
        else:
            print("Color not in palette or bad kind of color.")
            return 1

    def get_screen(self):
        return self.screen

    def get_palette(self):
        return self.palette

    def get_shapes(self):
        return self.shapes
