import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
    visited = [-1 for _ in range(n+1)]
    q = deque()
    q.append(i)
    visited[i] = 0
    while q:
        w = q.popleft()
        for j in friend[w]:
            if visited[j] == -1:
                visited[j] = visited[w] + 1
                q.append(j)
    return sum(visited)

n, m = map(int, input().split())
friend = [[] for _ in range(n+1)]
ans = [float("inf")]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(1, n+1):
    ans.append(bfs(i))

print(ans.index(min(ans)))