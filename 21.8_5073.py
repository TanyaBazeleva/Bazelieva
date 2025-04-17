class Graph:
    def __init__(self):
        self.edges = set()
    def add_edge(self, u, v):
        if (u, v) in self.edges:
            return True
        self.edges.add((u, v))
        return False
    def multiedges(self):
        return self._has_multi
    def build(self, edge_list):
        self._has_multi = False
        for u, v in edge_list:
            if self.add_edge(u, v):
                self._has_multi = True
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        edge_list = [tuple(map(int, f.readline().split())) for _ in range(m)]
    graph = Graph()
    graph.build(edge_list)
    with open("output.txt", "w") as file:
        if graph.multiedges():
            file.write("YES\n")
        else:
            file.write("NO\n")
