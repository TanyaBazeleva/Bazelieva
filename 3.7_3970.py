def binary_left(array, x):
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < x:
            left = middle + 1
        else:
            right = middle
    return left
def binary_right(array, y):
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] <= y:
            left = middle + 1
        else:
            right = middle
    return left
def count(colors, n):
    results = []
    for i in n:
        left = binary_left(colors, i)
        right = binary_right(colors, i)
        results.append(str(right - left))
    return results

if __name__ == "__main__":
    a = int(input().strip())
    if a > 0:
        colors = list(map(int, input().split()))
    else:
        colors = []
    b = int(input().strip())
    n = list(map(int, input().split()))
    print("\n".join(count(colors, n)))