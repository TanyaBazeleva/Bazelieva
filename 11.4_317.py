import sys
sys.set_int_max_str_digits(200000)  # Увеличение лимита на обработку длинных чисел
def karatsuba(x, y):
    x = str(x)
    y = str(y)
    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    n = len(x)
    m = n // 2
    if m == 0:
        return int(x) * int(y)
    x_high = int(x[:-m]) if len(x) > m else 0
    x_low = int(x[-m:]) if len(x) >= m else int(x)
    y_high = int(y[:-m]) if len(y) > m else 0
    y_low = int(y[-m:]) if len(y) >= m else int(y)
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba(x_low + x_high, y_low + y_high)
    z2 = karatsuba(x_high, y_high)
    result = (z2 * (10 ** (2 * m))) + ((z1 - z2 - z0) * (10 ** m)) + z0
    return result
a, b = map(int, input().split())
print(karatsuba(a, b))