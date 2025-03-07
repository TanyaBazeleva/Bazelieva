def sequences(lst, used, k, n):
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, k + 1):
        if not used[i]:
            used[i] = True
            lst.append(i)
            sequences(lst, used, k, n)
            lst.pop()
            used[i] = False

if __name__ == "__main__":
    k, n = map(int, input().split())
    sequences([], [False] * (k + 1), k, n)
