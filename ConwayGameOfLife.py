import sys
def inboundAdd(number, target):
    if number + 1 >= target:
        return 0
    else:
        return number + 1
def inboundSub(number, target):
    if number - 1 < 0:
        return target - 1
    else:
        return number - 1
def remove(posx, posy):
    posx = int(posx)
    posy = int(posy)
    neighbours = 0
    if board[inboundAdd(posx, lines)][posy] == 1:
        neighbours += 1
    if board[inboundSub(posx, lines)][posy] == 1:
        neighbours += 1
    if board[posx][inboundAdd(posy, cols)] == 1:
        neighbours += 1
    if board[posx][inboundSub(posy, cols)] == 1:
        neighbours += 1
    if board[inboundAdd(posx, lines)][inboundAdd(posy, cols)] == 1:
        neighbours += 1
    if board[inboundSub(posx, lines)][inboundSub(posy, cols)] == 1:
        neighbours += 1
    if board[inboundSub(posx, lines)][inboundAdd(posy, cols)] == 1:
        neighbours += 1
    if board[inboundAdd(posx, lines)][inboundSub(posy, cols)] == 1:
        neighbours += 1
    
    return neighbours
    
board = []
#starts variables and creates the board where the game of life is going to be played
lines = int(sys.argv[1])
cols = int(sys.argv[2])
print(inboundSub(4, lines))
i = 0
while i < lines:
    board.append([0] * cols)
    i += 1
#inserts positions representing living cells on the board
file = open(sys.argv[3], "r")
for line in file:
    chars = line.split(" ")
    board[int(chars[0])][int(chars[1])] = 1
print("================================")
for line in board:
    for col in line:
        print(col, end="   ")
    print()
while True:
    i = 0
    boardAux = []
    while i < lines:
        aux = []
        j = 0
        while j < cols:
            neighbours = remove(i, j)
            if neighbours < 2 or neighbours > 3:
                aux.append(0)
            elif board[i][j] == 1 and (neighbours == 2):
                aux.append(1)
            elif neighbours == 3:
                aux.append(1)
            else:
                aux.append(0)
            j += 1
        boardAux.append(aux)
        i += 1
    board = boardAux
    input("Press any key to continue")
    for line in board:
        for col in line:
            print(col, end="   ")
        print()
    
