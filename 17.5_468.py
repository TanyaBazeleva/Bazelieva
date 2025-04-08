def bst(path):
    if len(path) == 0:
        return False
    min_val = -2147483648
    max_val = 2147483647
    for i in range(1, len(path)):
        prev = path[i - 1]
        curr = path[i]
        if curr < prev:
            if curr <= min_val or curr >= prev:
                return False
            max_val = prev
        elif curr > prev:
            if curr >= max_val or curr <= prev:
                return False
            min_val = prev
        else:
            return False
    return True
if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
        if data:
            path = list(map(int, data.split()))
            if bst(path):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")