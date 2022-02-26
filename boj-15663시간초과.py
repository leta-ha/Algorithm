import sys
input = sys.stdin.readline

def inter_dfs(i):
    global ans, num
    ans.append(num[i])
    dfs()
    ans.pop()

def dfs():
    if len(ans) == m and ans not in anss:
        anss.append(ans[:])
        print(*ans)
        return
    elif ans in anss:
        return
    
    for i in range(n):
        if num.count(num[i]) > 1:
            inter_dfs(i)
        else:
            if num[i] not in ans:
                inter_dfs(i)

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
anss = []
dfs()