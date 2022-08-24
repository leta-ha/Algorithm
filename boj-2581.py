import sys
input = sys.stdin.readline

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    if x == 1:
        return False 
    return True 

m = int(input())
n = int(input())

mn = 10001
total = 0

for i in range(m, n+1):
    if is_prime(i):
        total += i
        if i < mn:
            mn = i

if total == 0:
    print(-1)
else: 
    print(total)
    print(mn)