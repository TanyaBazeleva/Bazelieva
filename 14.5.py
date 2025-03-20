import sys
from collections import deque

def josephus(n, k):
    queue = deque(range(1, n+1))
    while len(queue) > 1:
        queue.rotate(-k)
        queue.pop()
    return  queue[0]
def main():
    input_date = sys.stdin.read().strip()
    n, k = map(int, input_date.split())
    print(josephus(n, k))
if __name__ == '__main__':
    main()