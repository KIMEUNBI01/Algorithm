# 백준 1037 김은비 

Num = int(input()) #진짜 약수의 개수
factor = list(map(int, input().split())) #N의 진짜 약수

#N의 진짜 약수가 주어지기때문에 N = 약수 중 제일 큰 수 * 약수 중 제일 작은 수
print(max(factor) * min(factor)) 