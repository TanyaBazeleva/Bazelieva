def prefix(e):
    stack = []
    operators = set("+-*/")
    for char in reversed(e):
        if char in operators:
            first = stack.pop()
            second = stack.pop()
            if char in "+-" and first[0] in "*/":
                first = f"({first})"
            if char in "+-" and second[0] in "+-":
                second = f"({second})"
            if char in "*/" and second[0] in "+-":
                second = f"({second})"
            result = f"{first}{char}{second}" if char in "+-" else f"({first}{char}{second})"
            stack.append(result)
        else:
            stack.append(char)
    return stack[0]
e = input().strip()
print(prefix(e))
