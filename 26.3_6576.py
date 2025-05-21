def kruskal(n, edges):
    parent = list(range(n + 1))
    def find(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
        return True
    mst_edges = set()
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if union(u, v):
            mst_edges.add((min(u, v), max(u, v)))
    return mst_edges

def process_test_case(n, m, p, q, edge_data):
    target_edge = None
    for u, v, w in edge_data:
        if (u == p and v == q) or (u == q and v == p):
            target_edge = (min(p, q), max(p, q), w)
            break
    if target_edge is None:
        return "NO"
    mst = kruskal(n, edge_data)
    return "YES" if (min(p, q), max(p, q)) in mst else "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, p, q = map(int, input().split())
        edge_data = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            edge_data.append((u, v, w))
        print(process_test_case(n, m, p, q, edge_data))
