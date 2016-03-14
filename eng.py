import turtle

#Functions to draw screen

def drawShape(x, y, sides, dist):
    turtle.setpos(x , y)
    angle = 360/sides
    for i in range (sides):
        turtle.forward(dist)
        turtle.right(angle)

def clear():
    turtle.clear()

def rendSpeed(speed):
    turtle.speed(speed)

def setColour(colour):
    turtle.color(str(colour))

#Broken commands bellow. Please edit for it to work.

def setBackgroundPic(image):
    turtle.bgpic(str(image))

def setBackgroundColour(colour):
    turtle.bgcolor(str(image))
