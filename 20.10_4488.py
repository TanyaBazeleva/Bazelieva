import sys
sys.setrecursionlimit(1 << 25)
class Node:
    def __init__(self):
        self.left_val = self.right_val = 0
        self.left_len = self.right_len = self.max_len = 1
        self.len = 1
        self.set = None
class Tree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1, data)
    def build(self, v, l, r, data):
        if l == r:
            node = self.tree[v]
            val = data[l]
            node.left_val = node.right_val = val
            node.left_len = node.right_len = node.max_len = 1
            node.len = 1
        else:
            m = (l + r) // 2
            self.build(v * 2, l, m, data)
            self.build(v * 2 + 1, m + 1, r, data)
            self.tree[v] = self.merge(self.tree[v * 2], self.tree[v * 2 + 1])
    def push(self, v, l, r):
        if self.tree[v].set is not None and l != r:
            val = self.tree[v].set
            for u in [v * 2, v * 2 + 1]:
                self.tree[u].set = val
                self.tree[u].left_val = self.tree[u].right_val = val
                self.tree[u].left_len = self.tree[u].right_len = self.tree[u].max_len = self.tree[u].len
            self.tree[v].set = None
    def merge(self, a, b):
        res = Node()
        res.len = a.len + b.len
        res.left_val = a.left_val
        res.right_val = b.right_val
        res.left_len = a.left_len if a.left_len == a.len and a.right_val <= b.left_val else a.left_len
        if a.right_val <= b.left_val:
            res.left_len = a.len + b.left_len if a.left_len == a.len else res.left_len
        res.right_len = b.right_len if b.right_len == b.len and a.right_val <= b.left_val else b.right_len
        if a.right_val <= b.left_val:
            res.right_len = b.len + a.right_len if b.right_len == b.len else res.right_len
        res.max_len = max(a.max_len, b.max_len)
        if a.right_val <= b.left_val:
            res.max_len = max(res.max_len, a.right_len + b.left_len)
        return res
    def update(self, v, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            node = self.tree[v]
            node.set = val
            node.left_val = node.right_val = val
            node.left_len = node.right_len = node.max_len = node.len
            return
        self.push(v, l, r)
        m = (l + r) // 2
        self.update(v * 2, l, m, ql, qr, val)
        self.update(v * 2 + 1, m + 1, r, ql, qr, val)
        self.tree[v] = self.merge(self.tree[v * 2], self.tree[v * 2 + 1])
    def query(self, v, l, r, ql, qr):
        if ql > r or qr < l:
            return None
        if ql <= l and r <= qr:
            return self.tree[v]
        self.push(v, l, r)
        m = (l + r) // 2
        left = self.query(v * 2, l, m, ql, qr)
        right = self.query(v * 2 + 1, m + 1, r, ql, qr)
        if left is None:
            return right
        if right is None:
            return left
        return self.merge(left, right)
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx]);
    idx += 1
    arr = list(map(int, data[idx:idx + n]));
    idx += n
    m = int(data[idx]);
    idx += 1
    tree = Tree(arr)
    res = []
    for _ in range(m):
        q_type = int(data[idx]);
        idx += 1
        l = int(data[idx]) - 1;
        idx += 1
        r = int(data[idx]) - 1;
        idx += 1
        if q_type == 1:
            ans = tree.query(1, 0, n - 1, l, r).max_len
            res.append(str(ans))
        else:
            v = int(data[idx]);
            idx += 1
            tree.update(1, 0, n - 1, l, r, v)
    print("\n".join(res))
