import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input()) #전화번호 수
    tele = [input().strip() for _ in range(n)]
    tele.sort()
    cons = True #consistency
    for i in range(1,n):
        if tele[i].startswith(tele[i-1]):
            cons = False
            break
    if cons:
        print("YES")
    else:
        print("NO")