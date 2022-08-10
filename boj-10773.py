import sys
input = sys.stdin.readline

k = int(input())
num = []
for i in range(k):
    n = int(input())
    if n == 0:
        del num[-1]
    else:
        num.append(n)

print(sum(num))