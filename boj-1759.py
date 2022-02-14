import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
char = list(map(str, input().split()))
char.sort()

comb = combinations(char, l)
vowel = ['a', 'e', 'i', 'o', 'u']
for i in comb:
    csn = 0 #consonant
    vw = 0 #vowel
    for j in range(l):
        if i[j] in vowel:
            vw += 1
        else:
            csn += 1
    if csn >= 2 and vw >= 1:
        print(''.join(i))