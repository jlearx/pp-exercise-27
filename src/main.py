'''
Created on Sep 20, 2017

@author: jlearx
'''

def printBoard(gameBoard):
    size = len(gameBoard)
    
    for i in range(0,size):
        print(gameBoard[i])
    
    print("")
    
def getMove(gameBoard):
    printBoard(gameBoard)

def playGame(gameBoard):
    getMove(gameBoard)

if __name__ == '__main__':
    gameBoard = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    playGame(gameBoard)
    