def heap(array):
    n = len(array)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            if array[i] > array[left]:
                return False
        if right < n:
            if array[i] > array[right]:
                return False
    return True
if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        if heap(array):
            print("YES")
        else:
            print("NO")