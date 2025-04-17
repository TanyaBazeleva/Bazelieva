class Graph:
    def __init__(self, size):
        self.vertices = {v: [] for v in range(1, size + 1)}
    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)
    def adjacency_matrix(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1 and j + 1 not in self.vertices[i + 1]:
                    self.add_edge(i + 1, j + 1)
    def counted(self):
        count = 0
        for neighbors in self.vertices.values():
            if len(neighbors) == 1:
                count += 1
        return count
if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    graph = Graph(n)
    graph.adjacency_matrix(matrix)
    result = graph.counted()
    print(result)
