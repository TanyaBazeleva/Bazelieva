from typing import List, Tuple
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        self.parent[fx] = fy
        return True

def kruskal(n: int, edges: List[Tuple[int, int, int]], banned_edge: Tuple[int, int, int] = None) -> Tuple[int, List[Tuple[int, int, int]]]:
    dsu = DSU(n)
    total_cost = 0
    mst_edges = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if banned_edge and (u, v, w) == banned_edge:
            continue
        if dsu.union(u, v):
            total_cost += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == n - 1:
                break
    if len(mst_edges) != n - 1:
        return float('inf'), []
    return total_cost, mst_edges

if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        edges = []
        for _ in range(m):
            u, v, w = map(int, inp.readline().split())
            edges.append((u, v, w))
    min_cost, mst = kruskal(n, edges)
    second_cost = float('inf')
    for edge in mst:
        cost, _ = kruskal(n, edges, banned_edge=edge)
        if cost != float('inf'):
            second_cost = min(second_cost, cost)
    print(min_cost, second_cost)
