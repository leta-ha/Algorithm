#채점하는데 5분 걸림. 시간초과는 안 남...뭘까
import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())
oper = list(input().split())
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ans = []

perm = permutations(num, k+1)
for i in perm:
    for j in range(k):
        bk = 0
        if oper[j] == ">":
            if int(i[j]) < int(i[j+1]):
                bk = 1 #break.. 판별
                break
        if oper[j] == "<":
            if int(i[j]) > int(i[j+1]):
                bk = 1
                break
    if bk == 1:
        continue
    ans.append(i)

print(''.join(max(ans)))
print(''.join(min(ans))) 