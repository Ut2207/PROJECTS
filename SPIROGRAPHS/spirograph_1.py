import datetime
from re import A
import turtle
import math

turtle.speed(0)
turtle.tracer(0)

# Create the turtle
t = turtle.Turtle()
# Cosmetic: make the cursor look like a turtle
step = int(input("STEP DISTANCE (keep below 5): "))
xc = int(input("X coordinate: "))
yc = int(input("Y coordinate: "))
R = int(input("Radius for stationary circle: "))
r = int(input("Radius for moving circle: "))
# Distance of the pen from the center of the moving circle
l = int(input("PEN DISTANCE: "))
# Number of rotations needed for the pattern to close
gcdVal = math.gcd(R, r)
nRot = r // gcdVal
k = float(R) / r
a = 0.0


def restart():
    """Move the turtle to the starting point of the spirograph."""
    t.showturtle()
    t.penup()
    s = 1 + 0.002 * a
    x = s * (R - r) * math.cos(a) + l * math.cos((R - r) * a / r)
    y = s * (R - r) * math.sin(a) - l * math.sin((R - r) * a / r)
    t.setpos(xc + x, yc + y)
    t.pendown()


def draw():
    """Draw the spirograph using the parametric equations."""
    for i in range(0, 1786 * nRot + 1, step):
        s = 1 + 0.002 * a
        x = s * (R - r) * math.cos(a) + l * math.cos((R - r) * a / r)
        y = s * (R - r) * math.sin(a) - l * math.sin((R - r) * a / r)
        t.setpos(xc + x, yc + y)
    t.hideturtle()


def save():
    t.hideturtle()
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    filename = "spiro-" + dateStr
    print("saving drawing to %s.eps/png" % filename)
    canvas = turtle.getcanvas()
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save(filename + ".png", "png")
    turtle.showturtle()
