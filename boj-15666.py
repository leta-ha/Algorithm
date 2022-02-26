import sys
input = sys.stdin.readline

def dfs(s): #s: start
    if len(ans) == m:
        print(*ans)
        return
    
    same = 0
    for i in range(n):
        if same != num[i]:
            if i >= s:
                ans.append(num[i])
                same = num[i]
                dfs(i)
                ans.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
dfs(0)