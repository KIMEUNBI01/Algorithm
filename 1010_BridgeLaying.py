# 백준 1010 김은비

import math

for _ in range(int(input())): #테스트 케이스의 개수
    N, M = map(int, input().split()) #강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M

    Case = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))
    #조합공식 이용
    
    print(Case)