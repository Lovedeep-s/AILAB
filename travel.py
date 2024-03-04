import itertools

# Define the distance matrix
distances = {
    ('A', 'B'): 20,
    ('B', 'A'): 20,
    ('A', 'C'): 42,
    ('C', 'A'): 42,
    ('A', 'D'): 35,
    ('D', 'A'): 35,
    ('B', 'C'): 30,
    ('C', 'B'): 30,
    ('B', 'D'): 34,
    ('D', 'B'): 34,
    ('C', 'D'): 12,
    ('D', 'C'): 12
}


# Initial path
initial_path = ['A', 'B', 'D', 'C', 'A']

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[(path[i], path[i + 1])]
    return cost

def best_first_tsp(initial_path, max_cost):
    queue = [initial_path]
    path = initial_path
    for permutation in itertools.permutations(path[1:-1]):
            new_path = [path[0]] + list(permutation) + [path[-1]]
            queue.append(new_path)
    while queue:
        path = queue.pop(0)
        cost = calculate_cost(path)
        if cost < max_cost:
            return path, cost
        print(path,cost)
    return None, None

# Find the path
path, cost = best_first_tsp(initial_path, 100)

# Print the result
if path:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found within the cost limit.")
