from collections import deque
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(1, n + 1)}
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def is_bipartite(self):
        color = {}
        for vertex in range(1, self.n + 1):
            if vertex not in color:
                if not self.bfs(vertex, color):
                    return False
        return True
    def bfs(self, start, color):
        queue = deque([start])
        color[start] = 0
        while queue:
            v = queue.popleft()
            for neighbor in self.adj[v]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[v]
                    queue.append(neighbor)
                elif color[neighbor] == color[v]:
                    return False
        return True
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
    if graph.is_bipartite():
        print("YES")
    else:
        print("NO")
