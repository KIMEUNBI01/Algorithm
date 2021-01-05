# 백준 10870 김은비

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2) #피보나치 n = (n-1)*(n-2)

N = int(input())
print(fibonacci(N))
