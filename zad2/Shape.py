import matplotlib.pyplot as plt

class Shape(object):
    def __init__(self):
        pass

    def draw(self):
        pass

    def draw_to_screen(self):
        pass

class Square(Shape):
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.square = plt.Rectangle((x, y), size, size,facecolor=color)
        pass

    def draw(self):
        pass
        # print(self.x)

    def draw_to_screen(self):
        pass

    def get_shape(self,ax):
        ax.add_patch(self.square)
        # return self.square


class Circle(Shape):
    def __init__(self,x,y,radius,color):
        # self.x = x
        # self.y = y
        # self.radius = radius
        self.circle = plt.Circle((x, y), radius=radius,facecolor=color)

    def draw(self):
        pass

    def draw_to_screen(self):
        pass

    def get_shape(self,ax):
        ax.add_patch(self.circle)
        return self.circle

class Polygon(Shape):
    def __init__(self,points,color):
        # self.points = points
        # self.color = color
        self.polygon = plt.Polygon(points,facecolor=color)
        pass

    def draw(self):
        print("hejo2")

    def draw_to_screen(self):
        pass

    def get_shape(self,ax):
        ax.add_patch(self.polygon)
        # return self.polygon


class Rectangle(Shape):
    def __init__(self,x,y,widht,heigth,color):
        self.x = x
        self.y = y
        self.widht = widht
        self.heigth = heigth
        self.color = color
        self.rectangle = plt.Rectangle((x,y),widht,heigth,facecolor=color)

        pass

    def draw(self):
        print("hejo3")

    def draw_to_screen(self):
        pass

    def get_shape(self,ax):
        ax.add_patch(self.rectangle)
        # return self.rectangle


class Point(Shape):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.point = plt.Circle((x, y), radius=10,facecolor=color)

        pass

    def draw(self):
        print("hejo4")

    def draw_to_screen(self):
        pass


    def get_shape(self,_):
        plt.scatter([self.x], [self.y], color=self.color,zorder=10)
        pass


