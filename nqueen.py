borad=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
        [0,0,0,0]
       ]
def is_safe(borad,row,col):
    for i in range(row):
        if borad[i][col]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if borad[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,len(borad))):
        if borad[i][j]==1:
            return False
    return True
def placequeen(borad,row):
    for i in range(len(borad)):
        if is_safe(borad,row,i):
            borad[row][i]=1
            return borad,True
            
    return borad,False
def printboard(borad):
    for i in range(len(borad)):
        for j in range(len(borad)):
            print(borad[i][j],end=" ")
        print()
    print()
    
def bfs(borad):
    for i in range(len(borad)):
        borad,flag=placequeen(borad,i)
        if flag==True:
            printboard(borad)
bfs(borad)