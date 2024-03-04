# import itertools

# Define the distance matrix
distances = {
    ('A', 'B'): 20,
    ('B', 'A'): 20,
    ('A', 'C'): 12,
    ('C', 'A'): 12,
    ('A', 'D'): 35,
    ('D', 'A'): 35,
    ('B', 'C'): 35,
    ('C', 'B'): 30,
    ('B', 'D'): 34,
    ('D', 'B'): 34,
    ('C', 'D'): 12,
    ('D', 'C'): 12
}

# Initial path
all_nodes = ['A', 'B', 'C', 'D','A']

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[(path[i], path[i + 1])]
    return cost

def hill_climbing_tsp(all_nodes):
    path = all_nodes[:]
    current_cost = calculate_cost(path)
    while True:
        swapped = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)-1):
                new_path = path[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                print("New path:", new_path)
                new_cost = calculate_cost(new_path)
                print("New cost:", new_cost)
                if new_cost < current_cost:
                    path = new_path
                    current_cost = new_cost
                    swapped = True
        if not swapped:
            break
        # Complete the cycle by returning to the start
    return path

# Find the path
path = hill_climbing_tsp(all_nodes)

# Print the result
print("Path:", path)
print("Cost:", calculate_cost(path))
