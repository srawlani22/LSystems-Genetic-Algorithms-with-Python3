import turtle 
screen=turtle.Screen()
draw=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
draw.pensize(4)
draw.shape('turtle')
draw.penup()
draw.pencolor('red')
j=0


for i in range(12):
      j=j+1
      draw.penup()
      draw.setheading(-30*i+60)
      draw.forward(150)
      draw.pendown()
      draw.forward(25)
      draw.penup()
      draw.forward(20)
      draw.write(str(j),align="center",font=("Arial", 12, "normal"))
      if j==12:
        j=0
      draw.home()


draw.home()
draw.setpos(0,-250)
draw.pendown()
draw.pensize(10)
draw.pencolor('blue')
draw.circle(250)
draw.penup()
draw.setpos(150,-270)

input("")
