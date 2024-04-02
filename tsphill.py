import heapq

def best_first_search(start_city, cities, distances):
    num_cities = len(cities)
    # city_indices = {city: i for i, city in enumerate(cities)}
    visited = set()
    pq = [(0, start_city, [start_city])]
    
    while pq:
        print("PQ:", pq)
        c, current_city, path = heapq.heappop(pq)
        print("Current city:", current_city)
        print("Path:", path)
        pq=[ ]
        if len(path) == num_cities:
            new_path = path + [cities[0]]
            i=cities.index(path[-1])
            # print (i)
            c=c+distances[i][0]
            return new_path,c
        
        # visited.add(tuple(path))
        
        for next_city in [x for x in cities if x not in path]:
            # if next_city not in visited:
            new_path = path + [next_city]
            # if tuple(new_path) not in visited:
            cost = c+distances[cities.index(current_city)][cities.index(next_city)]
            heapq.heappush(pq, (cost, next_city, new_path))
    
    return None,0

# Example usage
cities = ['A', 'B', 'C', 'D']  # Example cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]  # Example distances between cities

start_city = cities[0]
path,cost = best_first_search(start_city, cities, distances)
print(path,cost)
