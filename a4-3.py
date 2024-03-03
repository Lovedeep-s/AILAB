import itertools

# Complete city distances
city_distances = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('A', 'D'): 20,
    ('B', 'A'): 10,
    ('B', 'C'): 35,
    ('B', 'D'): 25,
    ('C', 'A'): 15,
    ('C', 'B'): 35,
    ('C', 'D'): 30,
    ('D', 'A'): 20,
    ('D', 'B'): 25,
    ('D', 'C'): 30
}

def total_distance(route):
    # Calculate the total distance of the given route
    distance = 0
    for i in range(len(route) - 1):
        distance += city_distances[(route[i], route[i + 1])]
    distance += city_distances[(route[-1], route[0])]  # Return to the origin
    return distance

def next_state_gen(current_state):
    # Generate the next possible states from the current state
    next_states = []
    cities = list(current_state)
    for perm in itertools.permutations(cities[1:]):  # Exclude the first city (origin)
        next_states.append((cities[0],) + perm)
    return next_states

# Example heuristic: Minimum spanning tree (MST) approach
def heuristic_mst(route):
    # Calculate the lower bound of the route using the MST approach
    if len(route) < 2:
        return 0
    min_span_tree_dist = 0
    remaining_cities = set(route)
    current_city = route[0]
    remaining_cities.remove(current_city)
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: city_distances[(current_city, city)])
        min_span_tree_dist += city_distances[(current_city, next_city)]
        remaining_cities.remove(next_city)
        current_city = next_city
    min_span_tree_dist += city_distances[(current_city, route[0])]  # Return to the origin
    return min_span_tree_dist

# Example usage
initial_state = ('A', 'B', 'C', 'D')
print("Initial state:", initial_state)
print("Initial heuristic value (MST):", heuristic_mst(initial_state))

current_state = initial_state
for next_state in next_state_gen(current_state):
    print("Next state:", next_state)
    print("Heuristic value (MST):", heuristic_mst(next_state))
