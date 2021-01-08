# 백준 2231 김은비

N = int(input()) #입력값
DG = 0 #분해합(Digit Generator)

for i in range(1, N+1):
    A = list(map(int, str(i))) #각자리의 숫자들을 리스트로 만듦
    DG = i + sum(A) #분해합 = 자기자신 + 각자리의 숫자들
    
    if DG == N: 
        print(i)
        break
        
    if i == N:
        print(0)
        
