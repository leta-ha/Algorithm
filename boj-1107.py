import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ans = abs(100 - n)

if m != 0: #고장난 버튼 존재
    broken1 = list(input().split())
else:
    broken1 = []

for i in range(1000001):
    for j in str(i):
        if j in broken1:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)