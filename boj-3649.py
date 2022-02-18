import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * (10**7) #cm (너비)
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        ans = []
        
        i, j = 0, n-1 #투포인터 방식
        while i < j:
            if lego[i] + lego[j] == x:
                ans.append(lego[i])
                ans.append(lego[j])
                break
            elif lego[i] + lego[j] > x:
                j -= 1
            else:
                i += 1

        if len(ans) == 0:
            print("danger")
        else:
            print("yes", end=' ')
            print(*ans)
    except:
        break