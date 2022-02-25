import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

s = 0 #start
cnt = 0

for i in leak:
    if s < i:
        s = i + l - 1
        cnt += 1

print(cnt)