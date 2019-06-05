import turtle
# So python has a turtle library that helps us in using the defined methods of the library that further help us in drawing L.

canvas = turtle.Screen()
#opens the canvas/screen so that we can draw the alphabet

draw = turtle.Turtle()
# starts drawing the file

draw.speed(1)
# we set a drawing speed

draw.left(90)
# to make a straight L, I had to start the drawing from the Y-axis since it was set to X-axis by default

instructions = "FFF+F+FF-F+F+FF"
#instructions/L-system rules to draw an L

for task in instructions: #a for loop iterates through the instructions and draw an l based on the simple Lsystem rules which can be figured out by the if and else if statements below
    if task == "F":
        draw.forward(90)
    elif task == "+":
        draw.right(90)
    elif task == "-":
        draw.left(90)

input("to exit")
#a manual exit command so the GUI screen doesn't close as soon as the program finishes drawing the L.
