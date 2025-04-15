from math import gcd, ceil, log2
class Tree:
    def __init__(self, nums, func, neutral):
        self.size = len(nums)
        self.func = func
        self.neutral = neutral
        height = ceil(log2(self.size))
        self.data = [neutral] * (2 ** (height + 1))
        self.build(nums, 1, 0, self.size - 1)
    def build(self, nums, node, start, end):
        if start == end:
            self.data[node] = nums[start]
        else:
            mid = (start + end) // 2
            self.build(nums, 2 * node, start, mid)
            self.build(nums, 2 * node + 1, mid + 1, end)
            self.data[node] = self.func(self.data[2 * node], self.data[2 * node + 1])
    def update(self, pos, value, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        if start == end:
            self.data[node] = value
        else:
            mid = (start + end) // 2
            if pos <= mid:
                self.update(pos, value, 2 * node, start, mid)
            else:
                self.update(pos, value, 2 * node + 1, mid + 1, end)
            self.data[node] = self.func(self.data[2 * node], self.data[2 * node + 1])
    def query(self, left, right, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        if left > right:
            return self.neutral
        if left == start and right == end:
            return self.data[node]
        mid = (start + end) // 2
        left_result = self.query(left, min(right, mid), 2 * node, start, mid)
        right_result = self.query(max(left, mid + 1), right, 2 * node + 1, mid + 1, end)
        return self.func(left_result, right_result)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
if __name__ == "__main__":
    with open("input.txt") as file:
        size = int(file.readline())
        nums = list(map(int, file.readline().split()))
        ops = int(file.readline())
        queries = [list(map(int, file.readline().split())) for _ in range(ops)]
    gcd_tree = Tree(nums, gcd, 0)
    lcm_tree = Tree(nums, lcm, 1)
    results = []
    for query in queries:
        q, l, r = query
        l -= 1
        r -= 1
        if q == 1:
            g = gcd_tree.query(l, r)
            L = lcm_tree.query(l, r)
            if g < L:
                results.append("wins")
            elif g > L:
                results.append("loser")
            else:
                results.append("draw")
        elif q == 2:
            gcd_tree.update(l, r + 1)
            lcm_tree.update(l, r + 1)
    with open("output.txt", "w") as file:
        file.write("\n".join(results))