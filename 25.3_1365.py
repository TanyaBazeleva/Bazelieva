INF = float("inf")
graph = []

def init(n):
    global graph
    graph = [[] for _ in range(n)]
def addEdge(u, v, w):
    graph[u].append((v, w))
def findDistance(start, end):
    n = len(graph)
    distances = [INF] * n
    visited = [False] * n
    distances[start] = 0
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or distances[i] < distances[u]):
                u = i
        if distances[u] == INF:
            break
        visited[u] = True
        for v, w in graph[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
    return distances[end] if distances[end] != INF else -1

if __name__ == "__main__":
    n, s, f = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    init(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1 and i != j:
                addEdge(i, j, matrix[i][j])
    result = findDistance(s - 1, f - 1)
    print(result)