import math
import turtle

turtle.tracer(0)
turtle.speed(0)
turtle.bgcolor("black")


def drawcircle(x, y, r, c):
    turtle.pencolor(c)
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(360):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


x = -300
y = -300
r = 5

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]

for i in range(300):
    drawcircle(x, y, r, colors[i % len(colors)])
    r = 200
    x += 20
    y += 20

turtle.update()
turtle.done()
