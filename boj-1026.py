import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0

for i in range(n):
    mx = max(b)
    s += a[i]*mx
    b.remove(mx)

print(s)