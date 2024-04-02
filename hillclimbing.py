import heapq
from copy import deepcopy
initial=[0,0,0,0]
weights=[
    [50,20],
    [60,60],
    [30,50],
    [70,40]
]
capacity=100
def calcost(queue):
    weigh =0
    profit=0
    for i in range(len(queue)):
        if queue[i]==1:
            weigh+=weights[i][0]
            profit+=weights[i][1]
    if weigh>capacity:
        return 0
    else:
        return profit 
            
            
def change(queue,i):
    queue[i]=1
    return queue

def bfs():
    queue=[[0,initial]]
    visited=[]
    visited.append(initial)
    while queue:
        profit,current_state=queue.pop()
        m=0
        bestnode=[ ]
        for i in range(4):
            nx2 = change(deepcopy(current_state),i)
            p=calcost(nx2)
            if p>profit:
                if p>m:
                    m=p
                    bestnode = nx2
        if bestnode not in visited and m!=0:
            queue.append([m,bestnode])
            visited.append(bestnode)
            print(m,bestnode)
    print(profit,current_state)
    
    # print(visited)
bfs()