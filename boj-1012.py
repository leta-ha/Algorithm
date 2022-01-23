import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == m-1 and y == n-1:
            break
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in dxdy:
            new_x = x + dx
            new_y = y + dy
            if -1 < new_x < len(matrix) and -1 < new_y < len(matrix[0]):
                if matrix[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
                

t = int(input()) #테스트 케이스 개수
for _ in range(t):
    m, n, k = map(int, input().split()) #m: 가로, n: 세로, k: 배추 심어진 위치 개수
    visited = [[0 for _ in range(n)] for _ in range(m)]
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    worm = 0
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                worm += 1

    print(worm)
