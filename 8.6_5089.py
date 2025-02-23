n = int(input().strip())
array = [input().strip() for _ in range(n)]

def selection_sort(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        minindex = i
        for j in range(1, i + 1):
            if array[j] < array[minindex]:
                minindex = j
        array[i], array[minindex] = array[minindex], array[i]

selection_sort(array)
print("\n".join(array))
