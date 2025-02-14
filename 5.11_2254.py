A, B, C = map(int, input().split())
X = [int(input()) for _ in range(A)]
def max(A, B, C, X):
    def transport(k):
        prefix = [0] * (A + 1)
        for i in range(A):
            prefix[i + 1] = prefix[i] + X[i]
        for i in range(A - k + 1):
            median_idx = i + k // 2
            median = X[median_idx]
            left_cost = median * (median_idx - i) - (prefix[median_idx] - prefix[i])
            right_cost = (prefix[i + k] - prefix[median_idx + 1]) - median * (i + k - median_idx - 1)
            if left_cost + right_cost <= C:
                return True
        return False

    l, r = 1, A
    while l < r:
        m = (l + r + 1) // 2
        if transport(m):
            l = m
        else:
            r = m - 1
    return l

print(max(A, B, C, X))
