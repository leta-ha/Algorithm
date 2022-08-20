import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(i, m):
            if i == 0:
                dp[i][j] = j+1
                continue
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                
    print(dp[-1][-1])