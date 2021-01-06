# 백준 2750 김은비

N = int(input())
num = []

for _ in range(N) : 
    num.append(int(input()))

# Bubble Sort
for i in range(len(num)) : 
    for j in range(len(num)) : 
        if num[i] < num[j] : 
            num[i], num[j] = num[j], num[i]
            
for n in num : 
    print(n)
