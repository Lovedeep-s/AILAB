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
    heapq._heapify_max(queue)
    while queue:
        profit,current_state=heapq.heappop(queue)
        for i in range(4):
            nx2 = change(deepcopy(current_state),i)
            if nx2 not in visited:
                p=calcost(nx2)
                heapq.heappush(queue,[p,nx2])
                visited.append(nx2)
    print(profit,current_state)
    
    # print(visited)
bfs()