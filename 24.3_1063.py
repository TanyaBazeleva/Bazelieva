from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def count_pieces(m, n, grid):
    visited = [[False for _ in range(n)] for _ in range(m)]
    pieces = 0
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny] and grid[nx][ny] == '#':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                pieces += 1
    return pieces

if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    result = count_pieces(m, n, grid)
    print(result)
