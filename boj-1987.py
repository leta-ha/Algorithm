import sys
input = sys.stdin.readline

def dfs(y, x, s): #s: sum
    global ans
    ans = max(ans, s)
    dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if -1 < nx < c and -1 < ny < r:
            if check[alph[ny][nx]] == 0:
                check[alph[ny][nx]] = 1
                dfs(ny, nx, s+1)
                check[alph[ny][nx]] = 0

r, c = map(int, input().split())
alph = []
for _ in range(r):
    alph.append(list(map(lambda x: ord(x) - 65, input().strip())))
check = [0]*26 #26: 알파벳 개수
ans = 1
check[alph[0][0]] = 1

dfs(0, 0, ans)
print(ans)