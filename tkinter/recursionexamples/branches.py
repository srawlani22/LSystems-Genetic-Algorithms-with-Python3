#referred from: https://interactivepython.org/runestone/static/pythonds/Recursion/pythondsintro-VisualizingRecursion.html


import turtle 

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()

#the nature is not as symmetric as a computer programe that's why you will notice that these designs don't really look realistic even though L-Systems
# were supposed to create natural symmetrical stuff however this only the beginning of things and stuff gets complicated as we move forward.

