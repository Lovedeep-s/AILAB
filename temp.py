import heapq
cities=["A","B","C","D"]
start =cities[0]
distances = [
    [0, 50, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def bfs():
    queue=[(0,start,[start])]
    visited = [ ]
    visited.append(tuple([start]))
    while queue:
        cost,current,path=heapq.heappop(queue)
        
        if len(path)==len(cities):
            newpath= path+[start]
            c =cost + distances[cities.index(current)][cities.index(start)]
           
            print(newpath,c)
            return 0
        for nextcity in [x for x in cities if x not in path]:
            newpath= path+[nextcity]
            c =cost + distances[cities.index(current)][cities.index(nextcity)]
        
            if (tuple(newpath)) not in visited:
                visited.append(tuple(newpath))
                heapq.heappush(queue,(c,nextcity,newpath))
        heapq.heapify(queue)
    return False
    
bfs()
                