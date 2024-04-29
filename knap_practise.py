import heapq
from copy import deepcopy
initial=[0,0,0,0]
weights=[[38, 43], [23, 63], [91, 6], [37, 3]]
par=[ ]
capacity=100
def calcost(queue):
    weight=0
    profit=0
    for i in range(len(queue)):
        if queue[i]==1:
            weight+=weights[i][0]
            profit+=weights[i][1]
    if weight>capacity:
        return 0
    return profit

def nextstate(queue,i):
    queue[i]=1
    return queue


def bestfs():
    queue=[(0,initial,par)]
    visited = [ ]
    visited.append(initial)
    max=0
    while queue:
        profit, currentstate,parent = heapq.heappop(queue)
        if profit>max:
            bestnode=currentstate
            bp=parent
            max=profit
            
        for i in range(len(initial)):
            nx = nextstate(deepcopy(currentstate),i)
            p=calcost(nx)
            if nx not in visited:
                heapq.heappush(queue,(p,nx,currentstate))
                visited.append(nx)
        
        heapq._heapify_max(queue)
        # print(queue)
    
    print(max,bestnode)
    print_path(bp)


def print_path(bp):
    while bp:
        print(bp)
        bp = bp[2]
    print(initial)
bestfs()
