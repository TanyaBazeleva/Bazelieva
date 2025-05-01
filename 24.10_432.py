from collections import deque

DIRECTIONS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def escape_time(l, r, c, dungeon):
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    queue = deque()
    for z in range(l):
        for x in range(r):
            for y in range(c):
                if dungeon[z][x][y] == 'S':
                    queue.append((z, x, y, 0))
                    visited[z][x][y] = True
    while queue:
        z, x, y, minutes = queue.popleft()
        if dungeon[z][x][y] == 'E':
            return f"Escaped in {minutes} minute(s)."
        for dz, dx, dy in DIRECTIONS:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if not visited[nz][nx][ny] and dungeon[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, minutes + 1))
    return "Trapped!"

if __name__ == "__main__":
    while True:
        l, r, c = map(int, input().split())
        if l == 0 and r == 0 and c == 0:
            break
        dungeon = []
        for _ in range(l):
            level = [list(input().strip()) for _ in range(r)]
            dungeon.append(level)
            input()
        result = escape_time(l, r, c, dungeon)
        print(result)
