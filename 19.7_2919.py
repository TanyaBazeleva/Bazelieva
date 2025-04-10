import sys
sys.setrecursionlimit(200000)
def read_tree(n, edges):
    tree = {}
    for i in range(1, n + 1):
        l, r = edges[i - 1]
        tree[i] = (l, r)
    return tree
def get_potential(node, tree):
    if node == -1:
        return 0
    l, r = tree[node]
    if l == -1 or r == -1:
        return 1
    return 1 + min(get_potential(l, tree), get_potential(r, tree))
def find_violation(node, tree):
    if node == -1:
        return -1
    l, r = tree[node]
    if l == -1 and r != -1:
        return node
    if l != -1 and r != -1:
        pot_l = get_potential(l, tree)
        pot_r = get_potential(r, tree)
        if pot_l < pot_r:
            return node
    left_check = find_violation(l, tree)
    if left_check != -1:
        return left_check
    return find_violation(r, tree)
if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        edges = [tuple(map(int, f.readline().split())) for _ in range(n)]
    tree = read_tree(n, edges)
    result = find_violation(1, tree)
    print(result)
