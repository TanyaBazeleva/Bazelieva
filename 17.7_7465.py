class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
def tree(arry):
    if len(arry) == 0:
        return None
    root = Node(arry[0])
    for key in arry[1:]:
        root.insert(key)
    return root
def same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.key != tree2.key:
        return False
    return same_tree(tree1.left, tree2.left) and same_tree(tree1.right, tree2.right)

if __name__ == "__main__":
    with open("input.txt") as file:
        n = int(file.readline())
        arr1 = list(map(int, file.readline().split()))
        m = int(file.readline())
        arr2 = list(map(int, file.readline().split()))
    tree1 = tree(arr1)
    tree2 = tree(arr2)
    if same_tree(tree1, tree2):
        print(1)
    else:
        print(0)