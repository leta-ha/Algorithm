import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        y, x = q.popleft()
        for dy, dx in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < m and -1 < ny < n:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = tomato[y][x] + 1
                    q.append((ny, nx))
        
    for i in tomato:
        if 0 in i:
            return -1
    return max(map(max, tomato)) - 1

m,n = map(int, input().split()) #m: 가로, n:세로
tomato = []
q = deque()
for _ in range(n):
    tomato.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

print(bfs(n, m))