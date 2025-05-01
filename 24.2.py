from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_path(grid, start, end, n):
    visited = [[False] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]

    queue = deque()
    sx, sy = start
    ex, ey = end

    queue.append((sx, sy))
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == (ex, ey):
            break
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] in ['.', 'X']:
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)
                    queue.append((nx, ny))

    # Якщо не дійшли
    if not visited[ex][ey]:
        return False, grid

    # Відновлюємо шлях
    path = []
    x, y = ex, ey
    while (x, y) != (sx, sy):
        path.append((x, y))
        x, y = prev[x][y]
    path.reverse()

    # Малюємо шлях
    for x, y in path:
        if grid[x][y] == '.':
            grid[x][y] = '+'
        elif grid[x][y] == 'X':
            grid[x][y] = '+'
    grid[sx][sy] = '+'

    return True, grid

if __name__ == "__main__":
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    start = end = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                end = (i, j)
    found, new_grid = find_path(grid, start, end, n)
    if found:
        print('Y')
        for row in new_grid:
            print(''.join(row))
    else:
        print('N')
