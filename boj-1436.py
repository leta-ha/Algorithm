import sys
input = sys.stdin.readline

n = int(input())

ans = '666'
cnt = 1
while cnt != n:
    intans = int(ans)
    intans += 1
    ans = str(intans)
    if '666' in ans:
        cnt += 1
print(ans)