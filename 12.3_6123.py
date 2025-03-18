class Stack:
    def __init__(self):
        self.data = []
    def empty(self):
        return len(self.data) == 0

    def push(self, number):
        self.data.append(number)
        print("ok")
    def pop(self):
        if self.empty():
            print("error")
        else:
            print(self.data.pop())
    def back(self):
        if self.empty():
            print("error")
        else:
            print(self.data[-1])
    def size(self):
        print(len(self.data))
    def clear(self):
        self.data = []
        print("ok")

if __name__ == "__main__":
    stack = Stack()
    with open("input.txt") as f:
        for line in f.readlines():
            line_command = line.strip().split()
            if line_command[0] == "push":
                stack.push(int(line_command[1]))
            elif line_command[0] == "pop":
                stack.pop()
            elif line_command[0] == "back":
                stack.back()
            elif line_command[0] == "size":
                stack.size()
            elif line_command[0] == "clear":
                stack.clear()
            elif line_command[0] == "exit":
                print("bye")
                break