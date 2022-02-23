import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()
w = 0 #대기시간
for i in range(n):
    wait = time[:i+1]
    w += sum(wait)
print(w)