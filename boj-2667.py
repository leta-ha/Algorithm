import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if map[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
town = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            town.append(cnt)
            cnt = 0
            
print(len(town))
for i in sorted(town):
    print(i)