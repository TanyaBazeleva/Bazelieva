class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None
class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None
    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def Print(self) -> None:
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" ".join(result))
    def PrintReverse(self) -> None:
        def reversePrint(node: 'Node | None'):
            if node is None:
                return
            reversePrint(node.next)
            print(node.data, end=" ")
        reversePrint(self.head)
        print()

if __name__ == "__main__":
    n = int(input().strip())
    values = list(map(int, input().split()))
    linked_list = List()
    for val in values:
        linked_list.addToTail(val)
    linked_list.Print()
    linked_list.PrintReverse()