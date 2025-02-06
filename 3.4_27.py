def binar(b):
    return int(b, 2)
def generate(n):
    bin_str = bin(n)[2:]
    rotations = [bin_str[i:] + bin_str[:i] for i in range(len(bin_str))]
    return sorted([binar(rot) for rot in rotations])

def search(array):
    left, right = 0, len(array) - 1
    while left < right:
        middle = (left + right + 1) // 2
        if array[middle] > array[left]:
            left = middle
        else:
            right = middle - 1
    return array[left]

def max(n):
    rotations = generate(n)
    return search(rotations)

if __name__ == "__main__":
    n = int(input( ))
    print(max(n))
