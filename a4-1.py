from copy import deepcopy
# initial_state = [
#     [1, 2, 3],
#     [0, 4, 6],
#     [7, 5, 8]
# ]

# goal = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]

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

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count
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

    def __eq__(self, other):
        return self.state == other.state


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
    if i == 2:
        return state,0
    else:
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        return state, 1
def moveDown(state):
    i, j = findBlank(state)
    if i == 0:
        return state, 0
    else:
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        return state, 1


def isGoal(state):
    global goal
    if state == goal:
        return True
    else:
        return False

def parent(state):
    queue = []
    while state:
        queue.append(state.state)
        state = state.get_parent()
    return queue

def Puzzle():
    
    queue = [StateNode(initial_state)]
    visited = [] # Including the number of steps taken
    visited.append(initial_state)
    while queue:
        curr_state= queue.pop(0)
        
        print("Current state in steps",curr_state.steps," : ")
        printState(curr_state.state)

        if curr_state.state == goal:
            print("Goal state reached in",curr_state.steps,"steps.")
            printState(curr_state.state)
            print("Path:")
            p=parent(curr_state)
            while p:
                printState(p.pop())
            return True
    

        for move_func in [moveLeft, moveRight, moveUp, moveDown]:
            new_state, moved = move_func(deepcopy(curr_state.state))
            if moved and new_state not in visited:
                visited.append(new_state)
                if heuristic(curr_state.state) < heuristic(new_state):
                    queue.append(StateNode(new_state, curr_state, curr_state.steps + 1))
                    print(heuristic(curr_state.state),heuristic(new_state))

            
               
    print("Goal state not reachable!")
    return False

Puzzle()


                # Store the parent state
                    
