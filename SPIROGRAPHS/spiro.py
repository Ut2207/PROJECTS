import math
import turtle
turtle.tracer(0)

def drawcircle(x,y,r):
    turtle.up()
    turtle.setpos(x+r,y)
    turtle.down()

    for i in range(0,360,1):
        a=math.radians(i)
        turtle.setpos(x+r*math.cos(a),y+r*math.sin(a))
x_axis=int(input("enter the abscissa for the centere of the circle : "))
y_axis=int(input("enetr the oordinate for thr sentere of the circle : "))
radius=int(input("enter the radius of the circle : "))
for i in range(100):
    drawcircle(x_axis,y_axis,radius)
    radius+=3
    x_axis+=5
    y_axis+=5
turtle.update()
turtle.done()

