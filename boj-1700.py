import sys
input = sys.stdin.readline

n, k = map(int, input().split())
elec = list(map(int, input().split()))
mt = [0]*n #multitap
ans = 0
last = 0 #가장 나중에 재사용하는 제품

for i in range(k):
    product = elec[0]
    if product in mt: #이미 꽂혀있는 경우
        elec.remove(product)
        continue
    elif 0 in mt: #빈 콘센트 존재
        mt[mt.index(0)] = product
        elec.remove(product)

    else: #위에 if문에 해당하지 않는 경우 기존 플러그를 뽑아야 함 (콘센트 만석)
        for j in mt:
            #멀티탭에 꽂혀있는 제품들 중 이후에 재사용하는 제품이 없는 경우
            if j not in elec: 
                change = j #재사용하지 않는 제품이 있으므로 이 제품을 뽑고 현재(i) 플러그를 꽂는다.
                break
            elif elec.index(j) > last: #현재 제품(j)이 가장 나중에 재사용하는 제품인 경우
                #가장 나중에 사용하는 제품을 뽑고 현재 제품을 꽂는다.
                last = elec.index(j)
                change = j #우선 여기서 바꾸기로 함 
                #그러나, for j in mt 문을 돌면서 이후에 재사용하지 않는 제품이 콘센트에 꽂혀져있다면 그 제품을 뽑을 것

        mt[mt.index(change)] = product #바꾸기로 한 제품(change)이 꽂혀있는 콘센트에 현재 제품(product)을 꽂는다.
        elec.remove(product)
        last = 0 
        ans += 1

print(ans)