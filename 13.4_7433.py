def convert_to_base(n, m):
    n = int(n)
    m = int(m)
    result = []
    while n > 0:
        remainder = n % m
        if remainder > 9:
            result.append(f"[{remainder}]")
        else:
            result.append(str(remainder))
        n //= m
    return "".join(result[::-1])
n = input().strip()
m = input().strip()
print(convert_to_base(n, m))
