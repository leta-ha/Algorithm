import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]

total = sum(height)
for i in range(9):
    for j in range(i+1, 9):
        if total - height[i] - height[j] == 100:
            first = height[i]
            second = height[j]
            break
height.remove(first)
height.remove(second)
height.sort()
for i in height:
    print(i)