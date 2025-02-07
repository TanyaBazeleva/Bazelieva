import math
def find():
    eps = 0.0000000001
    l, r = 1.6, 3
    while r - l > eps:
        m = (l + r) / 2
        if math.sin(m) < m / 3:
            r = m
        else:
            l = m
    return l

print(f"Корінь: {find():.3f}") 
