class Node:
    def __init__(self, left=0, right=0, prefix_len=1, suffix_len=1, max_len=1):
        self.left = left
        self.right = right
        self.prefix_len = prefix_len
        self.suffix_len = suffix_len
        self.max_len = max_len
class Tree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.data = data
        self.build(1, 0, self.n - 1)
    def build(self, v, tl, tr):
        if tl == tr:
            val = self.data[tl]
            self.tree[v] = Node(val, val, 1, 1, 1)
        else:
            tm = (tl + tr) // 2
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)
            self.tree[v] = self.merge(self.tree[v * 2], self.tree[v * 2 + 1], tm - tl + 1, tr - tm)
    def merge(self, left_node, right_node, llen, rlen):
        res = Node()
        res.left = left_node.left
        res.right = right_node.right
        # Обчислюємо prefix_len
        if left_node.prefix_len == llen and left_node.right <= right_node.left:
            res.prefix_len = left_node.prefix_len + right_node.prefix_len
        else:
            res.prefix_len = left_node.prefix_len
        # Обчислюємо suffix_len
        if right_node.suffix_len == rlen and left_node.right <= right_node.left:
            res.suffix_len = left_node.suffix_len + right_node.suffix_len
        else:
            res.suffix_len = right_node.suffix_len
        # Обчислюємо max_len
        res.max_len = max(left_node.max_len, right_node.max_len)
        if left_node.right <= right_node.left:
            res.max_len = max(res.max_len, left_node.suffix_len + right_node.prefix_len)
        return res
    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = Node(new_val, new_val, 1, 1, 1)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = self.merge(
                self.tree[v * 2], self.tree[v * 2 + 1],
                tm - tl + 1, tr - tm)
    def query(self, v, tl, tr, l, r):
        if l > r:
            return Node(0, 0, 0, 0, 0)
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_res = self.query(v * 2, tl, tm, l, min(r, tm))
        right_res = self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        return self.merge(
            left_res, right_res,
            min(r, tm) - l + 1 if l <= tm else 0,
            r - max(tm + 1, l) + 1 if r > tm else 0)
if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        m = int(f.readline())
        queries = [list(map(int, f.readline().split())) for _ in range(m)]
    tree = Tree(arr)
    result = []
    for q in queries:
        if q[0] == 1:
            l, r = q[1] - 1, q[2] - 1
            res = tree.query(1, 0, n - 1, l, r)
            result.append(str(res.max_len))
        elif q[0] == 2:
            pos, new_val = q[1] - 1, q[2]
            tree.update(1, 0, n - 1, pos, new_val)
    with open("output.txt", "w") as f:
        f.write("\n".join(result))
