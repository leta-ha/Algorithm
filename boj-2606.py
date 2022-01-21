import sys
input = sys.stdin.readline

def dfs(x):
    global virus
    visited[x] = 1
    for i in adj[x]:
        if not visited[i]:
            virus += 1
            dfs(i)

n = int(input()) #컴퓨터 수
m = int(input()) #네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
visited = [0 for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
virus = 0
for _ in range(m):
    com1, com2 = map(int, input().split())
    adj[com1].append(com2)
    adj[com2].append(com1)

dfs(1)
print(virus)
