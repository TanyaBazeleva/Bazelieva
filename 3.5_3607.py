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
def count(heights, x, y):
    heights.sort()
    left_index = binary_left(heights, x)
    right_index = binary_right(heights, y)
    return right_index - left_index

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split("\n")
    index = 0
    results = []

    while index < len(data):
        if not data[index].strip():
            index += 1
            continue
        n = int(data[index].strip())
        index += 1
        heights = list(map(int, data[index].split()))
        index += 1
        x, y = map(int, data[index].split())
        index += 1
        results.append(str(count(heights, x, y)))
    print("\n".join(results))
