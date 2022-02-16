import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()
    # rank.sort(key = lambda x:(x[0])) #동석차 없으니 서류 기준으로만 해도 됨
    
    cnt = 1 #서류 1위면 일단 채용
    first = rank[0][1] #1위
    for i in range(1, n):
        if first > rank[i][1]:
            first = rank[i][1]
            cnt += 1
    
    print(cnt)