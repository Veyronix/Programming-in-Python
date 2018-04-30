import Shape
import matplotlib.pyplot as plt
import re
import numbers

class JSONParser:
    def __init__(self,json):
        JSONParser._parser(json)
        shapes = []
        self.screen = dict()
        self.palette = dict()

        for i in json["Palette"]:
            self.palette[i] = json["Palette"][i]

        self.screen["width"] = json["Screen"]["width"]
        self.screen["height"] = json["Screen"]["height"]
        self.screen["bg_color"] = JSONParser.return_color(self.palette, json["Screen"]["bg_color"])
        self.screen["fg_color"] = JSONParser.return_color(self.palette, json["Screen"]["fg_color"])

        for i in json["Figures"]:
            type = i["type"]
            if type == "point":
                x = i["x"]
                y = i["y"]
                color = JSONParser.return_color(self.palette,i["color"])
                # w jsonie nie jest napisane ze punkt ma kolor
                shapes.append(Shape.Point(x,y,color))
                pass
            elif type == "polygon":
                points = i["points"]
                color = JSONParser.return_color(self.palette, i["color"])
                shapes.append(Shape.Polygon(points,color))
                pass
            elif type == "rectangle":
                x = i["x"]
                y = i["y"]
                width = i["width"]
                heigth = i["height"]
                color = JSONParser.return_color(self.palette, i["color"])
                shapes.append(Shape.Rectangle(x,y,width,heigth,color))
                pass
            elif type == "square":
                x = i["x"]
                y = i["y"]
                size = 0
                if("size" in i):
                    size = i["size"]
                else:
                    size = i["radius"]/(2**(1/2))
                #     ???
                color = JSONParser.return_color(self.palette, i["color"])
                shapes.append(Shape.Square(x,y,size,color))
                pass
            elif type == "circle":
                shapes.append(Shape.Circle(i["x"],i["y"],i["radius"],color = JSONParser.return_color(self.palette,i["color"])))
            else:
                print("blad!")
                exit(2)

            self.shapes = shapes

    @staticmethod
    def _parser(json):

        if "Figures" not in json or "Screen" not in json or "Palette" not in json:
            raise ValueError("Bad json")

        tmp = json["Screen"]
        if "width" not in tmp or "height" not in tmp or "bg_color" not in tmp or "fg_color" not in tmp:
            raise ValueError("Bad json")
        for i in json["Figures"]:
            type = i["type"]

            if type == "point":
                if "x" not in i or "y" not in i or "color" not in i:
                    raise ValueError("Bad json")
            elif type == "polygon":
                if "points" not in i or "color" not in i:
                    raise ValueError("Bad json")
                pass
            elif type == "rectangle":
                if "x" not in i or "y" not in i or "width" not in i or "height" not in i or "color" not in i:
                    raise ValueError("Bad json")
                pass
            elif type == "square":
                if "x" not in i or "y" not in i or (("size" not in i) == ("radius" not in i)) or "color" not in i:
                    raise ValueError("Bad json")
                pass
            elif type == "circle":
                if "x" not in i or "y" not in i or "radius" not in i:
                    raise ValueError("Bad json")

            else:
                print("Bad json")
                exit(2)

        #     czy sprawdzac Screen i Palette?
        for i in json["Figures"]:
            for j in i:
                if j not in ["color","points","type"]:
                    if not isinstance(i[j], numbers.Integral):
                        print("Argument",j,"isnt number")
                        exit(1)
        # for i in json["Palette"]:
        #     print(i)
        #
        i = json["Screen"]
        if ("width" in i and isinstance(i["width"], numbers.Integral) and "height" in i and "bg_color" in i and "fg_color" in i) is not True:
            print("Bad Screen")
            exit(1)

            # or isinstance(i["x"], numbers.Integral) is not True

    @staticmethod
    def return_color(palette,color):
        if color in palette:
            return JSONParser.return_color(dict(),palette[color])
        elif re.match('^\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$', color):
            print("lol")
            return
        #     change to #coscoscos...
        elif re.match('^#([0-f]{6})',color):
            return color
        else:
            print("Color not in palette or bad kind of color.")
            exit(2)
        pass


    def draw_to_screen(self):
        for i in self.shapes:
            pass
            i.draw()

    def get_screen(self):
        return self.screen

    def get_palette(self):
        return self.palette

    def get_shapes(self):
        return self.shapes



