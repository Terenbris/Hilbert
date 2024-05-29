def lsystem(axioms, rules, iterations):
    for i in range(iterations):
        newAxiom = ""

        for axiom in axioms:
            if axiom in rules:
                newAxiom += rules[axiom]
            else:
                newAxiom += axiom
        axioms = newAxiom
    return axioms

def PrintArray(board):
    temp = ""
    w = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if w == 0:
                temp += str(board[x][y])
            elif w == 1:
                if board[x][y] == 0:
                    temp += '^'
                elif board[x][y] == 1:
                    temp += '>'
                elif board[x][y] == 2:
                    temp += 'v'
                elif board[x][y] == 3:
                    temp += '<'
                else:
                    temp += 'X'
            temp += ":"
        temp += "\n"
    print(temp)

rules = { "A" : "+BF-AFA-FB+", "B" : "-AF+BFB+FA-"}
instructions = lsystem("A", rules, 5)
board = [[6 for i in range(32)] for j in range(32)]
direction = 1
x = 0
y = 31
step = 0
print(instructions)
for i in instructions:

    if i == "F":
        step+=1
        if direction == 0:
            y-=1
        elif direction == 1:
            x+=1
        elif direction == 2:
            y+=1
        elif direction == 3:
            x-=1
    elif i == "+":
        direction-=1
    elif i == "-":
        direction+=1
    if direction > 3:
        direction = 0
    elif direction < 0:
        direction = 3

    board[x][y] = step
    

PrintArray(board)