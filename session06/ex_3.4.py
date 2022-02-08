import turtle
import math

leo = turtle.Turtle()
print(leo)

def all_spirals(t, n, length, a, b): #Got the code from: https://github.com/AllenDowney/ThinkPython2/blob/master/code/spiral.py
    """Draws an Archimedian spiral starting at the origin.
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)
    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta

all_spirals(leo, 10000, 3, 0.1, 0.0002)

turtle.mainloop()

