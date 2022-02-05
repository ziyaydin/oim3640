import turtle
import math

leo = turtle.Turtle()
print(leo)

# Exercise 1

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# for i in range(4):
#     print('Hello!')

# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)

# Excersie 2.1


def square(t):
    """This function takes a parameter named t, which is a turtle. 
    It should use the turtle to draw a square"""
    for i in range(4):
        t.fd(100)
        t.lt(90)

# square(leo)

# raphael = turtle.Turtle()
# square(raphael)

# Excersie 2.2


def square_2(t, lenght):
    """This function takes a parameter named t, which is a turtle and add another parameter length which is a float. 
    It should use the turtle to draw a square with side length"""
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

# square_2(leo, 300)

# Exercise 2.3


def polygon(t, lenght, n):
    """Draws an n-sided polygon"""
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)

# polygon(leo, 50, 20)
# polygon(t=leo, lenght=50, n=20)

# Exercise 2.4


def circle(t, r):
    """Draws and approximates circle"""
    circumference = 2 * math.pi * r
    length = circumference / 100
    polygon(t, length, 100)

# circle(leo, 200)

# Exercise 2.5


def arc(t, r, angle):
    """draws an arc with angle"""
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3)+1
    step_lenght = arc_length/n
    step_angle = angle/n

    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)

# arc(leo, 200, 90)
# arc(leo, 200, 360)
# arc(leo, 100, 180)


def polyline(t, n, length, angle):
    """Drwas n line segments with given length and angle between them.
    t is a turtle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polyline(leo, n=4, length=100, angle=60)


def polygon(t, length, n):  # Better way to draw polygon
    """Draw a n-sided polygon with given lengt.h
    t is a turtle"""
    angle = 360 / n
    polyline(t, n, length, angle)

# polygon(leo, 200, 4)


def arc(t, r, angle):  # Better version to draw arc
    """draws an arc with radius r and angle.
    t is a turtle """
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_lenght = arc_length/n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)

# arc(leo, 100, 180)


def circle(t, r):  # Better version to draw circle
    """Draw a circle with radius.
    t is a turtle"""
    arc(t, r, 360)

# circle(leo, 70)

# Exercise 3.1


# Got help from: https://www.geeksforgeeks.org/circle-of-squares-using-python/
def fancy_squares(t, lenght, n, q):
    """This function creates n squares and turning right q degrees after each square.
    t is a turtle"""
    for i in range(n):
        for j in range(4):
            t.fd(lenght)
            t.rt(90)
        t.rt(q)
# fancy_squares(leo, 100, 60, 5)

# Exercise 3.2


def even_fancier_squares(t, n, q, z):
    """This function creates n squares,
    q degrees turn right after each square 
    z units bigger in each square and starting with 30 length.
    t is a turtle"""
    length = 30
    for i in range(n):
        for j in range(4):
            t.fd(length)
            t.rt(90)
        length += z
        t.rt(q)

# even_fancier_squares(leo, 60, 5, 4)


# Exercise 3.3
def fancy_stars(t, n, q, z):
    """This function creates n stars,
    q degrees turn right after each stars 
    z units bigger in each square and starting with 30 length.
    t is a turtle"""
    length = 30
    for i in range(n):
        for j in range(5):
            t.fd(length)
            t.rt(144)
        length += z
        t.rt(q)

# fancy_stars(leo, 60, 5, 4)

# Exercise 3.4


def spiral(t, lenght, s):  # Got help from: https://dev.to/taarimalta/how-to-draw-a-spiral-with-python-turtle-2n5c
    """This function creates spirals
    s is the degree of one interior angle of the shape we want
    t is a turtle"""
    for i in range(360):
        t.fd(i)
        t.rt(s)

# spiral(leo, 30, 60)


turtle.mainloop()
