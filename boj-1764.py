import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nh = [input().strip() for _ in range(n)] #not hear
ns = [input().strip() for _ in range(m)] #not see
nhs = list(set(nh) & set(ns))

print(len(nhs))
for i in sorted(nhs):
    print(i)