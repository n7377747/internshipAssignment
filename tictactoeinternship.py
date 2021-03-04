import random


def newboard():
    '''
    generate an empty board, reset the number of moves
    and choose a random player
    '''
    board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return board,9,random.choice(['O','X'])


def printboard(board):
    '''
    print the board
    '''
    for row in board:
        print("| {} | {} | {} |".format(row[0],row[1],row[2]))

def checkRows(board):
    '''
    check if any row is filled with same items
    '''
    for row in board:
        if row[0]==row[1] and row[1]==row[2]:
                return row[0]
    return None
            
    
def checkCols(board):
    '''
    check if any column is filled with same items
    '''
    for i in range(len(board)):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            return board[0][i]
    return None

def checkLeftDiagonal(board):
    '''
    check if left diagonal is filled with same items
    '''
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if board[0][0] != 0:
            return board[0][0]
    return None

def checkRightDiagonal(board):
    '''
    check if right diagonal is filled with same items
    '''
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        if board[2][0] != 0:
            return board[2][0]
    return None

def placeItem(row, column, board, current_player):
    '''
    place item if the position is vacant
    '''
    if board[row][column] != ' ':
        return None
    else:
        board[row][column] = current_player


def swapPlayers(player):
    '''
    swap player O to X and vice versa
    '''
    if (player == 'O'):
        return 'X'
    else:
        return 'O'


def machineMove(board):
    '''
    generate a random machine move and place item
    '''
    moveFound=False
    while moveFound==False:
        row=random.choice([0,1,2])
        col=random.choice([0,1,2])
        if board[row][col] == ' ':
            board[row][col]='O'
            moveFound=True
    
def readScoreBoard():
    '''
    read the text file, return a tuple of scores,
     first value is score of machine
     second value is the score of the user
    '''
    f=open('./scoreboard.txt','r')
    data=f.read()
    data=data.split('\n')
    f.close()
    O_score=int(data[0].split()[1])
    X_score=int(data[1].split()[1])
    return O_score,X_score

def displayScoreBoard():
    '''
    display score board from textfile
    '''
    X_score,O_score=readScoreBoard()
    print(
        '''
        | computer | user |
        |%10d|%6d|
        '''%(X_score,O_score)
    )
def updateScoreBoard(x,o):
    '''
    update the text file with new scores
    '''
    X_score,O_score=readScoreBoard()
    f=open('./scoreboard.txt','w')
    f.write(str("O {}\n".format(O_score+o)))
    f.write(str("X {}".format(X_score+x)))
    f.close()

def winner(board):
    '''
    check if any player has won the game
    '''
    if checkRows(board) is not None:
        return checkRows(board)
    if checkCols(board) is not None:
        return checkCols(board)
    if checkLeftDiagonal(board) is not None:
        return checkLeftDiagonal(board)
    if checkRightDiagonal(board) is not None:
        return checkRightDiagonal(board)
    return None

def startGame():
    '''
    function to start the game
    '''
    while exit is not True:
        print("new Game starts now")
        board,moves,player=newboard()    
        # import pdb;pdb.set_trace()
        while moves>0:
            if player=='O':
                print("Machine moved, user's turn")
                machineMove(board)
                moves=moves-1
                player=swapPlayers(player)
            else:
                print("\nBoard: ")
                printboard(board)
                prompt=input("tictactoe> ").split()
                if prompt[0].lower()=='move':
                    row,col=([int(i) for i in prompt[1].split(',')])
                    if row not in range(0,3) or col not in range(0,3):
                        print(" {} {} is not a valid move".format(row,col)) 
                    elif placeItem(row,col,board,player) is not None:
                        print("Invalid move, place already taken")
                    else:
                        player=swapPlayers(player)
                        moves=moves-1
                elif "".join(prompt).lower()=='newgame':
                    break
                elif "".join(prompt).lower()=='scoreboard':
                    displayScoreBoard()
                elif "".join(prompt).lower()=="quit":
                    exit()
                    
                else:
                    print("Invalid command please try again")

            if winner(board) is not None:
                if winner(board)=='O':
                    print("Computer wins!")
                    printboard(board)
                    updateScoreBoard(1,0)
                    break
                elif winner(board)=='X':
                    print("User wins!")
                    printboard(board)
                    updateScoreBoard(0,1)
                    break
        
        if moves==0 and winner(board) is not None:
            print("The Game is a Draw")
        
        
        print("Gameover! Type newgame to start again")
        prompt=input("tictactoe> ")
        if prompt.lower()=="quit":
            exit()
        elif "".join(prompt).lower()=='scoreboard':
            displayScoreBoard()
if __name__=="__main__":
    startGame()

