n, k = map(int, input().split())
x = list(map(int, input().split()))

def cown(x, n, k, dist):
    count = 1
    end = x[0]
    for i in range(1, n):
        if x[i] - end >= dist:
            count += 1
            end = x[i]
            if count == k:
                return True
    return False

def find(n, k, x):
    l = 1
    r = x[-1] - x[0]
    while l < r:
        m = (l + r + 1) // 2
        if cown(x, n, k, m):
            l = m
        else:
            r = m - 1
    return l

print(find(n, k, x))
