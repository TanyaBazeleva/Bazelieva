class Tree:
    def __init__(self, n):
        self.n = n
        self.data = [None] * (n + 1)
        self.children = [[] for _ in range(n + 1)]
    def add(self, idx, bribe, subs):
        self.data[idx] = bribe
        self.children[idx].extend(subs)
    def min(self, idx):
        if not self.children[idx]:
            return self.data[idx]
        return self.data[idx] + min(self.min(child) for child in self.children[idx])
    def compute(self):
        return self.min(1)
if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        tree = Tree(n)
        for i in range(1, n + 1):
            parts = list(map(int, f.readline().split()))
            d, k, *subs = parts
            tree.add(i, d, subs)
        print(tree.compute())
