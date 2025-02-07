def find_x(C):
    eps = 0.0000000001
    l, r = 0, max(1, C)
    while r - l > eps:
        m = (l + r) / 2
        if m**2 + m**0.5 < C:
            l = m
        else:
            r = m
    return l

C = float(input().strip())
print(f"{find_x(C):.9f}")
