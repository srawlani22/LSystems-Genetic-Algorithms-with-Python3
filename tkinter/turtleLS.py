import turtle
from random import randint
# So python has a turtle library that helps us in using the defined methods of the library that further help us in drawing L.

canvas = turtle.Screen()
#opens the canvas/screen so that we can draw the alphabet

draw = turtle.Turtle()
# starts drawing the file


draw.pensize(4)
draw.speed(3)

screen = turtle.Screen()


#design 1- draws a star

draw.color('red', 'yellow')
draw.begin_fill()
while True:
        draw.forward(250)
        draw.left(220)
        if abs(draw.pos()) < 1:
            break
draw.end_fill()


draw.reset()

draw.pensize(2)
draw.speed(0)

# design 2- draws a multicolor spiral design 
x = 1

while x < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    screen.colormode(255)
    draw.pencolor(r,g,b)

    draw.fd(50+x)
    draw.rt(90.911)

    x = x+1


input("")