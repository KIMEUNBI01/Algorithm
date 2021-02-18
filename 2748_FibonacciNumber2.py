# 백준 2748 김은비
'''
점화식: Fn = Fn-1 + Fn-2 (n ≥ 2)
'''

n = int(input()) #90보다 작거나 같은 자연수 N
Fib = [i for i in range(n+1)] #Fibonacci[i]를 구하기 위한 배열
Fib[1] = 1 #Fib[1]은 미리 구해둔다 

for i in range(2, n+1) : #점화식을 이용하여 Fibonacci[i]를 구한다
    Fib[i] = Fib[i-1] + Fib[i-2] 
    
print(Fib[-1]) #n번째 Fibonacci 수 = 마지막 Fibonacci[i]