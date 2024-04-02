import heapq
def calcost(path,distances):
    c=0
    for i in range(len(path)-1):
       c=c+distances[cities.index(path[i])][cities.index(path[i+1])]
    return c
def best_first_search(start_city, cities, distances):
    num_cities = len(cities)
    visited = set()
    pq = [(0, start_city, [start_city])]
    
    while pq:
        print("PQ:", pq)
        c, current_city, path = heapq.heappop(pq)
        print("Current city:", current_city)
        print("Path:", path)
        
        if len(path) == num_cities:
            new_path = path + [cities[0]]
            i=cities.index(path[-1])
            # print (i)
            c=c+distances[i][0]
            pro = calcost(new_path,distances)
            return new_path,c,pro
        
        visited.add(tuple(path))
        
        for next_city in [x for x in cities if x not in path]:
            # if next_city not in visited:
            new_path = path + [next_city]
            if tuple(new_path) not in visited:
                p= calcost(new_path,distances)+heuristic[cities.index(next_city)]
                heapq.heappush(pq, (p, next_city, new_path))
    
    return None,0

# Example usage
cities = ['A', 'B', 'C', 'D']  # Example cities
distances = [
    [0, 50, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]  # Example distances between cities
heuristic=[90,80,70,60]
start_city = cities[0]
path,cost,pro = best_first_search(start_city, cities, distances)
print(path,cost,pro)
