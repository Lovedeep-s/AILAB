from copy import deepcopy

initial_state = [
    [0, 3, 6],
    [1, 2, 0],
    [4, 5, 7]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 0]
]

def heuristic(state):
    c = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] != goal[i][j]:
                c += 1
    return c

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                return i, j
    return None

def move_up(state):
    i, j = find_blank(state)
    if i > 0:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        return new_state
    return None

def move_down(state):
    i, j = find_blank(state)
    if i < 2:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        return new_state
    return None

def move_left(state):
    i, j = find_blank(state)
    if j > 0:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        return new_state
    return None

def move_right(state):
    i, j = find_blank(state)
    if j < 2:
        new_state = deepcopy(state)
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        return new_state
    return None

def hill_climbing(state):
    current_state = state
    path = [current_state]
    while True:
        neighbors = [move_up(current_state), move_down(current_state), move_left(current_state), move_right(current_state)]
        best_neighbor = min(neighbors, key=lambda x: heuristic(x) if x is not None else float('inf'))
        if heuristic(best_neighbor) >= heuristic(current_state):
            break
        current_state = best_neighbor
        path.append(current_state)
    return path

def print_state(state):
    for row in state:
        print(" ".join(str(cell) for cell in row))

print("Initial State:")
print_state(initial_state)

path = hill_climbing(initial_state)

print("\nPath:")
for state in path:
    print_state(state)
    print()
































# from copy import deepcopy
# from queue import PriorityQueue

# initial_state = [
#     [0, 3, 6],
#     [1, 2, 0],
#     [4, 5, 7]
# ]

# goal = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 0, 0]
# ]

# queue = PriorityQueue()

# class statenode:
#     def __init__(self, state, parent=None, step=0):
#         self.state = state
#         self.parent = parent
#         self.step = step

#     def __lt__(self, other):
#         return heuristic(self.state) > heuristic(other.state)

#     def getparent(self):
#         return self.parent

# def heuristic(state):
#     c = 0
#     for i in range(len(state)):
#         for j in range(len(state)):
#             if state[i][j] == goal[i][j]:
#                 c += 1

#     return c

# def findblanks(state):
#     blanks = []
#     for i in range(len(state)):
#         for j in range(len(state)):
#             if state[i][j] == 0:
#                 blanks.append((i, j))
#     return blanks

# def up(state):
#     m = 0
#     blanks = findblanks(state)
#     for i, j in blanks:
#         if i > 0:
#             state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
#             m = 1
#     return state, m

# def down(state):
#     m = 0
#     blanks = findblanks(state)
#     for i, j in blanks:
#         if i < 2:
#             state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
#             m = 1
#     return state, m

# def left(state):
#     m = 0
#     blanks = findblanks(state)
#     for i, j in blanks:
#         if j > 0:
#             state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
#             m = 1
#     return state, m

# def right(state):
#     m = 0
#     blanks = findblanks(state)
#     for i, j in blanks:
#         if j < 2:
#             state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]
#             m = 1
#     return state, m

# def parent(state):
#     q = []
#     while state:
#         q.append(state.state)
#         state = state.getparent()
#     return q

# def printstate(state):
#     for i in range(len(state)):
#         for j in range(len(state)):
#             print(state[i][j], end=" ")
#         print()
#     print()

# def bfs():
#     queue.put(statenode(initial_state))
#     visited = set()
#     visited.add(tuple(map(tuple, initial_state)))
#     while not queue.empty():
#         currentstate = queue.get()
#         if currentstate.state == goal:
#             print(currentstate.step)
#             k = parent(currentstate.getparent())
#             while k:
#                 printstate(k.pop())
#             printstate(currentstate.state)
#             print("pass")
#             return 1
#         for movfun in [up, down, left, right]:
#             next_state, m = movfun(deepcopy(currentstate.state))
#             if m == 1:
#                 if tuple(map(tuple, next_state)) not in visited:
#                     queue.put(statenode(next_state, currentstate, currentstate.step + 1))
#                     visited.add(tuple(map(tuple, next_state)))

#     return None

# bfs()
