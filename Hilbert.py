def CreateArray(size):
    board = [[[0,0] for i in range(size)] for j in range(size)]
    board = CreateQuadrant(0, 0, size, 0, board)
    PrintArray(board)

def PrintArray(board):
    temp = ""
    w = 1
    z = 1
    for y in range(len(board)):
        for x in range(len(board[0])):
            if w == 0:
                temp += str(board[x][y][z])
            elif w == 1:
                if board[x][y][z] == 0:
                    temp += '^'
                elif board[x][y][z] == 1:
                    temp += '>'
                elif board[x][y][z] == 2:
                    temp += 'v'
                elif board[x][y][z] == 3:
                    temp += '<'
        temp += "\n"
    print(temp)

def CreateQuadrant(x, y, height, dir, board):
    wh = height/2 
    for i in range(2):
        for j in range(2):
            wx = x+(j*wh)
            wy = y+(i*wh)
            if dir == 0:
                wd = (i*j*2) + i
                sd = 1 + j - i + (i*j)
            elif dir == 1:
                wd = 2 - j - (i*2) + (i*j*2)
                sd = 3 - j - (i*2) + (i*j*3)
            elif dir == 2:
                wd = 1 + (j*2) + i - (i*j*2)
                sd = abs(2 - ((i+j)*2) - (i*j))
            elif dir == 3:
                wd = 3 - j - (i*j*2)
                sd = 1 + (j*2) - (i*j)

            board[int(wx)][int(wy)][0] = wd
            board[int(wx)][int(wy)][1] = sd
            if wh >= 2:
                board = CreateQuadrant(wx, wy, wh, wd, board)
    return board

def Menu():
    CreateArray(4)

Menu()