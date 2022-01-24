import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(x, y):
    global areas
    visited[x][y] = 1
    area = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in dxdy:
            new_x = x + dx
            new_y = y + dy
            if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]):
                if grid[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
                    area += 1
    areas.append(area)

m, n, k = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
areas = []

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            grid[i][j] = 1

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

print(len(areas))
print(*sorted(areas))