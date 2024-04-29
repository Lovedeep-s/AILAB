from copy import deepcopy
from queue import PriorityQueue
initial_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

queue = PriorityQueue()
class statenode:
    def __init__(self, state, parent=None, step=0):
        self.state = state
        self.parent = parent
        self.step = step
    def __lt__(self,other):
        return heuristic(self.state)<heuristic(other.state)
    def getparent(self):
        return self.parent
def heuristic(state):
    c=0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]!=goal[i][j]:
                c+=1
                
    return c
    
def findblank(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]==0:
                return i,j
            
    return None
def up(state):
    m = 0
    i, j = findblank(state)
    if i == 0:
        return state, m
    else:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        m = 1
        return new_state, m


def down(state):
    m = 0
    i, j = findblank(state)
    if i == 2:
        return state, m
    else:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        m = 1
        return new_state, m


def left(state):
    m = 0
    i, j = findblank(state)
    if j == 0:
        return state, m
    else:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        m = 1
        return new_state, m


def right(state):
    m = 0
    i, j = findblank(state)
    if j == 2:
        return state, m
    else:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        m = 1
        return new_state, m
def parent(state):
    q = []
    while state:
        q.append(state.state)
        state = state.getparent()
    return q
def printstate(state):
    for i in range(len(state)):
        for j in range(len(state)):
            print(state[i][j], end=" ")
        print()
    print()
def bfs():
    queue.put(statenode(initial_state))
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    while not queue.empty():
        currentstate=queue.get()
        if currentstate.state == goal:
            print(currentstate.step)
            k=parent(currentstate.getparent())
            # print(k)
            while k:
                printstate(k.pop())
            printstate(currentstate.state)
            print("pass")
            return 1
        for movfun in [up,down,left,right]:
            next_state,m=movfun(deepcopy(currentstate.state))
            if m==1:
                if (tuple(map(tuple, next_state))) not in visited:
                    queue.put(statenode(next_state,currentstate,currentstate.step+1))
                    visited.add(tuple(map(tuple, next_state)))
        
    return None
bfs()