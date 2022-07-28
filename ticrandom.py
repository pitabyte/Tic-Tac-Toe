from random import randint

#create a list of all positions from 1 to 9
pos = []
for i in range(9):
    pos.append(i+1)

#create a list of variables which will hold players' choices
choice = []
for i in range(9):
    choice.append(" ")

#check if there is a win on a board
def check(ox):
    i = 0

    #horizontal wins
    for i in range(0, 8, 3):
        if pos[i] == ox and pos[i+1] == ox and pos[i+2] == ox:
            print(ox + ' is a winner!')
            exit()
    i=0

    #vertical wins
    for i in range(3):
        if pos[i] == ox and pos[i+3] == ox and pos[i+6] == ox:
            print(ox + ' is a winner!')
            exit()
    #cross wins
    if pos[0] == ox and pos[4] == ox and pos[8] == ox:
        print(ox + ' is a winner!')
        exit()
    if pos[2] == ox and pos[4] == ox and pos[6] == ox:
        print(ox + ' is a winner!')
        exit()

    #check if draw
    if all(x != ' ' for x in choice):
        print("It's a draw!")
        exit()
        
#print grid with numbers for position tutorial
def printgrid(list):
    k=0
    for i in range(15):
        if i == 4 or i == 9:
            print(("_"*5 + "|")*2 + "_"*5)
        elif i == 2 or i == 7 or i == 12:
            print(" "*2 + str(list[k]) + " "*2 + "|" + " "*2 + str(list[k+1]) + " "*2 + "|" + " "*2 + str(list[k+2]) + " "*2)
            k = k + 3
        else:
            print((" "*5 + "|")*2 + " "*5)


#welcome with numbered grid
printgrid(pos)
print('Look at the numeration of the grid and play accordingly :)')


while True:
    #ask player for choice and check if wins
    while True:
        move = input('Choose a number where "X" will be placed \n')
        move = int(move)
        if choice[move-1] != 'O' or choice[move-1] != 'X':
            if move in pos:
                break
    
    choice[move-1] = 'X'
    pos[move-1] = 'X'
    check('X')

    #bot's move and check if wins
    while True:
        move = randint(1, 9)
        if choice[move-1] != 'O' or choice[move-1] != 'X':
            if move in pos:
                break
    choice[move-1] = 'O'
    pos[move-1] = 'O'
    printgrid(choice)
    check('O')