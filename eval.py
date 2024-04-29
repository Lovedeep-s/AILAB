from queue import PriorityQueue
from copy import deepcopy

initial=[
    [1,2,3],
    [8,0,4],
    [7,6,5]
]
goal=[
    [2,8,1],
    [0,4,3],
    [7,6,5]
]
# initial = [
#     [2, 0, 3],
#     [1, 8, 4],
#     [7, 6, 5]
# ]
# goal = [
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5]
# ]
def heuristic(state):
    c=0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]!=goal[i][j]:
                c+=1
    return c
            
class statenode:
    def __init__(self,state,parent=None,steps=0):
        self.state=state
        self.parent =parent
        self.steps=steps
    def __lt__(self,other):
        return (self.steps+heuristic(self.state))<(other.steps + heuristic(other.state))
        # return (heuristic(self.state))<(heuristic(other.state))

def findblank(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]==0:
                return i,j
        
        
def moveup(s):
    m=0
    i,j=findblank(s)
    if i==0:
        return s, m
    else:
        m=1
        state = deepcopy(s)
        state[i-1][j],state[i][j]=state[i][j],state[i-1][j]
        return state ,m
def movedown(s):
    m=0
    i,j=findblank(s)
    if i==2:
        return s, m
    else:
        m=1
        state = deepcopy(s)
        state[i+1][j],state[i][j]=state[i][j],state[i+1][j]
        return state ,m
def moveleft(s):
    m=0
    i,j=findblank(s)
    if j==0:
        return s, m
    else:
        m=1
        state = deepcopy(s)
        state[i][j-1],state[i][j]=state[i][j],state[i][j-1]
        return state ,m
def moveright(s):
    m=0
    i,j=findblank(s)
    if j==2:
        return s, m
    else:
        m=1
        state = deepcopy(s)
        state[i][j+1],state[i][j]=state[i][j],state[i][j+1]
        return state ,m
def getparent(state):
    k =[]
    while state:
        k.append(state.state)
        state=state.parent
        
    return k
def printstate(state):
    for i in range(len(state)):
        for j in range(len(state)):
            print(state[i][j] ,end=" ")
        print(" ")
    print(" ")    
def astar():
    queue = PriorityQueue()
    queue.put(statenode(initial))
    visited=[ ]
    visited.append(tuple(map(tuple, initial)))
    while queue:
        curr_state=deepcopy(queue.get())
        
        if curr_state.state==goal:
            print("Goal state reached in ",curr_state.steps," steps")
            print("Path taken")
            k=getparent(curr_state)
            while k:
                printstate(k.pop(-1))
            # printstate(curr_state.state)print("Goal state reached in ",curr_state.steps," steps")
            print("pass")
            
            return 0
        
        for movfunc in [moveup,movedown,moveleft,moveright]:
            next_state,m=movfunc(deepcopy(curr_state.state))
            if m==1 and (tuple(map(tuple, next_state))) not in visited:
                queue.put(statenode(next_state,curr_state,curr_state.steps+1))
                visited.append(tuple(map(tuple, next_state)))
                
    print("fail")
    
astar()