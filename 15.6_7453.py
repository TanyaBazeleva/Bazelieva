import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def addToTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def RotateRight(self, k):
        if not self.head or k == 0 or self.size <= 1:
            return
        k = k % self.size
        if k == 0:
            return
        self.tail.next = self.head
        steps_to_new_tail = self.size - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail
    def Print(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    values = list(map(int, input_data[1:n+1]))
    k_values = list(map(int, input_data[n+1:]))
    lst = List()
    for v in values:
        lst.addToTail(v)
    for k in k_values:
        lst.RotateRight(k)
        lst.Print()