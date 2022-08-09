import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwinfo = {}

for _ in range(n):
    site, pw = input().rstrip().split()
    pwinfo[site] = pw

for _ in range(m):
    want = input().rstrip()
    print(pwinfo[want])