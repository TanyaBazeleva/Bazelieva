class Graph:
    def __init__(self, size):
        self.size = size
        self.in_degrees = [0] * size
        self.out_degrees = [0] * size
    def add_edge(self, u, v):
        self.out_degrees[u - 1] += 1
        self.in_degrees[v - 1] += 1
    def get_degrees(self):
        return list(zip(self.in_degrees, self.out_degrees))

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)

    degrees = graph.get_degrees()
    with open("output.txt", "w") as f:
        for deg_in, deg_out in degrees:
            f.write(f"{deg_in} {deg_out}\n")
