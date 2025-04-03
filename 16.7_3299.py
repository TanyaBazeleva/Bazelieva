from collections import defaultdict
class Tree:
    def __init__(self, root=0):
        self.n = None
        self.m = None
        self.parent_list = []
        self.queries = []
        self.lca_sum = 0
        self.root = root
        self.LOG = 17
        self.up = []
        self.depth = []
    def build(self):
        self.up = [[-1]*self.LOG for _ in range(self.n)]
        self.depth = [0]*self.n
        tree = defaultdict(list)
        for i in range(1, self.n):
            tree[self.parent_list[i - 1]].append(i)
        def dfs(v, p):
            self.up[v][0] = p
            for i in range(1, self.LOG):
                if self.up[v][i-1] != -1:
                    self.up[v][i] = self.up[self.up[v][i-1]][i-1]
            for u in tree[v]:
                self.depth[u] = self.depth[v] + 1
                dfs(u, v)

        dfs(self.root, -1)
    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        for i in reversed(range(self.LOG)):
            if self.up[u][i] != -1 and self.depth[self.up[u][i]] >= self.depth[v]:
                u = self.up[u][i]
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.up[u][i] != -1 and self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]
        return self.up[u][0]
    def execute(self, line):
        if not self.n:
            self.n, self.m = map(int, line.strip().split())
        elif len(self.parent_list) < self.n - 1:
            self.parent_list += list(map(int, line.strip().split()))
            if len(self.parent_list) == self.n - 1:
                self.build()
        elif len(self.queries) < 2:
            self.queries += list(map(int, line.strip().split()))
        elif len(self.queries) == 2:
            self.queries += list(map(int, line.strip().split()))
            return self.solve()
    def solve(self):
        a = [self.queries[0], self.queries[1]]
        x, y, z = self.queries[2], self.queries[3], self.queries[4]
        u, v = a[0], a[1]
        ans = self.lca(u, v)
        total = ans
        for i in range(1, self.m):
            a.append((x * a[-2] + y * a[-1] + z) % self.n)
            a.append((x * a[-2] + y * a[-1] + z) % self.n)
            u = (a[2*i] + ans) % self.n
            v = a[2*i+1]
            ans = self.lca(u, v)
            total += ans
        return total
if __name__ == "__main__":
    with open("input.txt") as f:
        tree = Tree()
        k = 4
        for _ in range(k):
            line = f.readline()
            result = tree.execute(line)
            if result is not None:
                print(result)
