import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = [[0, 0, 0, 0]]
rank = [0 for _ in range(n+1)]
cnt_rank = [0 for _ in range(n+1)] #같은 순위인 경우를 구하기 위함
for _ in range(n):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x:(x[1], x[2], x[3])) #금, 은, 동 순으로 정렬

for i in range(len(medals)-1, 0, -1):
    if i == len(medals) -1:
        rank[medals[i][0]] = 1
        cnt_rank[1] = 1
    elif medals[i][1] == medals[i+1][1]:
        if medals[i][2] == medals[i+1][2]:
            if medals[i][3] == medals[i+1][3]:
                rank[medals[i][0]] = rank[medals[i+1][0]]
                cnt_rank[rank[medals[i][0]]] += 1
            else:
                if cnt_rank[rank[medals[i+1][0]]] != 1:
                    rank[medals[i][0]] = rank[medals[i+1][0]] + cnt_rank[rank[medals[i+1][0]]]
                else:
                    rank[medals[i][0]] = rank[medals[i+1][0]] + 1
                cnt_rank[rank[medals[i][0]]] += 1
        else:
            if cnt_rank[rank[medals[i+1][0]]] != 1:
                rank[medals[i][0]] = rank[medals[i+1][0]] + cnt_rank[rank[medals[i+1][0]]]
            else:
                rank[medals[i][0]] = rank[medals[i+1][0]] + 1
            cnt_rank[rank[medals[i][0]]] += 1
    else:
        if cnt_rank[rank[medals[i+1][0]]] != 1:
            rank[medals[i][0]] = rank[medals[i+1][0]] + cnt_rank[rank[medals[i+1][0]]]
        else:
            rank[medals[i][0]] = rank[medals[i+1][0]] + 1
        cnt_rank[rank[medals[i][0]]] += 1

print(rank[k])