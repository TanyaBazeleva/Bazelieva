def sequence(arry, l, r):
    if l == r:
        yield arry[:]
    else:
        for i in range(l, r + 1):
            arry[l], arry[i] = arry[i], arry[l]
            yield from sequence(arry, l + 1, r)
            arry[l], arry[i] = arry[i], arry[l]

def operators():
    ops = ['+', '-', '*', '/']
    for a in ops:
        for b in ops:
            for c in ops:
                yield a, b, c

def check(i, ops):
    try:
        if abs(eval(f"(({i[0]} {ops[0]} {i[1]}) {ops[1]} {i[2]}) {ops[2]} {i[3]}") - 24) < 1e-6:
            return True
        if abs(eval(f"({i[0]} {ops[0]} ({i[1]} {ops[1]} {i[2]})) {ops[2]} {i[3]}") - 24) < 1e-6:
            return True
        if abs(eval(f"{i[0]} {ops[0]} (({i[1]} {ops[1]} {i[2]}) {ops[2]} {i[3]})") - 24) < 1e-6:
            return True
        if abs(eval(f"{i[0]} {ops[0]} ({i[1]} {ops[1]} ({i[2]} {ops[2]} {i[3]}))") - 24) < 1e-6:
            return True
        if abs(eval(f"({i[0]} {ops[0]} {i[1]}) {ops[1]} ({i[2]} {ops[2]} {i[3]})") - 1e-6) < 1e-6:
            return True
    except ZeroDivisionError:
        return False
    return False

def sort(a, b, c, d):
    numbers = [a, b, c, d]
    for i in sequence(numbers, 0, len(numbers) - 1):
        for ops in operators():
            if check(i, ops):
                return "YES"
    return "NO"

t = int(input().strip())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    print(sort(a, b, c, d))
