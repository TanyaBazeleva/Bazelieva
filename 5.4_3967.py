n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

def cut(x, k, l):
    count = 0
    for i in x:
        count += i // l
    return count >= k

def find(n, k, x):
    l, r = 1, max(x)
    while l < r:
        m = (l + r + 1) // 2
        if cut(x, k, m):
            l = m
        else:
            r = m - 1
    return l

print(find(n, k, x))
