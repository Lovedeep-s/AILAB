from copy import deepcopy

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

def printState(state):
    for row in state:
        print(" ".join(map(str, row)))
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
        return state, 0
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
    return state == goal

def parent(state):
    queue = []
    while state:
        queue.append(state)
        state = state.parent
    return queue

def DFS():
    stack = [initial_state]
    visited = set()

    while stack:
        curr_state = stack.pop()

        print("Current state:")
        printState(curr_state)

        if curr_state == goal:
            print("Goal state reached.")
            printState(curr_state)
            # print("Path:")
            # p = parent(curr_state)
            # while p:
            #     printState(p.pop())
            return True

        i, j = findBlank(curr_state)

        visited.add(tuple(map(tuple, curr_state)))

        for move_func in [moveLeft, moveRight, moveUp, moveDown]:
            new_state, moved = move_func(deepcopy(curr_state))
            if moved and tuple(map(tuple, new_state)) not in visited:
                stack.append(new_state)

    print("Goal state not reachable!")
    return False

DFS()
