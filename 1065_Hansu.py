# 백준 1065 김은비

Num = int(input())
count = 0

if (Num < 100): #100이하는 모두 한수이다
    print(Num)

else:
    for i in range(100, Num+1):
        hund = (i//100) #백의자리
        ten = (i%100//10) #십의자리
        one = (i%100%10) #일의자리
        
        if ((hund - ten) == (ten - one)): #등차수열 확인
            count += 1
            
    print(99+count)