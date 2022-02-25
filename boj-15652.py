import sys
input = sys.stdin.readline

def dfs(s): #s: start
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(s, n+1):
        ans.append(i)
        dfs(i)
        ans.pop()

n, m = map(int, input().split())
ans = []
dfs(1)