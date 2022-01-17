import sys
input = sys.stdin.readline

def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 1:
        return False
    return True

def is_palindrome(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != n[len(n) - 1 - i]:
            return False
    return True

n = int(input())
result = n
while True:
    if is_palindrome(result):
        if is_prime_number(result):
            print(result)
            break
    result += 1