# 백준 10872 김은비

n = int(input())

def factorial(n):
    if n == 0 or n == 1: #n이 0 또는 1 이면 1 반환
        return 1
    return n * factorial(n-1) #재귀를 이용해 팩토리얼 계산

print(factorial(n))
