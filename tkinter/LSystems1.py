import turtle

canvas = turtle.Screen()
draw = turtle.Turtle()
draw.speed(1)

instructions = "FFF+F+FF-F+F+FF"

for task in instructions:
    if task == "F":
        draw.forward(90)
    elif task == "+":
        draw.right(90)
    elif task == "-":
        draw.left(90)

input("to exit")