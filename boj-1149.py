import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) #i번째를 빨강으로 칠하기
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) #초록
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) #파랑

print(min(cost[-1]))