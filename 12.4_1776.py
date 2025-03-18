from collections import deque

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    i = 0
    results = []
    while i < len(lines):
        n = int(lines[i].strip())
        if n == 0:
            break
        i += 1
        test_results = []
        while i < len(lines) and lines[i].strip() != "0":
            permutation = list(map(int, lines[i].strip().split()))
            stack = deque()
            current = 1
            possible = True
            for car in permutation:
                while current <= n and (not stack or stack[-1] != car):
                    stack.append(current)
                    current += 1
                if stack and stack[-1] == car:
                    stack.pop()
                else:
                    possible = False
                    break
            test_results.append("Yes" if possible else "No")
            i += 1
        results.append("\n".join(test_results))
        results.append("")
        i += 1
    print("\n\n".join(results).strip())
