def binary_search(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == x:
            return "YES"
        elif array[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return "NO"

if __name__ == "__main__":
    n = int(input().strip())
    v = list(map(int, input().split()))
    m = int(input().strip())
    listic = list(map(int, input().split()))
    results = [binary_search(v, q) for q in listic]
    print("\n".join(results))
