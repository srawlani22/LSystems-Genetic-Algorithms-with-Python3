import turtle # imported turtle library
screen=turtle.Screen() # in order to modify the screen we use the screen function
draw=turtle.Turtle()# a function inorder to call the turtle library
screen.setup(620,620)# sets the size of the screen
screen.bgcolor('black')# sets the background of the screen

draw.pensize(4) # sets the pensize of the turtle pen
draw.shape('turtle')# sets the shape of the turtle
draw.penup()# the turtle moves but doesn't draw anything 
draw.pencolor('red')# since we need gaps between the clock the pen is temporarily 


j=0 #an integer that stores the numbers of the clock


for i in range(12):
      j=j+1# since the clock starts from 0 and not from 1, we increment the values of J
      draw.penup()# the pen is up again because we want gaps between the numbers and the lines
      draw.setheading(-30*i+60)# sets the clock design in the centre and circular motion in the centre
      draw.forward(150) #draws a line forward
      draw.pendown() # the pen is down again
      draw.forward(25) # the turtle goes forward
      draw.penup()# the pen is up and the turtle draws forward again
      draw.forward(20)
      draw.write(str(j),align="center",font=("Arial", 12, "normal"))# the font and style of the  numbers represented the format
      if j==12:# in case the the numbers in the loop go beyond 12 which we certainly don't want in the case of a clock, the value of j is set to 0 again
        j=0
      draw.home()


draw.home()
draw.setpos(0,-250)# set the position of the outlined circle
draw.pendown()# the pen is down again
draw.pensize(10)# we want the outer cirle to be a little more thicker
draw.pencolor('blue') # and we want the color of the pen to be blue to make it lool cool
draw.circle(250) # draws a circle outside the clock


input("")
