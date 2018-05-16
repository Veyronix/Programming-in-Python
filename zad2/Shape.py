import matplotlib.patches as plt


class Shape(object):
    def __init__(self):
        pass

    def add_shape(self, fig):
        pass


class Square(Shape):
    def __init__(self, x, y, size, color):
        self.square = plt.Rectangle((x, y), size, size, facecolor=color)

    def add_shape(self, fig):
        fig.artists.append(self.square)


class Circle(Shape):
    def __init__(self, x, y, radius, color):
        self.circle = plt.Circle((x, y), radius=radius, facecolor=color)

    def add_shape(self, fig):
        fig.artists.append(self.circle)
        return self.circle


class Polygon(Shape):
    def __init__(self, points, color):
        self.polygon = plt.Polygon(points, facecolor=color)

    def add_shape(self, fig):
        fig.artists.append(self.polygon)


class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        self.rectangle = plt.Rectangle((x, y), width, height, facecolor=color)

    def add_shape(self, fig):
        fig.artists.append(self.rectangle)


class Point(Shape):
    def __init__(self, x, y, color):
        self.point = plt.Circle((x, y), 1, transform=None, color=color)

    def add_shape(self, fig):
        fig.artists.append(self.point)
