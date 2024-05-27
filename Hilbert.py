def CreateArray(size):
    board = [[[0,0] for i in range(size)] for j in range(size)]
    CreateQuadrant(size, 0)
    PrintArray(board)

def PrintArray(board):
    temp = ""
    for y in range(len(board)):
        for x in range(len(board[0])):
            temp += str(board[x][y][0])
        temp += "\n"
    print(temp)

def CreateQuadrant(height, dir):
    wh = height/2 
    for i in range(2):
        for j in range(2):
            if dir == 0:
                wd = ((i*3)-(i*j*3))+(i*j)
            elif dir == 1:
                wd = j+((i*2)-(i*j*2))
            elif dir == 2:
                wd = 3-(j*2)-i+(i*j*2)
            elif dir == 3:
                wd = 3-(j*3)+(i*j*2)

    if wh < 2:
        return
    else:
        CreateQuadrant(wh, wd)

def Menu():
    CreateArray(4)

Menu()