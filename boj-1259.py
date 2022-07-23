import sys
input = sys.stdin.readline

num = []
a = 1
while a != '0':
    a = input().strip()
    num.append(a)

for i in num:
    pal = 1
    if i == '0':
        break
    if len(i) % 2 == 0: #짝수
        for j in range(len(i)):
            if i[j] != i[len(i)-j-1]:
                pal = 0
                break
            if j == len(i) // 2:
                break
    else:
        for j in range(len(i)):
            if i[j] != i[len(i)-j-1]:
                pal = 0
                break
            if j > len(i)//2:
                break
            
    if pal == 0:
        print("no")
    elif pal == 1:
        print("yes")
