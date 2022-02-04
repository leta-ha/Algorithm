import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur_y, cur_x):
    chess[cur_y][cur_x] = 1
    q = deque()
    q.append((cur_y, cur_x))
    while q:
        y, x = q.popleft()
        if y == des_y and x == des_x:
            return chess[des_y][des_x] - 1
        dxdy = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dy, dx in dxdy:
            ny = y + dy
            nx = x + dx
            if -1 < nx < l and -1 < ny < l:
                if chess[ny][nx] == 0:
                    chess[ny][nx] = chess[y][x] + 1
                    q.append((ny, nx))

t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0 for _ in range(l)] for _ in range(l)]
    cur_y, cur_x = map(int, input().split())
    des_y, des_x = map(int, input().split())
    print(bfs(cur_y, cur_x))