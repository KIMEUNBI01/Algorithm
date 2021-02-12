# 백준 5585 김은비

Money = int(input()) #타로가 지불할 돈
Change = 1000 - Money #거스름돈
Changes = [500, 100, 50, 10, 5, 1] #거스름돈 종류
Num = 0 #잔돈의 개수

for i in Changes:
    Num += Change // i
    Change %= i
    
print(Num)