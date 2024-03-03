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
q = PriorityQueue()

def heuristic(state,goal):
   
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count

# def heuristic(state):
#     distance = 0
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] != 0:
#                 goal_i, goal_j = divmod(state[i][j] - 1, 3)
#                 distance += abs(i - goal_i) + abs(j - goal_j)
#     return distance

class StateNode:
    def __init__(self, state, parent=None, steps=0):
        self.state = state
        self.parent = parent
        self.steps = steps
    def get_parent(self):
        return self.parent
    def get_steps(self):
        return self.steps
    def newstate(self,state ,parent, steps):
        self.state = state
        self.parent = parent
        self.steps = steps
    def getstate(self):
        return self.state
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return heuristic(self.state, goal) < heuristic(other.state, goal)



def printState(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()
    print()

def findBlank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def moveLeft(state):
    i, j = findBlank(state)
    if j == 0:
        return state, 0
    else:
        state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
        return state, 1

def moveRight(state):
    i, j = findBlank(state)
    if j == 2:
        return state, 0
    else:
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]
        return state, 1

def moveUp(state):
    i, j = findBlank(state)
    if i == 0:
        return state,0
    else:
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        return state, 1
def moveDown(state):
    i, j = findBlank(state)
    if i == 2:
        return state, 0
    else:
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        return state, 1


def isGoal(state):
    global goal
    if state == goal:
        return True
    else:
        return False

def parent(state):
    q = []
    while state:
        q.append(state.state)
        state = state.get_parent()
    return q

def BFS():
    q.put(StateNode(initial_state))
    visited = set()

    while not q.empty():
        curr_state = q.get()

        if isGoal(curr_state.state):
            print("Goal reached in ",curr_state.steps," steps.")
            printState(curr_state.state)
            print("Path is :")
            p = parent(curr_state)
            while p:
                printState(p.pop())
            return True

        visited.add(tuple(map(tuple, curr_state.state)))
        for move_func in [moveUp, moveDown, moveRight, moveLeft]:
            newstate, moved = move_func(deepcopy(curr_state.state))
            if moved and tuple(map(tuple, newstate)) not in visited:
                q.put(StateNode(newstate, curr_state, curr_state.steps + 1))
    print("Goal state not reached")
BFS()