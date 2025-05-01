import sys
import threading
from collections import defaultdict

sys.setrecursionlimit(1 << 25)

def main():
    n = int(input())
    m1 = int(input())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    for _ in range(m1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        reverse_graph[v - 1].append(u - 1)
    m2 = int(input())
    candidate_edges = []
    for index in range(m2):
        u, v, w = map(int, input().split())
        candidate_edges.append((u - 1, v - 1, w, index + 1))
    order = []
    visited = [False] * n
    def dfs(v):
        visited[v] = True
        for to in graph[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)
    for i in range(n):
        if not visited[i]:
            dfs(i)
    comp = [-1] * n
    current_comp = 0
    def reverse_dfs(v, label):
        comp[v] = label
        for to in reverse_graph[v]:
            if comp[to] == -1:
                reverse_dfs(to, label)
    for v in reversed(order):
        if comp[v] == -1:
            reverse_dfs(v, current_comp)
            current_comp += 1
    if current_comp == 1:
        print("YES")
        print(0)
        print(0)
        return
    in_deg = [0] * current_comp
    out_deg = [0] * current_comp
    for v in range(n):
        for to in graph[v]:
            if comp[v] != comp[to]:
                out_deg[comp[v]] += 1
                in_deg[comp[to]] += 1
    need_in = []
    need_out = []
    for i in range(current_comp):
        if in_deg[i] == 0:
            need_in.append(i)
        if out_deg[i] == 0:
            need_out.append(i)
    candidate_edges_between_components = []
    for u, v, w, idx in candidate_edges:
        if comp[u] != comp[v]:
            candidate_edges_between_components.append((w, u, v, idx))
    candidate_edges_between_components.sort()
    result = []
    total_weight = 0
    pair_map = {}
    for w, u, v, idx in candidate_edges_between_components:
        cu = comp[u]
        cv = comp[v]
        if cu in need_out and cv in need_in and (cu, cv) not in pair_map:
            pair_map[(cu, cv)] = idx
            result.append(idx)
            total_weight += w
    if len(result) < max(len(need_in), len(need_out)):
        print("NO")
    else:
        print("YES")
        print(total_weight)
        print(len(result))
        for idx in result:
            print(idx)

if __name__ == "__main__":
    threading.Thread(target=main).start()
