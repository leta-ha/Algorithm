import sys
input = sys.stdin.readline

def dfs(d):
    if d == m:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            dfs(d+1)
            ans.pop()
            

n, m = map(int, input().split())
ans = []
dfs(0)