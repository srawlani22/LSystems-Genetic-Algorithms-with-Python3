import turtle
# So python has a turtle library that helps us in using the defined methods of the library that further help us in drawing L.

canvas = turtle.Screen()
#opens the canvas/screen so that we can draw the alphabet

draw = turtle.Turtle()
# starts drawing the file

draw.speed(1)
draw.left(90)

instructions = "FFF+F+FF-F+F+FF-fff"


for task in instructions:
    if task == "F":
        draw.forward(90)
    elif task == "+":
        draw.right(90)
    elif task == "-":
        draw.left(90)

input("")
    

