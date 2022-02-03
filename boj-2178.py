import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    q = deque()
    q.append((0, 0))
    maze[0][0] = 2
    while q:
        y, x = q.popleft()
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < m and -1 < ny < n:
                if maze[ny][nx] == 1:
                    maze[ny][nx] = maze[y][x] + 1
                    q.append((ny, nx))
    return maze[n-1][m-1] - 1

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

print(bfs(n, m))