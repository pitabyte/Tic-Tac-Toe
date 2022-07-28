pos = []

def printgrid(grid):
    for i in range(9):
        print(grid[i], end='')
        if (i+1) % 3 == 0:
            print('\n')

def check(ox):
    for i in range(0, 8, 3):
        if pos[i] == ox and pos[i+1] == ox and pos[i+2] == ox:
            print(ox + ' is a winner')
            exit()
    i=0
    for i in range(3):
        if pos[i] == ox and pos[i+3] == ox and pos[i+6] == ox:
            print(ox + ' is a winner')
            exit()
    if pos[0] == ox and pos[4] == ox and pos[8] == ox:
        print(ox + ' is a winner')
        exit()
    if pos[2] == ox and pos[4] == ox and pos[6] == ox:
        print(ox + ' is a winner')
        exit()
    
for i in range(9):
    pos.append(i+1)

i=0

for i in range(9):
    print(pos[i], end='')
    if (i+1) % 3 == 0:
        print('\n')

while True:
    while True:
        move = input('Choose a number where "X" will be placed \n')
        if int(move) in pos:
            break
    move = int(move)
    pos[move-1] = 'X'
    printgrid(pos)
    check('X')

    while True:
        move = input('Choose a number where "O" will be placed \n')
        if int(move) in pos:
            break
    move = int(move)
    pos[move-1] = 'O'
    printgrid(pos)
    check('O')