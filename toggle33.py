import random
board = [[0,0,0],[0,0,0],[0,0,0]]
state = False
pos = 1 # Set game state to ture

def beginBoard(): # Randomize Board
    for i in range(9):
        board[i//3][i%3] = random.randint(0,1)
    global state
    state = True
    if(check_solve2()):
        beginBoard()

def outBoard(): # Show board [ have to change to displaying on real board ]
    for i in range(3):
        print(board[i])

def check_solve(): # Check if the board is solved or not, if solved end the game
    solve = True
    for i in range(9):
        if(board[i//3][i%3] == 0):
            solve = False
    if(solve):
        global state
        state = False
        outBoard()
        print("done")

def check_solve2(): # Check if the board is solve (ONLY USE FOR PREVENTING GERERATING BOARD THAT ALREADY WON)
    solve = True
    for i in range(9):
        if(board[i//3][i%3] == 0):
            solve = False
    return solve

def getswitch(a): # for pushing the buttom (switch the light at position a)
    a -= 1
    row = a // 3
    column = a % 3
    if row > 0:
        board[row-1][column] = 1 - board[row-1][column]
    if row < 2:
        board[row+1][column] = 1 - board[row+1][column]
    if column > 0:
        board[row][column-1] = 1 - board[row][column-1]
    if column < 2:
        board[row][column+1] = 1 - board[row][column+1]
    board[row][column] = 1 - board[row][column]
    check_solve()

def moveleft(): # Move left for (l) input
    global pos
    pos -= 1
    if(pos < 1):
        pos += 9

def moveright(): # Move left for (r) input
    global pos
    pos += 1
    if(pos > 9):
        pos -= 9

def action(c): # For getting input (l = move left, r= move right, c = confirm)
    global pos
    if c == 'l':
        moveleft()
        print("Current position : ", pos)
    elif c == 'r':
        moveright()
        print("Current position : ", pos)
    elif c == 'c':
        getswitch(pos)
        print("Activating switch at pos ", pos)
        pos = 1
        print("Current position : ", pos)

beginBoard()
print("Current position : 1")
while(state): # While game haven't ended, get input
    outBoard()
    action = input("Choose an action (l,r,c) : ")
    action(action)