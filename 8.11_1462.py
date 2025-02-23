n = int(input().strip())
array = [int(input().strip()) for _ in range(n)]

def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        currentValue = array[index]
        position = index
        while (position > 0 and (array[position - 1] % 10 > currentValue % 10 or (array[position - 1] % 10 == currentValue % 10 and array[position - 1] > currentValue))):
            array[position] = array[position - 1]
            position -= 1
        array[position] = currentValue

insertion_sort(array)
print(" ".join(map(str, array)))
