from collections import deque
import sys
def main():
    d = deque()
    commands = {
        "push_front": lambda x: (d.appendleft(x), print("ok")),
        "push_back": lambda x: (d.append(x), print("ok")),
        "pop_front": lambda: print(d.popleft()) if d else print("error"),
        "pop_back": lambda: print(d.pop()) if d else print("error"),
        "front": lambda: print(d[0]) if d else print("error"),
        "back": lambda: print(d[-1]) if d else print("error"),
        "size": lambda: print(len(d)),
        "clear": lambda: (d.clear(), print("ok")),
        "exit": lambda: (print("bye"), sys.exit()), }
    for line in sys.stdin:
        parts = line.strip().split()
        cmd = parts[0]
        if cmd in {"push_front", "push_back"}:
            commands[cmd](parts[1])
        elif cmd in commands:
            commands[cmd]()
if __name__ == "__main__":
    main()
