# 백준 11047 김은비

import sys 

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
count = 0

for i in reversed(range(N)): #내림차순으로 정렬(동전값이 큰 것 부터 계산해야 동전을 적게내기 때문이다)
    if K == 0:
        break
    count += K // coin[i] #count에 K를 coin으로 나눈 몫을 더해준다
    K %= coin[i] #K를 coin으로 나눈 나머지로 바꿔준다

print(count)