# import itertools

# Define the distance matrix
distances = {
    ('A', 'B'): 20,
    ('B', 'A'): 20,
    ('A', 'C'): 42,
    ('C', 'A'): 42,
    ('A', 'D'): 35,
    ('D', 'A'): 35,
    ('B', 'C'): 35,
    ('C', 'B'): 30,
    ('B', 'D'): 34,
    ('D', 'B'): 34,
    ('C', 'D'): 12,
    ('D', 'C'): 12
}

# Define the heuristic function (straight-line distance)
heuristic = {
    'A': 55,  # Estimated distance from A to goal
    'B': 45,  # Estimated distance from B to goal
    'C': 25,  # Estimated distance from C to goal
    'D': 20   # Estimated distance from D to goal
}

# Initial path
all_nodes = ['A', 'B', 'C', 'D']

def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[(path[i], path[i + 1])]
    return cost

def a_star_tsp(all_nodes):
    remaining_nodes = all_nodes[1:]
    path = ['A']
    while remaining_nodes:
        min_cost = float('inf')
        best_node = None
        for node in remaining_nodes:
            # print("Node:", node)
            new_path = path + [node]
            
            cost_so_far = calculate_cost(new_path)
            # print("Cost so far:", cost_so_far)
            total_cost = cost_so_far + heuristic[node]
            # total_cost = cost_so_far
            if total_cost < min_cost:
                min_cost = total_cost
                best_node = node
        path.append(best_node)
        remaining_nodes.remove(best_node)
        # print("Path:", path)
    path.append(path[0])  # Complete the cycle by returning to the start
    return path
# Find the path
path = a_star_tsp(all_nodes)

# Print the result
print("Path:", path)
print("Cost:", calculate_cost(path))
