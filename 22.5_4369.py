from collections import deque
class Graph:
    def __init__(self, n):
        self.adj = {i: [] for i in range(1, n + 1)}
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def burn(self, sources):
        visited = {}
        queue = deque()
        for s in sources:
            visited[s] = 0
            queue.append(s)
        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
        max_time = max(visited.values())
        latest_nodes = [v for v in visited if visited[v] == max_time]
        return max_time, min(latest_nodes)
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
        k = int(f.readline())
        start_points = list(map(int, f.readline().split()))
    seconds, vertex = graph.burn(start_points)
    print(seconds)
    print(vertex)
