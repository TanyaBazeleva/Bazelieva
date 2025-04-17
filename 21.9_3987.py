class Graph:
    def __init__(self, n):
        self.n = n
        self.edge_set = set()
    def add_edge(self, u, v):
        a, b = min(u, v), max(u, v)
        self.edge_set.add((a, b))
    def is_complete(self):
        expected_edges = self.n * (self.n - 1) // 2
        return len(self.edge_set) == expected_edges
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
    with open("output.txt", "w") as file:
        if graph.is_complete():
            file.write("YES\n")
        else:
            file.write("NO\n")

