import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
diff = [x, y, w-x, h-y]
ans = min(diff)
print(ans)