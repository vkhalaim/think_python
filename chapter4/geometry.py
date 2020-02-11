from turtle import Turtle
from math import pi


def polyline(t, n, length, angle):
    """ Draws n segments line with the given length 
    and angle in degrees between them.
    t: Turtle
    n: segments in polyline
    length: length of the segment
    angle: angle (degrees) between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """ Draws n sides polygon with the given length 
    and angle in degrees between them.
    t: Turtle
    n: sides
    length: length of the side
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """ Draws arc with given radius - r and angle in degrees.
    t: Turtle
    r: radius of the arc
    angle: angle (degrees) for arc
    """
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    """ Draws circle with given radius - r.
    t: Turtle
    r: radius of the circle
    """
    arc(t, r, 360)

def petal(t, r, angle):
    """
    Draws a petal using two arcs.
    t: Turtle
    r: radius of the arc
    angle: angle (degrees) for arc
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, length):
    pass

bob = Turtle()

petal(bob, 10, 120)