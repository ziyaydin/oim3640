class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        """return a Point instance in a human-readable format"""
        return f'({self.x}, {self.y})'


point1 = Point(3, 4)
# create an instance of Point with two arguments for its attributes x and y
print(point1)

point2 = Point()