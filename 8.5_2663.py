n = int(input().strip())
array = list(map(int, input().split()))

def bubble_sort(array):
    n = len(array)
    swaps = 0
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps += 1
    return swaps

print(bubble_sort(array))
