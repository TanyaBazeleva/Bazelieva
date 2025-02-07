def find_x():
    eps = 0.0000000001
    l, r = 0, 10
    while r - l > eps:
        m = (l + r) / 2
        if m**3 + m + 1 > 5:
            r = m
        else:
            l = m
    return l

print(f"Найменше: {find_x():.3f}")
