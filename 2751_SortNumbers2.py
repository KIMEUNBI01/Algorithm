# 백준 2751 김은비

N = int(input()) #수의 개수
num = []

for i in range(N): #입력받은 수의 개수만큼 숫자 입력받기
    x = int(input())
    num.append(x)

for i in sorted(num): #sorted함수를 이용해 정렬 후 출력
