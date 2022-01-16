import sys
input = sys.stdin.readline

n = input().strip()
if len(n) == 1:
    n = '0' + n
check_n = n #while문에 쓰기 위한 n
new_n = ''
cycle = 0
while check_n != new_n:
    add = str(int(n[0]) + int(n[1]))
    if len(add) == 1:
        add = '0' + add
    new_n = n[1] + add[1]
    n = new_n
    cycle += 1

print(cycle)