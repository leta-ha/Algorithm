import sys
input = sys.stdin.readline

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    
    same = 0
    for i in range(n):
        if same != num[i]:
            ans.append(num[i])
            same = num[i]
            dfs()
            ans.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
anss = []
dfs()