board = [' ' for x in range(10)] 
def printBoard(board): 
    print('   |   |   ') 
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]) 
    print('   |   |   ') 
    print('------------') 
    print('   |   |   ') 
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]) 
    print('   |   |   ') 
    print('------------') 
    print('   |   |   ') 
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]) 
    print('   |   |   ') 
 
 
 
 
def IsWinner(b,l): 
    return (b[1]== l and b[2]==l and b[3]==l) or (b[4]== l and b[5]==l and b[6]==l) or (b[7]== l and b[8]==l and b[9]==l) or (b[1]== l and b[4]==l and b[7]==l) or (b[3]== l and b[6]==l and b[9]==l) or (b[2]== l and b[5]==l and b[8]==l) or (b[1]== l and b[5]==l and b[9]==l) or (b[3]== l and b[5]==l and b[7]==l) 

def spaceIsFree(pos): 
    return board[pos]==' ' 
 
def insertLetter(letter,pos): 
    board[pos]=letter 
 
 
def isEmpty():
    a=[]
    for i in range(10):
        if(i and board[i]==' '):
            print(f"{i}, ", end="")
    print(" are empty.")
 
 
def Game(): 
    cnt=9
    run = True
    flag=1  
    try:
        while run: 
            if flag: 
                symbol='X'
            else :
                symbol ='0'

            move = input(f"please select a position to enter the {symbol} between 1 to 9: ")   
            move = int(move) 
            if move > 0 and move < 10: 
                if spaceIsFree(move): 
                    insertLetter(symbol , move) 
                    cnt=cnt-1
                    temp=IsWinner(board,symbol)
                    printBoard(board)
                    if temp:
                        print(f"{symbol} is Winner.")
                        run=False
                    elif cnt==0:
                        run=False
                        print("Draw")
                else: 
                    print('Sorry, this space is occupied ') 
                    isEmpty()
                    continue
            else: 
                print('please type a number between 1 and 9') 
                continue;
                
            if(flag):
                flag=0
            else:
                flag=1
 
    except: 
            print('Please type a number') 



Game()