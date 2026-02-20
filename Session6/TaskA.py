import math as mt
import matplotlib.pyplot as plt
import copy


class Euclidean():

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def Shift(self, C2):
        C1 = self.shape.Centroid()
        shift_x = C2.x - C1.x
        shift_y = C2.y - C1.y
        for i in range(self.shape.nsides):
            self.shape.vertex[i].x += shift_x
            self.shape.vertex[i].y += shift_y


    def MirrorAboutX(self):
        for v in self.shape.vertex:
            v.y *= -1

    def Join(self, obj):
        C1 = self.shape.Centroid()
        C2 = obj.shape.Centroid()
        line = Line(C1, C2)
        line.plot()
        return line

    def Duplicate(self, C2):
        duplicate = copy.deepcopy(self)
        duplicate.Shift(C2)
        return duplicate

class Point():
    def __init__(self, x = '', y = ''):
        self.x = x
        self.y = y
        

class Line():
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2

    def plot(self):
        x = [self.P1.x, self.P2.x]
        y = [self.P1.y, self.P2.y]
        plt.plot(x, y)



class Polygon():
    def __init__(self, nsides = 0, vertex = None):
        self.nsides = nsides
        self.vertex = vertex

    def Perimeter(self):
        perimeter = 0
        for i in range(self.nsides):
            dx = self.vertex[i - 1].x - self.vertex[i].x
            dy = self.vertex[i - 1].y - self.vertex[i].y

            # distance
            perimeter += mt.sqrt(dx ** 2 + dy ** 2)
        return perimeter

    def Area(self):
        area = 0

        for i in range(self.nsides):
            # area += x_i-1 * y_i - x_i * y_i-1
            area += self.vertex[i - 1].x * self.vertex[i].y - self.vertex[i].x * self.vertex[i - 1].y
        return area / 2
    
    def Centroid(self):
        C = Point()
        cx = 0
        cy = 0

        for i in range(self.nsides):
            a = self.vertex[i-1].x * self.vertex[i].y - self.vertex[i].x * self.vertex[i-1].y
            cx += (self.vertex[i-1].x + self.vertex[i].x) * a
            cy += (self.vertex[i-1].y + self.vertex[i].y) * a

        area = self.Area()
        cx = cx / (6 * area)
        cy = cy / (6 * area)
        C.x = cx
        C.y = cy

        return C

    def Plot(self):
        x = []
        y = []

        for i in range(self.nsides):
            x.append(self.vertex[i].x)
            y.append(self.vertex[i].y)

        x.append(x[0])
        y.append(y[0])

        plt.plot(x, y)



rectangle = Euclidean('Rectangle', Polygon(nsides=4))
rectangle.shape.vertex = [Point(2, 8), Point(2, 10), Point(8, 10), Point(8, 8)]
rectangle.shape.Plot()
plt.xlim(-10, 15)
plt.ylim(-15, 15)
    
triangle = Euclidean('Triangle', Polygon(nsides=3))
triangle.shape.vertex = [Point(10, 6), Point(13, 10), Point(14, 6)]
triangle.shape.Plot()


pentagon = Euclidean('Pentagon', Polygon(nsides=5))
pentagon.shape.vertex = [Point(1, 3), Point(6, 4), Point(8, 3), Point(6, 1), Point(2, 3)]
pentagon.shape.Plot()


rectangle.Shift(triangle.shape.Centroid())
rectangle.shape.Plot()

pentagon.MirrorAboutX()
pentagon.shape.Plot()

pentagon.Join(rectangle)

shapes = [rectangle, triangle, pentagon]
for shape in shapes:
    perimeter = shape.shape.Perimeter()
    print(f'the perimeter of the {shape.name} is {perimeter}')

pentagon2 = pentagon.Duplicate(Point(-4, -5))
pentagon2.shape.Plot()

plt.show()