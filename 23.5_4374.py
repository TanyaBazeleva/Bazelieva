from collections import deque

def is_connected(n, edges, removed_edges_set):
    graph = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        edge_index = idx + 1
        if edge_index not in removed_edges_set:
            graph[u].append(v)
            graph[v].append(u)
    start = None
    for i in range(n):
        if graph[i]:
            start = i
            break
    if start is None:
        return True
    visited = [False] * n
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for to in graph[v]:
            if not visited[to]:
                visited[to] = True
                queue.append(to)
    for i in range(n):
        if graph[i] and not visited[i]:
            return False
    return True

if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        edges = []
        for _ in range(m):
            a, b = map(int, inp.readline().split())
            edges.append((a - 1, b - 1))
        k = int(inp.readline())
        queries = []
        for _ in range(k):
            data = list(map(int, inp.readline().split()))
            c = data[0]
            removed_edges = data[1:]
            queries.append(removed_edges)
    result = []
    for removed in queries:
        removed_set = set(removed)
        if is_connected(n, edges, removed_set):
            result.append("Connected")
        else:
            result.append("Disconnected")
    for res in result:
        print(res)
