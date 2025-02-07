def find():
    eps = 0.0000000001
    l, r = 0, 2
    while r - l > eps:
        m = (l + r) / 2
        if m**3 + 4*m**2 + m - 6 > 0:
            r = m
        else:
            l = m
    return l

print(f"Корінь: {find():.3f}")
