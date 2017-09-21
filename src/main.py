'''
Created on Sep 20, 2017

@author: jlearx
'''
COLSIZE = 3
ROWSIZE = 3

def printBoard(gameBoard):    
    for i in range(0,ROWSIZE):
        print(gameBoard[i])
    
    print("")
    
def getMove(gameBoard):
    # Display game state
    printBoard(gameBoard)
    
    # Repeat until a valid move is given
    while (True):
        moveStr = input("Please enter a valid move as row,column: ").strip()
        row = -1
        col = -1        
        
        # Check input length
        if (len(moveStr) < 3):
            continue
        
        # Check if input contains a comma
        cPos = moveStr.find(',')
        
        if ((cPos < 1) or (cPos == len(moveStr) - 1)):
            continue
        
        # Parse move out of input string
        row = moveStr[:cPos]
        col = moveStr[cPos + 1:]
        
        # Make sure the row and column are numeric
        if (row.isnumeric() and col.isnumeric()):
            # Reduce by 1 because we start from 0
            row = int(row) - 1
            col = int(col) - 1
        else:
            continue
        
        # Make sure the row and column are within bounds
        if ((row < 0) or (col < 0) or (row >= ROWSIZE) or (col >= COLSIZE)):
            continue
        
        # Check if move is in a free square (0)
        if (gameBoard[row][col] == 0):
            return (row,col)
        else:
            # Show the board again
            printBoard(gameBoard)

def playGame(gameBoard):
    getMove(gameBoard)

if __name__ == '__main__':
    gameBoard = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    playGame(gameBoard)
    