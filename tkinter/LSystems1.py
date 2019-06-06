import turtle

canvas = turtle.Screen()
draw = turtle.Turtle()
draw.speed(1)
draw.left(90)

# instructions = "FFF+F+FF-F+F+FF-fff"
instructions= "fffff"

for task in instructions:
    # if task == "F":
    #     draw.forward(90)
    # elif task == "+":
    #     draw.right(90)
    # elif task == "-":
    #     draw.left(90)
    if task == "f":
        draw.ondrag(90)

input("")