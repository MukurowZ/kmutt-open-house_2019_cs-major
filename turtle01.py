import turtle
import math

def drawStar(x):
    turtle.seth(252)
    for a in range(5):
        turtle.fd(x)
        turtle.right(72)
        turtle.fd(x)
        turtle.left(144)
        
def centeredCircle(x):
    turtle.up()
    a=turtle.pos()
    turtle.setpos(a[0],a[1]+(x))
    turtle.seth(180)
    turtle.down()
    turtle.circle(x)
    turtle.up()
    turtle.setpos(a[0],a[1])
    turtle.down()

def centeredStar(x):
    length = (x/math.sin(math.radians(126)))*(math.sin(math.radians(36)))
    turtle.up()
    pos = turtle.pos()
    turtle.setpos(pos[0],pos[1]+x)
    turtle.down()
    drawStar(length)
    turtle.up()
    turtle.setpos(pos[0],pos[1])
    turtle.down()

def dragonball_3():
    turtle.color("#FF9933")
    turtle.begin_fill()
    centeredCircle(100)
    turtle.end_fill()
    
    turtle.color("#FFCC00")
    turtle.begin_fill()
    centeredCircle(90)
    turtle.end_fill()
    pos = turtle.pos()
    turtle.setpos(pos[0]-5,pos[1]-5)
    
    turtle.color("#FF9933")
    turtle.begin_fill()
    centeredCircle(90)
    turtle.end_fill()
    
    turtle.color("#FF4500")
    turtle.up()
    pos = turtle.pos()
    turtle.setpos(pos[0]-40,pos[1]+70)
    turtle.down()
    turtle.begin_fill()
    drawStar(15)
    turtle.end_fill()

    turtle.up()
    pos = turtle.pos()
    turtle.setpos(pos[0]+50,pos[1]-110)
    turtle.down()
    turtle.begin_fill()
    drawStar(15)
    turtle.end_fill()

    turtle.up()
    pos = turtle.pos()
    turtle.setpos(pos[0]+30,pos[1]+80)
    turtle.down()
    turtle.begin_fill()
    drawStar(15)
    turtle.end_fill()

turtle.showturtle()
turtle.speed(9)
turtle.shape("turtle")
dragonball_3()
