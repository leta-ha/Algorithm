import sys
input = sys.stdin.readline

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i

    return fac

n = int(input())
ans = factorial(n)
strans = str(ans)
cnt = 0
for i in range(len(strans)-1, -1, -1):
    if strans[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
