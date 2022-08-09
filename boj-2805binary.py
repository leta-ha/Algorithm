import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 1, max(tree)

while s <= e:
    mid = (s + e) // 2
    lth = 0
    for i in tree:
        if i > mid:
            lth += (i - mid)
    if lth >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)