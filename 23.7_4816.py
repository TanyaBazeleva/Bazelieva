class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]
        self.visited = [False] * size
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self, vertex, component):
        self.visited[vertex] = True
        component.append(vertex + 1)
        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, component)
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u - 1, v - 1)
    components = []
    for i in range(n):
        if not graph.visited[i]:
            component = []
            graph.dfs(i, component)
            components.append(component)
    print(len(components))
    for component in components:
        print(len(component))
        print(*component)
