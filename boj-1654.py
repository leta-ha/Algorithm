import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

s = 1
e = max(lan)

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)

# k, n = map(int, input().split())
# lan = [int(input()) for _ in range(k)]

# mx = sum(lan)//n
# cnt = 0
# while True:
#     for i in lan:
#         cnt += i//mx
#     if cnt != n:
#         mx -= 1
#         cnt = 0
#     else:
#         break

# print(mx)