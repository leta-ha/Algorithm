import sys
input = sys.stdin.readline

def dfs(s): #s: start
    if len(ans) == m:
        print(*ans)
        return

    same = 0
    for i in range(n):
        if not visited[i] and same != num[i]:
            if i >= s:
                visited[i] = 1
                ans.append(num[i])
                same = num[i]
                dfs(i)
                ans.pop()
                visited[i] = 0

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
visited = [0] * n
dfs(0)