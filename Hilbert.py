def CreateArray(size):
    board = [[[0,0] for i in range(size)] for j in range(size)]
    CreateQuadrant(size)
    print(board)

def CreateQuadrant(height):
    wh = height/2

    if wh < 2:
        return
    else:
        CreateQuadrant(wh)

CreateArray(2)