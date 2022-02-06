import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[y][x] = 1
    q.append((y, x))
    time = 0
    while q:
        y, x = q.popleft()
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < m and -1 < ny < n:
                if tsmap[ny][nx] == 'L' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                    time = max(time, visited[ny][nx])
    return time - 1
    
n, m = map(int, input().split()) #n: 세로(y), m: 가로(x)
tsmap = []
ans = 0
for _ in range(n):
    tsmap.append(list(map(str, input().strip())))

for i in range(n):
    for j in range(m):
        if tsmap[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)