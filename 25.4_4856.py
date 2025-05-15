INF = float("inf")
graph = []

def init(vertices, edges_count=None):
    global graph
    graph = [{} for _ in range(vertices)]
def addEdge(u, v, w):
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w
def getWay(start, end):
    n = len(graph)
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            for v in graph[u]:
                w = graph[u][v]
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    updated = True
        if not updated:
            break
    for u in range(n):
        for v in graph[u]:
            if dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                raise ValueError("Цикл з від’ємною вагою виявлено")
    if dist[end] == INF:
        print(-1)
    else:
        print(int(dist[end]))
        path = []
        current = end
        while current != -1:
            path.append(current + 1)
            current = parent[current]
        path.reverse()
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    n, m = map(int, input().split())
    s, f = map(int, input().split())
    init(n, m)
    for _ in range(m):
        u, v, w = map(int, input().split())
        addEdge(u - 1, v - 1, w)
        addEdge(v - 1, u - 1, w)
    getWay(s - 1, f - 1)