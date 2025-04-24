class Graph:
    def __init__(self, size):
        self.n = size
        self.adj = {i: [] for i in range(1, size + 1)}
    def add_edge(self, u, v):
        self.adj[u].append(v)
    def count_paths(self, current, target, days_left, visited):
        if days_left < 0:
            return 0
        if current == target:
            return 1
        visited.add(current)
        total_paths = 0
        for neighbor in self.adj[current]:
            if neighbor not in visited:
                total_paths += self.count_paths(neighbor, target, days_left - 1, visited)
        visited.remove(current)
        return total_paths
if __name__ == "__main__":
    with open("input.txt") as f:
        n, k, a, b, d = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(k):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
    result = graph.count_paths(a, b, d, set())
    print(result)
