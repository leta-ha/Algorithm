#다른 사람들 풀이 기반
import sys
input = sys.stdin.readline

def possible(i, j, op):
    if op == "<":
        return i < j
    if op == ">":
        return i > j
    return True

def answer(cnt, s):
    global max_ans, min_ans
    if cnt == k + 1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return
    for i in range(len(num)):
        if not num[i]:
            if cnt == 0 or possible(s[-1], str(i), oper[cnt-1]):
                num[i] = 1
                answer(cnt+1, s + str(i))
                num[i] = 0

k = int(input())
oper = list(input().split())
num = [0] * 10 #0~9
max_ans = ''
min_ans = ''

answer(0, "")
print(max_ans)
print(min_ans)