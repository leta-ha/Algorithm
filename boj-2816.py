import sys
input = sys.stdin.readline

n = int(input()) #채널 수
channel = []
button = ''
for i in range(n):
    channel.append(input().strip())

k1 = channel.index('KBS1')
k2 = channel.index('KBS2')

if k1 != 0:
    button += '1' * k1 + '4' * k1
    if k1 > k2:
        k2 += 1
if k2 != 1:
    button += '1' * k2 + '4' * (k2 - 1)

print(button)