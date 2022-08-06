import sys, math
input = sys.stdin.readline

n = int(input())
ans = math.factorial(n)
strans = str(ans)
cnt = 0
for i in range(len(strans)-1, -1, -1):
    if strans[i] == '0':
        cnt += 1
    else:
        break

print(cnt)