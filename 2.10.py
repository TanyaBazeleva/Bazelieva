def f(n):
    sum = 0 # 1
    for i in range(1, n + 1): # n + 1
        sum = sum + i # 2
    return sum
# n*2 + 2 < O(2n) = O(n)