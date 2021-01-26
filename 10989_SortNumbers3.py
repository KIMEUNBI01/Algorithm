#백준 10989 김은비 

import sys

N = int(sys.stdin.readline())
List = [0 for _ in range(10001)] #숫자의 빈도를 세기 위해 10001으로 제한한 배열

for _ in range(N): #입력된 숫자의 빈도 계산
    List[int(sys.stdin.readline())] += 1

for i in range(1, 10001): #1부터 10000까지 오름차순으로 앞에서 저장된 빈도 만큼 숫자 출력
    Num = List[i]
    for _ in range(Num):
        print(i)
