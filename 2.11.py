def g(n):
    sum = 0 # 1
    for i in range(1, n + 1): # n + 1
        sum = sum + i + f(i) # 3
    return sum
# O(n^2) через виклик f(i)

