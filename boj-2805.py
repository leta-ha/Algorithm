import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

ans = max(tree)
lth = 0
while True:
    for i in tree:
        if i > ans:
            lth += i - ans
    if lth == m:
        break
    ans -= 1
    lth = 0

print(ans)