# 백준 2309 김은비

from itertools import combinations #조합

dwarf = [int(input()) for _ in range(9)] #아홉 난쟁이들의 키
dwarf.sort() #오름차순 정렬

for comb in combinations(dwarf, 7): #아홉 난쟁이 중 일곱 난쟁이를 뽑아 조합한다
    if sum(comb) == 100: #조합된 일곱 난쟁이의 키의 합이 100이라면 일곱 난쟁이의 키를 오름차순으로 출력한다
        for i in comb:
            print(i)
        break