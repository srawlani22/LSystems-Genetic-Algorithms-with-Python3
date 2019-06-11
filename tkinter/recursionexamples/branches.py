import turtle 


def tree(branchLength,branch):
    #branch= turtle.Turtle()
    if branchLength >10:
        branch.forward(branchLength)
        branch.right(20)
        tree(branchLength-15 , branch)
        branch.left(40)
        tree(branchLength-15, branch)
        branch.right(20)
        branch.right(branchLength)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    screen.exitonclick()

main()


