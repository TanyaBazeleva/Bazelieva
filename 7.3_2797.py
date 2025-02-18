import sys
n = int(sys.stdin.readline().strip())
numbers = map(int, sys.stdin.readline().strip().split())
contacts = set(numbers)
print(len(contacts))

