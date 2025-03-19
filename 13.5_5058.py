def brackets(sequence):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for bracket in sequence:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets.keys():
            if not stack or stack.pop() != brackets[bracket]:
                return "no"
    return "yes" if not stack else "no"
sequence = input().strip()
print(brackets(sequence))
