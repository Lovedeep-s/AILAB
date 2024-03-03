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
        print(' '.join(map(str, row)))
    print()

def findBlank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def isGoal(state):
    return state == goal

def get_parent_states(parents, curr_state):
    path = []
    while curr_state[1] is not None:
        path.append(curr_state[1])
        curr_state = curr_state[1]
    return path

def BFS():
    queue = [(initial_state, None)]  # Including the parent state
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    while queue:
        curr_state = queue.pop(0)

        state, parent_state = curr_state[0], curr_state[1]  # Extract state and parent

        if isGoal(state):
            print("Goal state reached.")
            printState(state)
            path = get_parent_states(queue, curr_state)
            print("Path to goal state:")
            for state in reversed(path):
                printState(state[0])
            return True

        i, j = findBlank(state)

        for move_func in [moveLeft, moveRight, moveUp, moveDown]:
            new_state, moved = move_func(state)
            if moved:
                state_tuple = tuple(map(tuple, new_state))
                if state_tuple not in visited:
                    queue.append((new_state, curr_state))  # Store the parent state
                    visited.add(state_tuple)

    print("Goal state not reachable!")
    return False

def moveLeft(state):
    i, j = findBlank(state)
    if j == 0:
        return state, False
    else:
        new_state = [row[:] for row in state]  # Create a copy of the state
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        return new_state, True

def moveRight(state):
    i, j = findBlank(state)
    if j == 2:
        return state, False
    else:
        new_state = [row[:] for row in state]  # Create a copy of the state
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        return new_state, True

def moveUp(state):
    i, j = findBlank(state)
    if i == 0:
        return state, False
    else:
        new_state = [row[:] for row in state]  # Create a copy of the state
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        return new_state, True

def moveDown(state):
    i, j = findBlank(state)
    if i == 2:
        return state, False
    else:
        new_state = [row[:] for row in state]  # Create a copy of the state
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        return new_state, True

BFS()
