import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
v = [0 for _ in range(len(x))]
mn = min(x)
mx = max(x)
new = 0
ch = 0 #change
for i in range(mn, mx+1, 1):
    for j in range(len(x)):
        if x[j] == i and v[j] == 0:
            x[j] = new
            v[j] = 1
            ch = 1
        if ch == 1 and j == len(x)-1: #바뀐 게 있고 리스트 1회 탐색
            new += 1
            ch = 0
        else:
            continue

print(*x)