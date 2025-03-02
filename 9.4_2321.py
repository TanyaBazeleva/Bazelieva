def qsort(array, a, b):
    while a < b:
        pivot = array[a + (b - a) // 2]
        left = a
        right = b
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        if right - a < b - left:
            qsort(array, a, right)
            a = left
        else:
            qsort(array, left, b)
            b = right

n = int(input())
listic = list(map(int, input().split()))
qsort(listic, 0, n - 1)
print(*listic)
