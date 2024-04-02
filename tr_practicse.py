import heapq
cities = ['A', 'B', 'C', 'D']  # Example cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
] 
start=cities[0]
def bfs():
    q=[(0,start,[start])]
    heapq.heapify(q)
    visited=set()
    while q:
        c,currentcity,path=heapq.heappop(q)
        
        if len(path)==len(cities):
            new_path=path+[cities[0]]
            c+=distances[cities.index(path[-1])][cities.index(start)]
            print(new_path,c)
            return
        visited.add(tuple(path))
        for new_city in (x for x in cities if x not in path):
            new_path=path+[new_city]
            cost=c+distances[cities.index(currentcity)][cities.index(new_city)]
            if tuple(new_path) not in visited:
                heapq.heappush(q,([cost,new_city,new_path]))

bfs()
            
            
    