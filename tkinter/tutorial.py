import turtle 
import time
import math
#from turtleLS import randint

draw = turtle.Turtle()

# # drawing a square
# draw.forward(100)
# draw.right(90)
# draw.forward(100)
# draw.right(90)
# draw.forward(100)
# draw.right(90)
# draw.forward(100)

# # time.sleep(3)
# # draw.reset()

# draw.penup()
# draw.forward(100)
# draw.pendown()







# Another design- draws a fancy star graph using recursion in Python.
pickachu = turtle.Turtle()
screen = turtle.Screen()
pickachu.pencolor("white")


pickachu.getscreen().bgcolor("black")
# r = randint(0,255)
# g = randint(0,255)
# b = randint(0,255)

# screen.colormode(255)
# draw.pencolor(r,g,b)


# for i in range(5):
#     pickachu.forward(200)
#    pickachu.left(216)

pickachu.speed(0)
pickachu.penup()
pickachu.goto((-200,100))
pickachu.pendown()






def starGraph(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            pickachu.forward(size)
            starGraph(turtle, size/3)
            pickachu.left(216)
            turtle.end_fill()

starGraph(pickachu,360)
turtle.done()