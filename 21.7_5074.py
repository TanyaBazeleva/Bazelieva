class Graph:
    def __init__(self, size):
        self.size = size
        self.degrees = [0] * size
    def add_edge(self, u, v):
        self.degrees[u - 1] += 1
        self.degrees[v - 1] += 1
    def get_degrees(self):
        return self.degrees
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)
    degrees = graph.get_degrees()
    with open("output.txt", "w") as f:
        for d in degrees:
            f.write(str(d) + "\n")
