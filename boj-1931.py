import sys
input = sys.stdin.readline

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x:(x[1], x[0]))
t = 0 #time
cnt = 0

for i in range(n):
    if t <= meet[i][0]:
        t = meet[i][1]
        cnt += 1

print(cnt)