import sys
input = sys.stdin.readline

t = int(input()) #test case 개수
for i in range(t):
    n = int(input()) #의상 수
    clothes = {}
    for j in range(n):
        c_n, c_t = input().split() #clothes_name, clothes_type

        #종류별로 분류
        if c_t not in clothes.keys():
            clothes[c_t] = 1
        else:
            clothes[c_t] += 1
    
    ans = 1
    for i in clothes: #i: key
        ans *= (clothes[i]+1) #해당 종류는 안 입는 경우 포함
    print(ans-1) #알몸인 경우 제외