from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

perm = permutations(arr)
ans = 0

for i in perm:
    s = 0 #sum
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j+1])
    if s > ans:
        ans = s

print(ans)