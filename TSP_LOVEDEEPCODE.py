from collections import deque

def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    queue = [(start, [start], 0)]  # (current_node, path_taken, total_cost)

    min_cost = float('inf')
    min_path = []

    while queue:
        current_node, path_taken, total_cost = queue.pop()

        if len(path_taken) == n:
            if graph[current_node][start] != 0:
                total_cost += graph[current_node][start]  # Add cost to return to start
                if total_cost < min_cost:
                    min_cost = total_cost
                    min_path = path_taken + [start]
        else:
            for next_node not in path_taken:
                if not visited[next_node] and graph[current_node][next_node] != 0:
                    visited[next_node] = True
                    new_path = path_taken + [next_node]
                    new_cost = total_cost + graph[current_node][next_node]
                    queue.append((next_node, new_path, new_cost))
                    visited[next_node] = False  # Reset visited flag

    return min_cost, min_path

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_node = 0
min_cost, min_path = tsp(graph, start_node)

print("Minimum cost:", min_cost)
print("Minimum path:", min_path)
