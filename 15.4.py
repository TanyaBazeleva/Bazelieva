class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def empty(self):
        return self.head is None

    def set_first(self):
        self.current = self.head

    def set_last(self):
        self.current = self.tail

    def next(self):
        if self.current is None or self.current.next is None:
            raise StopIteration("Current is last")
        self.current = self.current.next

    def prev(self):
        if self.current is None or self.current.prev is None:
            raise StopIteration("Current is first")
        self.current = self.current.prev

    def current_value(self):
        if self.current is None:
            raise Exception("Current is None")
        return self.current.value

    def insert_after(self, item):
        new_node = Node(item)
        if self.current is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.prev = self.current
            new_node.next = self.current.next
            if self.current.next:
                self.current.next.prev = new_node
            self.current.next = new_node
            if self.current == self.tail:
                self.tail = new_node

    def insert_before(self, item):
        new_node = Node(item)
        if self.current is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.next = self.current
            new_node.prev = self.current.prev
            if self.current.prev:
                self.current.prev.next = new_node
            self.current.prev = new_node
            if self.current == self.head:
                self.head = new_node

    def delete(self):
        if self.current is None:
            return
        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next
        if self.current.next:
            self.current.next.prev = self.current.prev
        else:
            self.tail = self.current.prev
        self.current = self.current.next or self.tail

    def damp(self):
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next
        return result

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def swap_prev(self):
        tmp = self.current()
        self.delete()
        self.insert_before(tmp)


    def swap_next(self):
        self.next()
        self.swap_prev()
        self.prev()
