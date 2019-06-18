def Lsystem_Rules(inputEx):
    outputEx = ""
    if inputEx == 'A':
        outputEx = 'B'   # Rule 1
    elif inputEx == 'B':
        outputEx = 'AB'  # Rule 2
    else:
        outputEx = inputEx    # no rules apply so keep the character

    return outputEx


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + Lsystem_Rules(ch)

    return newstr


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


for i in range(10):
    print(createLSystem(i, "A"))


