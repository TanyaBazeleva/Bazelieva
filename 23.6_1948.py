from collections import deque
if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for _ in range(m):
            u, v = map(int, inp.readline().split())
            graph[u - 1].append(v - 1)
            in_degree[v - 1] += 1
    queue = deque()
    result = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        result.append(node + 1)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != n:
        print(-1)
    else:
        print(*result)
