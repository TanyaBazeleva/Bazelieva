class Queue:
    def __init__(self):
        self.items = []
    def push(self, n):
        self.items.append(n)
        print("ok")
    def pop(self):
        if self.items:
            print(self.items.pop(0))
        else:
            print("error")
    def front(self):
        if self.items:
            print(self.items[0])
        else:
            print("error")
    def size(self):
        print(len(self.items))
    def clear(self):
        self.items = []
        print("ok")
    def exit(self):
        print("bye")
        exit()
if __name__ == "__main__":
    queue = Queue()
    while True:
        command = input().strip().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "size":
            queue.size()
        elif command[0] == "clear":
            queue.clear()
        elif command[0] == "exit":
            queue.exit()