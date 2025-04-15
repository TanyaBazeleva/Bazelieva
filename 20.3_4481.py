from math import gcd, log2, ceil
class Tree:
    def __init__(self, nums):
        self.size = len(nums)
        h = ceil(log2(self.size))
        total_size = 2 ** (h + 1)
        self.data = [0] * total_size
        self.build(nums, 1, 0, self.size - 1)
    def build(self, nums, node, start, end):
        if start == end:
            self.data[node] = nums[start]
        else:
            mid = (start + end) // 2
            self.build(nums, 2 * node, start, mid)
            self.build(nums, 2 * node + 1, mid + 1, end)
            self.data[node] = gcd(self.data[2 * node], self.data[2 * node + 1])
    def update(self, pos, val, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        if start == end:
            self.data[node] = val
        else:
            mid = (start + end) // 2
            if pos <= mid:
                self.update(pos, val, 2 * node, start, mid)
            else:
                self.update(pos, val, 2 * node + 1, mid + 1, end)
            self.data[node] = gcd(self.data[2 * node], self.data[2 * node + 1])
    def query(self, left, right, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.data[node]
        mid = (start + end) // 2
        left_result = self.query(left, right, 2 * node, start, mid)
        right_result = self.query(left, right, 2 * node + 1, mid + 1, end)
        return gcd(left_result, right_result)
if __name__ == "__main__":
    with open("input.txt") as file:
        size = int(file.readline())
        nums = list(map(int, file.readline().split()))
        ops = int(file.readline())
        queries = [tuple(map(int, file.readline().split())) for _ in range(ops)]
    tree = Tree(nums)
    output = []
    for query in queries:
        if query[0] == 1:
            left, right = query[1] - 1, query[2] - 1
            output.append(str(tree.query(left, right)))
        elif query[0] == 2:
            pos, value = query[1] - 1, query[2]
            tree.update(pos, value)
    with open("output.txt", "w") as file:
        file.write("\n".join(output))