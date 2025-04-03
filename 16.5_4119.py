class Tree:
    def __init__(self):
        self.root = {}
    def add(self, path):
        parts = path.strip().split("\\")
        node = self.root
        for part in parts:
            if part not in node:
                node[part] = {}
            node = node[part]
    def print(self, node=None, depth=0):
        if node is None:
            node = self.root
        for key in sorted(node):
            print(" " * depth + key)
            self.print(node[key], depth + 1)
if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        n = int(f.readline())
        tree = Tree()
        for _ in range(n):
            path = f.readline()
            tree.add(path)
        tree.print()
