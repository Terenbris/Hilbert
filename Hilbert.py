def CreateArray(size):
    board = [[[0,0] for i in range(size)] for j in range(size)]
    board = CreateQuadrant(0, 0, size, 1, 0, 3, 1, board)
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

def GetSubDirection(dir, pos, ij, wdir):
                        #dir   0        1        2        3
    SubDirectionlookupTable = [1,2,0,1, 2,1,1,0, 3,3,1,0, 1,1,0,3,          #position 0
                               1,2,0,2, 1,2,2,3, 2,3,1,2, 2,0,1,0,          #position 1
                               0,3,1,0, 0,3,1,0, 0,2,0,3, 1,0,0,3,          #position 2
                               2,3,1,1, 1,2,3,3, 3,2,0,3, 2,3,1,1]          #position 3
    return SubDirectionlookupTable[int(format(pos, '02b')+format(dir, '02b')+ij,2)]

def GetSubDirection2(position, direction, inside, outside):
    down = direction + 2
    left = direction - 1
    right = direction + 1
    if down > 3:
        down-=4
    if right > 3:
        right = 0
    if left < 0:
        left = 3


def CreateQuadrant(x, y, height, dir, pos, inside, outside, board):
    wh = height/2 
    for i in range(2):
        for j in range(2):
            if dir == 0:
                wd = (i*j*2) + i
                wn = format(2 - (j*2) - i + (4*i*j), '02b')
            elif dir == 1:
                wd = 2 - j - (i*2) + (i*j*2)
            elif dir == 2:
                wd = 1 + (j*2) + i - (i*j*2)
            elif dir == 3:
                wd = 3 - j - (i*j*2)

                

            
            wx = x+(int(wn[1])*wh)
            wy = y+(i*wh)

            board[int(wx)][int(wy)][0] = wd
            board[int(wx)][int(wy)][1] = GetSubDirection(dir, pos, str(i)+str(j), wd)
            if wh >= 2:
                board = CreateQuadrant(wx, wy, wh, wd, int(str(i)+str(j), 2), 0, 0, board)
    return board

def Menu():
    CreateArray(4)

Menu()