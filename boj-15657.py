import sys
input = sys.stdin.readline

def dfs(s): #s: start
    if len(ans) == m:
        print(*ans)
        return

    for i in num:
        if i >= s:
            ans.append(i)
            dfs(i)
            ans.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
dfs(0)