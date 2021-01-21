# 백준 9372 김은비 

'''
주어지는 비행 스케줄은 항상 연결 그래프를 이룬다
그렇기 떄문에 이는 최소신장트리(MST)의 특징을 이용하면 쉽게 구할 수 있다
최소신장트리(MST) -> n개의 정점을 가지는 그래프는 반드시 (n-1)개의 간선만 사용해야 한다
'''

import sys
T = int(sys.stdin.readline()) #테스트 케이스의 수
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split()) #국가의 수 N, 비행기의 종류 M    
    for _ in range(M):
        a ,b = map(int, sys.stdin.readline().split()) #a와 b 쌍들 입력 -> a와 b를 왕복하는 비행기가 있다는 것을 의미
    print(N-1) #상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수